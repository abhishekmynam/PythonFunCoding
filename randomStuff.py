#!/bin/python3

import sys
import re


s = input().strip()

s1 = len(re.findall(r'[A-Z]',s))+1
print(s1)