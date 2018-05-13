#!/usr/bin/env python3

import urllib.request
import json

repos = [
    'Bilibili/ijkplayer',
    'facebook/react-native',
    'facebook/react',
    'golang/go',
]

PAGES = 10

for repo in repos:
    out = []
    for n in range(10):
        out += json.loads(urllib.request.urlopen(
            f"https://api.github.com/repos/{repo}"
            "/issues"
            f"?page={n+1}"
            "&per_page=100"
        ).read())

    with open(f'{repo.replace("/", "-")}.json', 'w') as f:
        f.write(json.dumps(out))
