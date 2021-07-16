import os


def enable_proxy(mode=True):
    cmd = f'echo "{os.environ["IOS_HOST_PASSWORD"]}" | sudo -S networksetup '
    cmd += '-setsecurewebproxy Wi-Fi 0.0.0.0 8080' if mode else '-setsecurewebproxystate Wi-Fi off'
    os.system(cmd)