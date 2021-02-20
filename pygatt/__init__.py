'''
File: __init__.py
Project: pygatt
Created Date: 20/02/2021
Author: Shun Suzuki
-----
Last Modified: 20/02/2021
Modified By: Shun Suzuki (suzuki@hapis.k.u-tokyo.ac.jp)
-----
Copyright (c) 2021 Hapis Lab. All rights reserved.

'''

import os.path
import platform
import requests
import glob
import shutil
import zipfile
import tarfile

from pygatt.test import sayhello
from pygatt.nativemethods import Nativemethods

PLATFORM = platform.system()
TARGET_OS = ''
ARCH = ''
PREFIX = ''
BIN_EXT = ''
ARCHIVE_EXT = ''
if PLATFORM == 'Windows':
    BIN_EXT = '.dll'
    ARCHIVE_EXT = '.zip'
    TARGET_OS = 'win'
    ARCH = 'x64' if platform.machine().endswith('64') else 'x86'
elif PLATFORM == 'Darwin':
    PREFIX = 'lib'
    BIN_EXT = '.dylib'
    ARCHIVE_EXT = '.tar.gz'
    TARGET_OS = 'macos'
    ARCH = 'x64'
elif PLATFORM == 'Linux':
    PREFIX = 'lib'
    BIN_EXT = '.so'
    ARCHIVE_EXT = '.tar.gz'
    TARGET_OS = 'linux'
    if platform.machine().startswith('aarch64'):
        ARCH = 'arm64'
    elif platform.machine().startswith('arm64'):
        ARCH = 'arm64'
    elif platform.machine().startswith('arm'):
        ARCH = 'arm32'
    elif platform.machine().endswith('64'):
        ARCH = 'x64'
    else:
        raise ImportError('Cannot identify CPU architecture')
else:
    raise ImportError('Not supported OS')

__all__ = ['sayhello']

__version__ = '0.2.2'
LIB_PATH = os.path.join(os.path.dirname(__file__), 'bin', f'{PREFIX}sayhellocapi_{__version__}{BIN_EXT}')


def download_bin(version):
    _AssetsBaseURL = 'https://github.com/sssssssuzuki/github-actions-test/releases/download/'
    _Version = 'v' + '.'.join(version.split('.')[0:3])
    _Version = _Version.strip()

    url = f'{_AssetsBaseURL}{_Version}/sayhello-{_Version}-{TARGET_OS}-{ARCH}{ARCHIVE_EXT}'

    module_path = os.path.dirname(__file__)
    tmp_archive_path = os.path.join(module_path, 'tmp' + ARCHIVE_EXT)

    res = requests.get(url, stream=True)
    with open(tmp_archive_path, 'wb') as fp:
        shutil.copyfileobj(res.raw, fp)

    if ARCHIVE_EXT == '.zip':
        with zipfile.ZipFile(tmp_archive_path) as f:
            for info in f.infolist():
                if info.filename.startswith('bin') and info.filename.endswith(BIN_EXT):
                    f.extract(info, module_path)
    elif ARCHIVE_EXT == '.tar.gz':
        with tarfile.open(tmp_archive_path) as f:
            libraries = []
            for i in f.getmembers():
                if i.name.startswith('bin') and i.name.endswith(BIN_EXT):
                    libraries.append(i)
            f.extractall(path=module_path, members=libraries)

    os.remove(tmp_archive_path)


def load_latest_binary(version):
    version = '.'.join(version.split('.')[0:3])
    version = version.strip()
    if os.path.exists(LIB_PATH):
        return

    print(f'Cannot find  {LIB_PATH}.')
    print('Downloading latest binaries...')

    for file in glob.glob(os.path.join(os.path.dirname(__file__), 'bin', '*')):
        if file.endswith(BIN_EXT):
            # try:
            os.remove(file)
            # catch Exce:

    download_bin(version)

    for file in glob.glob(os.path.join(os.path.dirname(__file__), 'bin', '*')):
        if file.endswith(BIN_EXT):
            os.rename(file, file.replace(BIN_EXT, f'_{version}{BIN_EXT}'))
    print('Done')


load_latest_binary(__version__)
Nativemethods().init_dll(LIB_PATH)
