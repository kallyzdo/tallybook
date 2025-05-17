# setup.py
from setuptools import setup, find_packages

setup(
    name='tallybook',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'tb=tallybook.main:main',  # This makes the `tb` command available
        ],
    },
    install_requires=[],
)
