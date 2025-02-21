import requests

from typing import Any, Dict



def loadData() -> list[Dict[str, Any]]:
    
    responseStream = requests.get("https://nutrito.vercel.app/api/alternativeproducts?secretkey=thisismysecretkey")
    if responseStream.status_code == 200:
        return responseStream.json().get("products", [])
    else:
        responseStream.raise_for_status()

