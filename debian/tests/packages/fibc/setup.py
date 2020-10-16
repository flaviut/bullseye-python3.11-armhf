#!/usr/bin/env python

from setuptools import setup, Extension

setup(
    name='fibc',
    version='42.0.0',
    description='C Fibonacci',
    ext_modules=[Extension(
        'fibc',
        sources=['fibc.c'],
    )],
    zip_safe=False,
)
