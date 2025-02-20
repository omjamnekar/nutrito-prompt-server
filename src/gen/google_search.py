import os
from dotenv import load_dotenv

import aiohttp
load_dotenv()

API_KEY =os.getenv("SEARCH_API")
SEARCH_ENGINE_ID=os.getenv("SEARCH_ID")


async def googleSearchImage(search_query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': search_query,
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'searchType': 'image',
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            results = await response.json()
            if 'items' in results:
                return results['items'][0]['link']
