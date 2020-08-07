import urllib.request


def test_urlopen():
    with urllib.request.urlopen("https://www.google.com") as r:
        r.read()
    with urllib.request.urlopen("https://matplotlib.org/1.5.0/_static/logo2.png") as r2:
        r2.read()
    print()
