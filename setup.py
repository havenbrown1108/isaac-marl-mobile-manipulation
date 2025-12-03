"""Installation script for the 'omniisaacgymenvs' python package."""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

from setuptools import setup, find_packages

import os

# Minimum dependencies required prior to installation
INSTALL_REQUIRES = [
    "hydra-core",
    "omegaconf",
    "protobuf>=3.20.3",
    "antlr4-python3-runtime==4.9.3",
    "redis==3.5.3", # needed by Ray on Windows
    "rl-games==1.5.2",
    "numpy",
    "gym",
    "pyyaml",
    "tensorboard"
]

# Installation operation
setup(
    name="omniisaacgymenvs",
    author="NVIDIA",
    version="2.0.0",
    description="RL environments for robot learning in NVIDIA Isaac Sim.",
    keywords=["robotics", "rl"],
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    packages=find_packages("."),
    classifiers=["Natural Language :: English", "Programming Language :: Python :: 3.7, 3.8"],
    zip_safe=False,
)

# EOF
