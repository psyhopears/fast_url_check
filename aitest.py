import asyncio
from aiohttp import ClientSession, ClientConnectorError

async def fetch_html(url: str, session: ClientSession, **kwargs) -> tuple:
    try:
        resp = await session.request(method="GET", url=url, **kwargs)
    except ClientConnectorError:
        print(url, 404)
    # return (url, resp.status)
    print(url, resp.status, "OK")

async def make_requests(urls: set, **kwargs) -> None:
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(
                fetch_html(url=url, session=session, **kwargs)
            )
        results = await asyncio.gather(*tasks)

    for result in results:
        print(f'{result[1]} - {str(result[0])}')

if __name__ == "__main__":
    import sys
    assert sys.version_info >= (3, 7), "Script requires Python 3.7+."
    with open("3.txt") as infile:
        urls = set(map(str.strip, infile))
    asyncio.run(make_requests(urls=urls))
