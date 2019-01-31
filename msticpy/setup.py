# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""Setup script for msticpy."""

import setuptools

from ._version import VERSION as __version__

# pylint: disable=locally-disabled, C0103
with open("README.md", "r") as fh:
    long_description = fh.read()
# pylint: enable=locally-disabled, C0103

setuptools.setup(
    name="msticpy",
    version=__version__,
    author="Ian Hellen",
    author_email="ianhelle@microsoft.com",
    description="MSTIC Security Tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://https://github.com/ianhelle/msyticpy",
    python_requires='>=3.6',
    packages=setuptools.find_packages(exclude=['notebookext', 'notebooks', 'miscnotebooks']),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require={
        "matplotlib": ["matplotlib>=3.0.2"],
        "bokeh": ["bokeh>=1.0.2"],
        "setuptools": ["setuptools>=40.6.3"],
        "attrs": ["attrs>=18.2.0"],
        "pandas": ["pandas>=0.22.0"],
        "requests": ["requests>=2.21.0"],
        "networkx": ["networkx>=2.2"],
        "numpy": ["numpy>=1.15.4"],
        "urllib3": ["urllib3>=1.24.1"],
        "ipywidgets": ["ipywidgets>=7.4.2"],
        "ipython": ["ipython>=7.2.0"],
        "Kqlmagic": ["Kqlmagic>=0.1.90"],
        "attr": ["attr>=0.3.1"],
        "scikit_learn": ["scikit_learn>=0.20.2"],
        "maxminddb_geolite2": ["maxminddb_geolite2>=2018.0"],
        "typing": ["typing>=3.6.6"]
    }
)
