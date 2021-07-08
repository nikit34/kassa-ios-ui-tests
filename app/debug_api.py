import os
from datetime import datetime
from mitmproxy.options import Options
from mitmproxy.proxy.config import ProxyConfig
from mitmproxy.proxy.server import ProxyServer
from mitmproxy.tools.dump import DumpMaster
import threading
import asyncio
from time import time
import json


def _logging(this, method, url, content=''):
    path_dir_log = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '/app/'
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
    def __init__(self, request=True, response=True, switch_proxy=True, timeout_recard=0):
        self.request = request
        self.response = response
        self.switch_proxy = switch_proxy
        self.timeout_recard = timeout_recard
        self.path_log = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '/app/'

    class AddonReqRes:
        def __init__(self, timeout_recard):
            self.timeout_recard = timeout_recard
            self.timeout_now = time()

        def request(self, flow):
            this = 'request'
            method = flow.request.method
            url = flow.request.url
            content = flow.request.content.decode('UTF-8')
            if time() - self.timeout_now >= self.timeout_recard:
                _logging(this, method, url, content)

        def response(self, flow):
            this = 'response'
            method = flow.request.method
            url = flow.request.url
            content = flow.response.content.decode('UTF-8')
            if time() - self.timeout_now >= self.timeout_recard:
                _logging(this, method, url, content)

    class AddonReq:
        def __init__(self, timeout_recard):
            self.timeout_recard = timeout_recard
            self.timeout_now = time()

        def request(self, flow):
            this = 'request'
            method = flow.request.method
            url = flow.request.url
            content = flow.request.content.decode('UTF-8')
            if time() - self.timeout_now >= self.timeout_recard:
                _logging(this, method, url, content)

    class AddonRes:
        def __init__(self, timeout_recard):
            self.timeout_recard = timeout_recard
            self.timeout_now = time()

        def response(self, flow):
            this = 'response'
            method = flow.request.method
            url = flow.request.url
            content = flow.response.content.decode('UTF-8')
            if time() - self.timeout_now >= self.timeout_recard:
                _logging(this, method, url, content)

    @staticmethod
    def _loop_in_thread(loop, m):
        asyncio.set_event_loop(loop)
        t = threading.currentThread()
        while getattr(t, "open_loop", True):
            m.run_loop(loop.run_forever)
        loop.stop()

    def _setup(self):
        options = Options(listen_host='0.0.0.0', listen_port=8080, http2=True)
        m = DumpMaster(options, with_termlog=False, with_dumper=False)
        config = ProxyConfig(options)
        m.server = ProxyServer(config)
        self._addon_setup(m)
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
        self._start_logging()

    @classmethod
    def run(cls, request=True, response=True, switch_proxy=True, timeout_recard=0):
        self = cls(request, response, switch_proxy, timeout_recard)
        if self.switch_proxy:
            self.enable_proxy(mode=True)
        m = self._setup()
        loop = asyncio.get_event_loop()
        t = threading.Thread(target=self._loop_in_thread, args=(loop, m))
        t.start()
        setattr(self, 'm', m)
        setattr(self, 't', t)
        return self

    def kill(self):
        self.m.shutdown()
        self.t.join()
        if self.switch_proxy:
            self.enable_proxy(mode=False)
        self.clear_buffer()

    @staticmethod
    def enable_proxy(mode=True):
        if mode:
            os.system(f'echo "{os.environ["IOS_HOST_PASSWORD"]}" | sudo -S networksetup -setsecurewebproxy Wi-Fi 0.0.0.0 8080')
        else:
            os.system(f'echo "{os.environ["IOS_HOST_PASSWORD"]}" | sudo -S networksetup -setsecurewebproxystate Wi-Fi off')

    def read_buffer(self, read_mapi=True):
        file = self.path_log
        if read_mapi:
            file += 'mapi.log'
        else:
            file += 'other.log'
        count = 0
        with open(file, 'r') as reader:
            for line in reader.readlines():
                count += 1
                yield line

    @staticmethod
    def get_content_response(line):
        split_line = line.split(';', 4)
        if len(split_line) < 5:
            raise ValueError('response is not valid')
        return json.loads(split_line[4])

    def clear_buffer(self):
        open(self.path_log + 'mapi.log', 'w').close()
        open(self.path_log + 'other.log', 'w').close()

    def keep_buffer(self, old_name='mapi.log', new_name=''):
        os.rename(self.path_log + old_name, self.path_log + new_name)


