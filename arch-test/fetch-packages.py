#!/bin/python
import requests

GROUP = "11323"
BASE_URL = f"https://gitlab.archlinux.org/api/v4/groups/{GROUP}/projects"
params = {
    "per_page": 100,
    "archived": "false",
}

projects = []
page = 1

while True:
    params["page"] = page
    r = requests.get(BASE_URL, params=params)
    data = r.json()
    if not data:
        break
    projects.extend(data)
    if r.headers.get("X-Next-Page"):
        page += 1
    else:
        break

for p in projects:
    print(p["name"])
