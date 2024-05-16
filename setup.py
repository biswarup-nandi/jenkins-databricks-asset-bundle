from setuptools import setup, find_packages

import sys
sys.path.append('./wheel')

import datetime
import cartoon

setup(
    name="cartoon",
    version=cartoon.__version__ + "+" + datetime.datetime.utcnow().strftime("%Y%m%d.%H%M%S"),
    url="https://databricks.com",
    author="soumi992mondal@gmail.com",
    description="wheel file based on DAB_E2E/wheel",
    packages=find_packages(where='./wheel'),
    package_dir={'': 'wheel'},
    entry_points={
        "packages": [
            "main=cartoon.app:main"
        ]
    },
    install_requires=[
        "setuptools"
    ],
)