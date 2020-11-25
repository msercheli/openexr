# -*- coding: utf-8 -*-

name = "openexr"

version = "2.5.99"

authors = ["Industrial Light and Magic"]

requires = [

]

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.OPENEXR_ROOT = "{root}"
    env.OPENEXR_LOCATION = "{root}"
    env.EXR_ROOT = "{root}"
    env.EXR_LOCATION = "{root}"

uuid = "repository.openexr"
