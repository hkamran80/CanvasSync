#!/usr/bin/env python
from setuptools import setup

from CanvasSync._version import __version__

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('CHANGES.txt') as readme_file:
    changes = readme_file.read()

with open("requirements.txt") as req_file:
    requirements = list(filter(None, req_file.read().split("\n")))


setup(
    name='CanvasSync',
    version=__version__,
    description='Synchronizes modules, assignments and files from a '
                'Canvas server to a local folder',
    long_description=readme + "\n\n" + changes,
    author='Mathias Perslev',
    author_email='mathias@perslev.com',
    url='https://github.com/perslev/CanvasSync',
    license="LICENSE.txt",
    package_dir={'CanvasSync': 'CanvasSync'},
    entry_points={
        'console_scripts': [
            'canvas=CanvasSync.__main__:main',
        ],
    },
    install_requires=requirements,
    classifiers=['Development Status :: 3 - Alpha',
                'Environment :: Console',
                'Operating System :: MacOS :: MacOS X',
                'Operating System :: POSIX',
                'Programming Language :: Python',
                'License :: OSI Approved :: MIT License']
)
