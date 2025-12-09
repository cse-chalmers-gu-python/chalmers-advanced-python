"""
Search for user in Canvas course, using HTTP API
"""

import os
from dotenv import load_dotenv
import requests

# Read token from .env file
load_dotenv()
api_token = os.getenv("CANVAS_API_TOKEN")

# Prepare URL
canvas_base_url = "https://chalmers.instructure.com/api/v1"
course_id = "36887"
headers = {
  "Authorization": f"Bearer {api_token}"
}
url = f"{canvas_base_url}/courses/{course_id}/search_users?enrollment_type=ta"

# Make request
response = requests.get(url, headers=headers)
response.raise_for_status()

# Print results
print(response.json())
# results = response.json()
# print(f"{len(results)} results")
# for res in results:
#   print('-', res["name"])
