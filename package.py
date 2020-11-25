# -*- coding: utf-8 -*-

name = "openexr"

version = "2.5.99"

authors = ["Industrial Light and Magic"]

requires = [

]

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")

uuid = "repository.openexr"
