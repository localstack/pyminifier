import sys
import pyminifier
from setuptools import setup
from distutils.command.install import INSTALL_SCHEMES

for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

extra = {}

if isinstance(sys.version_info, tuple):
    major = sys.version_info[0]
else:
    major = sys.version_info.major

try:
	from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
	print("Python 3.X support requires the 2to3 tool.")
	sys.exit(1)

cmdclass = {'build_py': build_py}

setup(
    name="pyminifier-ls",
    version=pyminifier.__version__,
    description="Python code minifier, obfuscator, and compressor",
    author=pyminifier.__author__,
    cmdclass=cmdclass,
    author_email="daniel.mcdougall@liftoffsoftware.com",
    url="https://github.com/liftoff/pyminifier",
    license="Proprietary",
    packages=['pyminifier'],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    provides=['pyminifier'],
    entry_points = {
        'console_scripts': [
            'pyminifier = pyminifier.__main__:main'
        ],
    },
    test_suite = "tests",
    **extra
)
