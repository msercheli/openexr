# -*- coding: utf-8 -*-

name = "openexr"

version = "2.3.0"

authors = ["Industrial Light and Magic"]

requires = [
    "boost-1.55.0",
]

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")

uuid = "repository.openexr"
