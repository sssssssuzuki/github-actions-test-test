'''
File: setup.py
Project: github-actions-test-test
Created Date: 20/02/2021
Author: Shun Suzuki
-----
Last Modified: 20/02/2021
Modified By: Shun Suzuki (suzuki@hapis.k.u-tokyo.ac.jp)
-----
Copyright (c) 2021 Hapis Lab. All rights reserved.

'''

import setuptools


def _get_version():
    with open('README.md', 'r') as f:
        for line in f.readlines():
            if line.startswith('version: '):
                return line.replace('version: ', '').strip()
    raise LookupError('version info is not found in README.md')


def _set_package_version(version):
    init_py = ''
    with open('pygatt/__init__.py', 'r') as f:
        for line in f.readlines():
            if line.startswith('__version__'):
                line = '__version__ = \'' + version.strip() + '\'\n'
            init_py = init_py + line

    with open('pygatt/__init__.py', 'w') as f:
        f.write(init_py)


with open('README.md', 'r') as fh:
    long_description = fh.read()

_set_package_version(_get_version())

setuptools.setup(
    name='pygatt',
    version=_get_version(),
    author='Shun Suzuki',
    author_email='suzuki@hapis.k.u-tokyo.ac.jp',
    description='Github action test test',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['requests'],
    url='https://github.com/sssssssuzuki/github-actions-test-test',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows'
        'Operating System :: POSIX',
        'Operating System :: MacOS'
    ],
    platforms=["Windows", "Linux", "Mac OS-X"],
    include_package_data=True,
    package_dir={'pygatt': 'pygatt'},
    packages=['pygatt'],
    python_requires='>=3.6',
)
