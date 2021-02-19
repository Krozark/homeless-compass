import os

import setuptools

from homeless_compas import __version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setuptools.setup(
    name='homeless-compass',
    version=__version__,
    description='A GPS App',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    license="BSD 2-Clause",
    author='Maxime Barbier',
    author_email='maxime.barbier1991+homelesscompass@gmail.com',
    url="https://github.com/Krozark/homeless-compass",
    packages=setuptools.find_packages(),
    classifiers=[
      "Programming Language :: Python",
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3.7",
      "Programming Language :: Python :: 3.8",
      "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
      "Operating System :: OS Independent",
    ],
    install_requires=[
        "plyer",
        "kivy[base]",
    ],
    extras_require={
        "dev": [
            "buildozer==1.2.0"
        ],
        "android": [
            "pyjnius"
        ]
    },
    python_requires='>=3.7, <3.9, <4',
)
