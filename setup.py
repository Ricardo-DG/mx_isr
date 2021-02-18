#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Ricardo Dominguez"
__version__ = "0.0.1"
__maintainer__ = "Ricardo Dominguez"
__email__ = "ricardo.dominguezguevara@gmail.com"
__status__ = "Development"

# -- python import
from setuptools import setup

setup(
    name='mx_isr',
    version='0.0.1',
    description="""Support tool for easy calculation of taxes (Mexico) with python. Herramienta de soporte para cálculo
                   fácil de impuesto sobre la renta ISR (México) con python.""",
    url='git@github.com:Ricardo-DG/mx_isr.git',
    author='Ricardo Dominguez',
    author_email='ricardo.dominguezguevara@gmail.com',
    license='unlicense',
    packages=['mx_isr'],
    zip_safe=False
)