import asyncio

from proxy_manager import ProxyManager
from services.service_manager import service_list

proxy_manager = ProxyManager()

async def _bounded_send(service, proxy, phone_number, semaphore: asyncio.Semaphore):
    async with semaphore:
        return await service.send_request(proxy_url=proxy, phone_number=phone_number)

async def bombing(max_concurrent=20):
    phone_number = input('Номер телефона в формате 79999999999: ')
    proxy_list = proxy_manager.get_proxy_list()

    semaphore = asyncio.Semaphore(max_concurrent)

    tasks = [
        _bounded_send(service, proxy.rstrip('\n'), phone_number, semaphore)
        for proxy in proxy_list
        for service in service_list
    ]

    await asyncio.gather(*tasks)


async def main():
    await bombing(max_concurrent=10)

if __name__ == '__main__':
    asyncio.run(main())