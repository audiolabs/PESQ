# 2019-May
# github.com/ludlows
# Python Wrapper for PESQ Score (narrowband and wideband)
from setuptools import find_packages
from setuptools import setup, Extension

with open("README.md", "r") as fh:
    long_description = fh.read()


class CyPesqExtension(Extension):
    def __init__(self, *args, **kwargs):
        self._include = []
        super().__init__(*args, **kwargs)

    @property
    def include_dirs(self):
        import numpy
        return self._include + [numpy.get_include()]

    @include_dirs.setter
    def include_dirs(self, dirs):
        self._include = dirs


extensions = [
    CyPesqExtension(
        "cypesq",
        ["pesqc2/cypesq.pyx", "pesqc2/dsp.c", "pesqc2/pesqdsp.c", "pesqc2/pesqmod.c"],
        include_dirs=['pesqc2'],
        language="c")
]
setup(
    name="pesqc2",
    version="0.0.4",
    author="mtorcoli, ModarHalimeh, ludlows",
    description="Python Wrapper for PESQ Score (narrow band and wide band) - including Corrigendum 2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/audiolabs/PESQ",
    packages=find_packages(),
    package_data={'pesqc2': ["*.pyx", "*.h", "dsp.c", "pesqdsp.c", "pesqmod.c"]},
    ext_package='pesqc2',
    ext_modules=extensions,
    setup_requires=['setuptools>=18.0', 'cython', 'numpy<2.0'],
    install_requires=['numpy<2.0'],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
