from urllib2 import urlopen


def a(something,somethingelse):
    return something+somethingelse
def c(url):
    return urlopen(url).read()
