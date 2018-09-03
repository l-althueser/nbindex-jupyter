# encoding: utf-8
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='nbindex-jupyter',
    version='0.2.25',
    packages=['nbindex'],
    url='https://github.com/l-althueser/nbindex-jupyter',
    license='BSD 3-Clause License',
    author='Lutz Althüser',
    author_email='coding@l-althueser.de',
    description='Javascript based Jupyter Notebook additions (Table of Content, hide code, Figure numbers, ...)',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: IPython",
        "Framework :: Jupyter",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
