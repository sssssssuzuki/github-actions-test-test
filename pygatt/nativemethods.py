'''
File: nativemethods.py
Project: pygatt
Created Date: 20/02/2021
Author: Shun Suzuki
-----
Last Modified: 20/02/2021
Modified By: Shun Suzuki (suzuki@hapis.k.u-tokyo.ac.jp)
-----
Copyright (c) 2021 Hapis Lab. All rights reserved.

'''

import threading
import ctypes


class Singleton(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Nativemethods(metaclass=Singleton):
    dll = None

    def init_dll(self, dlllocation):
        self.dll = ctypes.CDLL(dlllocation)
        # self.dll.C_SAYHELLO.argtypes = None
        # self.dll.C_SAYHELLO.restypes = [None]
