#!/bin/python
# -*- coding: cp936 -*-
#pass、exec、eval
if(1 == 1):
    pass

exec('print(x)', {"x": "abc"})
print(eval('x*2', {"x": 5}))