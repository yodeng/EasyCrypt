import os
import imp
import sysconfig

from setuptools import setup
from setuptools.extension import Extension


def get_versin():
    m = imp.load_module(
        "vserion", *imp.find_module("version", ["EasyCrypt"]))
    return m.__version__


def getdes():
    des = ""
    if os.path.isfile(os.path.join(os.getcwd(), "README.md")):
        with open(os.path.join(os.getcwd(), "README.md")) as fi:
            des = fi.read()
    return des


def writeExtension(ext):
    extensions = []
    for f in ext:
        e = Extension("EasyCrypt." + os.path.splitext(os.path.basename(f))[0],
                      [f, ], extra_compile_args=["-O3", ],)
        e.cython_directives = {
            'language_level': sysconfig._PY_VERSION_SHORT_NO_DOT[0]}
        extensions.append(e)
    return extensions


setup(
    name="EasyCrypt",
    version=get_versin(),
    packages=["EasyCrypt"],
    author="Deng Yong",
    author_email="yodeng@tju.edu.cn",
    url="https://github.com/yodeng/EasyCrypt",
    license="BSD",
    install_requires=["pycryptodome", "Cython"],
    ext_modules=writeExtension(
        ["src/decrypt.py", "src/encrypt.py", "src/main.py", "src/utils.py"]),
    long_description=getdes(),
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            'EasyCrypt = EasyCrypt.main:main',
        ]
    }
)
