import aiohttp
import asyncio

async def kursy(kurs, dni):
    url = f"http://api.nbp.pl/api/exchangerates/rates/a/{kurs}/last/{dni}/?format=json"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    result = await response.json()
                    return result
                else:
                    print(f"ERROR: Failed to fetch data for {kurs.upper()}, status code: {response.status}")
                    return None
    except aiohttp.ClientError as e:
        print(f"ERROR: An error occurred while fetching data for {kurs.upper()}: {e}")
        return None

async def main():
    kursy_list = ['usd', 'eur']
    dni = 10
    for kurs in kursy_list:
        rates = await kursy(kurs, dni)
        if rates:
            print(f"Exchange rates for {kurs.upper()}:")
            for rate in rates['rates']:
                print(f"Kurs z dnia {rate['effectiveDate']}: {kurs.upper()} {rate['mid']}")
            print()

if __name__ == "__main__":
    asyncio.run(main())

