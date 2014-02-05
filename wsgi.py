# https://code.google.com/p/modwsgi/wiki/VirtualEnvironments

import os
os.chdir(os.path.dirname(__file__))

import site
site.addsitedir(os.getcwd())

from application import app as application
