"""
Run in console:
_distribute.py py2exr
"""
from distutils.core import setup
import os

# Name of the main() program/python file
script_file = 'RandomNPC.py'

# Setup args that apply to all setups, including ordinary distutils.
setup_args = dict()
    
# Version: py2exe options
import py2exe

setup_args.update(dict(
    console=[dict(script=script_file)],
    options={
        "py2exe": {
            'bundle_files':1,
            'compressed':True,
            'ascii':True,
            'dll_excludes':['w9xpopen.exe'],
            'unbuffered':True
            }}),
                  zipfile = None)

# Version: py2app
# try:
#     import py2app
#     setup_args.update(dict(
#         app=[script_file],
#         options=dict(py2app=dict(
#             argv_emulation=True,
#             iconfile='assets/app.icns',
#         )),
#     ))
# except ImportError:
#     pass

setup(**setup_args)
