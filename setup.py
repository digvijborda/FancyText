import os
from setuptools import setup

#For more help on the package, go to https://github.com/George-Leonard/pyfont
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pyfont",
    version = "1.0",
    author = "George Leonard",
    description = ("A python font converting package"),
    keywords = "https://github.com/George-Leonard/pyfont",
    url = "",
    packages=['pyfont', 'tools'],
)