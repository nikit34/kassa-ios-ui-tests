import redis
from datetime import datetime


class RedisServer:
    def __init__(self, host='localhost', port=6379, db=0):
        self.item = redis.Redis(host=host, port=port, db=db)

    def connect_pubsub(self):
        p = self.item.pubsub()
        setattr(self, 'p', p)

    def start_listen(self, mapi_handler, other_handler):
        channels = self.check_handlers(mapi_handler, other_handler)
        channel_handler = {
            'mapi_log_channel': mapi_handler,
            'other_log_channel': other_handler,
        }
        if channels:
            if isinstance(channels, tuple):
                for channel in channels:
                    self.p.subscribe(**{channel: channel_handler[channel]})
            elif isinstance(channels, str):
                self.p.subscribe(**{channels: channel_handler[channels]})
            t_redis = self.p.run_in_thread(sleep_time=0.001)
            setattr(self, 't_redis', t_redis)

    @staticmethod
    def check_handlers(mapi_handler, other_handler):
        if mapi_handler is not None and other_handler is not None:
            return 'mapi_log_channel', 'other_log_channel'
        elif mapi_handler is not None:
            return 'mapi_log_channel'
        elif other_handler is not None:
            return 'other_log_channel'
        else:
            return False

    def kill_redis(self):
        self.item.flushall()
        self.t_redis.stop()


class RedisClient:
    def __init__(self, host='localhost', port=6379, db=0):
        self.item = redis.Redis(host=host, port=port, db=db)

    def logging(self, this, method, url, content):
        logging_time = datetime.now().strftime("%H:%M:%S")
        if 'mapi.kassa.rambler.ru' in url:
            line = logging_time + ';' + this + ';' + method + ';' + url + ';' + content
            channel = 'mapi_log_channel'
        else:
            line = logging_time + ';' + this + ';' + method + ';' + url
            channel = 'other_log_channel'
        self.item.publish(channel, line)

