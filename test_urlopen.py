import urllib.request

import pytest


@pytest.mark.parametrize(
    "url",
    ["https://www.google.com", "https://matplotlib.org/1.5.0/_static/logo2.png"]
)
def test_urlopen(url):
    with urllib.request.urlopen(url) as r:
        r.read()
