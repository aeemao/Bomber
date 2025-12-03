class ProxyManager():
    def __init__(self):
        with open('proxies.txt', 'r') as file:
            self.proxies = file.readlines()

    def get_proxy_list(self):
        return self.proxies
