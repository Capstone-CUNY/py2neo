#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2011-2014, Nigel Small
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import sys

try:
    from setuptools import setup
    from setuptools.extension import Extension
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension

from py2neo import __author__, __email__, __license__, __package__, __version__


python_2 = sys.version_info < (3,)

package_metadata = {
    "name": __package__,
    "version": __version__,
    "description": "Python client library and toolkit for Neo4j",
    "long_description": "Py2neo is a comprehensive toolkit for working with Neo4j from within "
                        "Python applications or from the command line. The library has no "
                        "external dependencies and has been carefully designed to be easy and "
                        "intuitive to use.",
    "author": __author__,
    "author_email": __email__,
    "url": "http://nigelsmall.com/py2neo",
    "scripts": [
        "scripts/neotool",
    ],
    "packages": [
        "py2neo",
        "py2neo.batch",
        "py2neo.cypher",
        "py2neo.ext",
        "py2neo.ext.admin",
        "py2neo.ext.calendar",
        "py2neo.ext.gremlin",
        "py2neo.ext.ogm",
        "py2neo.legacy",
        "py2neo.packages",
        "py2neo.packages.httpstream",
        "py2neo.packages.httpstream.packages",
        "py2neo.packages.httpstream.packages.urimagic",
        "py2neo.packages.jsonstream",
        "py2neo.tool",
    ],
    "license": __license__,
    "classifiers": [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Database",
        "Topic :: Software Development",
    ],
    "zip_safe": False,
}

extensions = []
sdist = "sdist" in sys.argv
if sdist or not python_2:
    extensions.append(Extension("py2neo.packages.jsonstream.cjsonstream",
                                ["py2neo/packages/jsonstream/cjsonstream.c"]))
if sdist or python_2:
    extensions.append(Extension("py2neo.packages.jsonstream.cjsonstream_2x",
                                ["py2neo/packages/jsonstream/cjsonstream_2x.c"]))

try:
    setup(ext_modules=extensions, **package_metadata)
except:
    setup(**package_metadata)
