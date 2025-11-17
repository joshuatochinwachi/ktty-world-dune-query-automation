import os
import requests

# Get API key from environment variable
dune_api_key = os.getenv("DEFI_JOSH_DUNE_QUERY_API_KEY")

if not dune_api_key:
    raise ValueError("API key not found in environment variables")

query_ids = [5748715, 5822954, 5517268, 5517376, 5692998, 5510269, 5519323, 5510514, 5515772, 5516718, 5516764, 5517177, 5517021, 5516616, 5517559, 5517965, 5518130, 5517738, 5518374, 6005382, 6005998, 6006246, 6006127, 6006249]  # KTTY World queries

headers = {"X-DUNE-API-KEY": dune_api_key}

for query_id in query_ids:
    url = f"https://api.dune.com/api/v1/query/{query_id}/execute"
    response = requests.post(url, headers=headers)
    print(f"Query {query_id}: {response.status_code} - {response.text}")
