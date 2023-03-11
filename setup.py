import sys

from setuptools import find_packages, setup

if sys.version_info < (3, 0):
    sys.exit("Sorry, Python < 3.0 is not supported")

import re

VERSIONFILE = "midl2impacket/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

entry_points = {
    'console_scripts': [
        "midl2impacket = midl2impacket.midl2imp:main",
        "idlpp = midl2impacket.idl_preprocessor:main",
        "idl_scraper = midl2impacket.idl_scraper:main",
        "idlfix = midl2impacket.idl_fix:main",
    ],
}

install_requires = [
    "impacket >= 0.10.0",
]

setup(
    name="midl2impacket",
    version=verstr,
    description="midl2impacket",
    long_description="Please visit origin repo `Github <https://github.com/T-RN-R/midl2impacket>`_ for more information.",
    author="midl2impacket project developers",
    author_email="",
    url="https://github.com/saycv/midl2impacket",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    entry_points=entry_points,
    include_package_data=True,
    install_requires=install_requires,
)
