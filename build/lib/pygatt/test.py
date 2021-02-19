'''
File: test.py
Project: pygatt
Created Date: 20/02/2021
Author: Shun Suzuki
-----
Last Modified: 20/02/2021
Modified By: Shun Suzuki (suzuki@hapis.k.u-tokyo.ac.jp)
-----
Copyright (c) 2021 Hapis Lab. All rights reserved.

'''

from .nativemethods import Nativemethods

NATIVE_METHODDS = Nativemethods()


def sayhello():
    NATIVE_METHODDS.dll.C_SAYHELLO()
