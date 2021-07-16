import os
from datetime import datetime
from mitmproxy.options import Options
from mitmproxy.proxy.config import ProxyConfig
from mitmproxy.proxy.server import ProxyServer
from mitmproxy.tools.dump import DumpMaster
import threading
import asyncio
from time import time


from logging_api.redis_api import RedisServer, RedisClient
from utils.internet import enable_proxy


def _logging(this, method, url, content=''):
    path_dir_log = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '/logs/'
    logging_time = datetime.now().strftime("%H:%M:%S")
    if 'mapi.kassa.rambler.ru' in url:
        path_log = path_dir_log + 'mapi.log'
        line = logging_time + ';' + this + ';' + method + ';' + url + ';' + content + '\n'
    else:
        path_log = path_dir_log + 'other.log'
        line = logging_time + ';' + this + ';' + method + ';' + url + '\n'
    with open(path_log, 'a+') as f:
        f.write(line)


class DebugAPI:
    def __init__(self, request=True, response=True, mapi_handler=None, other_handler=None, file_logging=False, switch_proxy=True, timeout_recard=0):
        self.request = request
        self.response = response
        self.mapi_handler = mapi_handler
        self.other_handler = other_handler
        self.switch_proxy = switch_proxy
        self.file_logging = file_logging
        self.timeout_recard = timeout_recard
        self.path_log = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '/logs/'

    class AddonReqRes:
        def __init__(self, timeout_recard, file_logging=False):
            self.timeout_recard = timeout_recard
            self.timeout_now = time()
            self.rc = RedisClient(host='localhost', port=6379, db=0)
            self.file_logging = file_logging

        def request(self, flow):
            this = 'request'
            method = flow.request.method
            url = flow.request.url
            content = flow.request.content.decode('UTF-8')
            if time() - self.timeout_now >= self.timeout_recard:
                if self.file_logging: _logging(this, method, url, content)
                self.rc.logging(this, method, url, content)

        def response(self, flow):
            this = 'response'
            method = flow.request.method
            url = flow.request.url
            content = flow.response.content.decode('UTF-8')
            if time() - self.timeout_now >= self.timeout_recard:
                if self.file_logging: _logging(this, method, url, content)
                self.rc.logging(this, method, url, content)

    class AddonReq:
        def __init__(self, timeout_recard, file_logging=False):
            self.timeout_recard = timeout_recard
            self.timeout_now = time()
            self.rc = RedisClient(host='localhost', port=6379, db=0)
            self.file_logging = file_logging

        def request(self, flow):
            this = 'request'
            method = flow.request.method
            url = flow.request.url
            content = flow.request.content.decode('UTF-8')
            if time() - self.timeout_now >= self.timeout_recard:
                if self.file_logging: _logging(this, method, url, content)
                self.rc.logging(this, method, url, content)

    class AddonRes:
        def __init__(self, timeout_recard, file_logging=False):
            self.timeout_recard = timeout_recard
            self.timeout_now = time()
            self.rc = RedisClient(host='localhost', port=6379, db=0)
            self.file_logging = file_logging

        def response(self, flow):
            this = 'response'
            method = flow.request.method
            url = flow.request.url
            content = flow.response.content.decode('UTF-8')
            if time() - self.timeout_now >= self.timeout_recard:
                if self.file_logging: _logging(this, method, url, content)
                self.rc.logging(this, method, url, content)

    @staticmethod
    def _loop_in_thread(loop, m):
        asyncio.set_event_loop(loop)
        m.run_loop(loop.run_forever)

    def _setup(self):
        options = Options(listen_host='0.0.0.0', listen_port=8080, http2=True)
        m = DumpMaster(options, with_termlog=False, with_dumper=False)
        config = ProxyConfig(options)
        m.server = ProxyServer(config)
        self._addon_setup(m)
        if RedisServer.check_handlers(self.mapi_handler, self.other_handler):
            redis_server = RedisServer()
            redis_server.connect_pubsub()
            setattr(self, 'redis_server', redis_server)
        return m

    def _start_logging(self):
        start_time = datetime.now().strftime("%H:%M:%S")
        with open(self.path_log + 'mapi.log', 'a+') as f:
            f.write(start_time + '\n')

    def _addon_setup(self, m):
        if self.request and self.response:
            m.addons.add(self.AddonReqRes(self.timeout_recard))
        elif self.request:
            m.addons.add(self.AddonReq(self.timeout_recard))
        elif self.response:
            m.addons.add(self.AddonRes(self.timeout_recard))
        else:
            raise KeyError('[ERROR] Addon will not be exist')
        if self.file_logging: self._start_logging()

    @classmethod
    def run(cls, request=True, response=True, mapi_handler=None, other_handler=None, file_logging=False, switch_proxy=True, timeout_recard=0):
        self = cls(request, response, mapi_handler, other_handler, file_logging, switch_proxy, timeout_recard)
        if self.switch_proxy: enable_proxy(mode=True)
        m = self._setup()
        loop = asyncio.get_event_loop()
        t = threading.Thread(target=self._loop_in_thread, args=(loop, m))
        t.start()
        setattr(self, 't', t)
        setattr(self, 'm', m)
        if hasattr(self, 'redis_server'): self.redis_server.start_listen(self.mapi_handler, self.other_handler)
        return self

    def kill(self):
        self._kill_mitmproxy()
        if hasattr(self, 'redis_server'): self.redis_server.kill_redis()
        if self.file_logging: self.clear_buffer()
        if self.switch_proxy: enable_proxy(mode=False)

    def _kill_mitmproxy(self):
        self.m.shutdown()
        self.t.join()

    def clear_buffer(self):
        open(self.path_log + 'mapi.log', 'w').close()
        open(self.path_log + 'other.log', 'w').close()
        open(self.path_log + 'redis_filter.log', 'w').close()

    def read_buffer(self, name_file=None):
        file = self.path_log
        if name_file:
            file += name_file
        with open(file, 'r') as reader:
            for line in reader.readlines():
                yield line

    def keep_buffer(self, old_name='', new_name=''):
        os.rename(self.path_log + old_name, self.path_log + new_name)


