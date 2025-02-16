import requests
import os
from typing import Any, Dict


def loadData() -> list[Dict[str, Any]]:
    secreteKey = os.getenv("MONGO_KEY")
    if secreteKey is None:
        raise ValueError("MONGO_KEY environment variable is not set")
    responseStream = requests.get("https://nutrito.vercel.app/api/alternativeproducts?secretkey=" + secreteKey)
    if responseStream.status_code == 200:
        return responseStream.json().get("products", [])
    else:
        responseStream.raise_for_status()


