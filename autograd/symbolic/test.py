#/usr/bin/env python
# -*- coding: utf-8 -*-

'''
test 
'''
from value_node import(
    Input,
    Output,
    Parameter
)

x = Input()

k = Parameter(0.)
b = Parameter(0.)

y = k * x + b