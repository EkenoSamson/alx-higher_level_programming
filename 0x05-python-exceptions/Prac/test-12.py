#!/usr/bin/python3
# os._exit(0) versus finally block

import os
try:
    print("try")
    os._exit(0)
except:
    print("except")
finally:
    print("finally")
