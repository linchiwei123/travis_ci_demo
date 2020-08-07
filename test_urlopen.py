import urllib.request


def test_urlopen():
    r = urllib.request.urlopen("https://www.google.com")
    r.read()
