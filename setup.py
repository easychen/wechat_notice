#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project: wechat-notice
Creator: DoubleThunder
Create time: 2019-10-06 00:33
Introduction:
"""


import io
import os
import re
from setuptools import find_packages, setup, Command


# What packages are required for this module to be executed?
REQUIRED = [
    'requests', 'yagmail'
]

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

current_dir = os.path.abspath(os.path.dirname(__file__))

def get_meta():
    meta_re = re.compile(r"(?P<name>__\w+__) = '(?P<value>[^']+)'")
    meta_d = {}
    with open(os.path.join(current_dir, 'wechat_notice','__init__.py'),
              encoding='utf8') as fp:
        for match in meta_re.finditer(fp.read()):
            meta_d[match.group('name')] = match.group('value')
    return meta_d

try:
    with io.open(os.path.join(current_dir, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = '随时随地发消息到微信/工具.'

packages = [
    'wechat_notice',
]

meta_d = get_meta()
# Where the magic happens:
setup(
    name=meta_d['__title__'],
    version=meta_d['__version__'],
    description='发消息通知给微信/工具.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=meta_d['__author__'],
    author_email='sfyc23@gmail.com',
    license=meta_d['__license__'],
    python_requires='>=3.6.0',
    url='https://github.com/sfyc23/wechat-notice',
    # packages=find_packages(exclude=('tests',)),
    packages=packages,
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,

    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    keywords='wechat, 微信, notice, 通知',

)




