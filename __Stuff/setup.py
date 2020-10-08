# https://www.py2exe.org/index.cgi/Tutorial

from distutils.core import setup
import backend
import py2exe

setup(console=['frontend.py'])