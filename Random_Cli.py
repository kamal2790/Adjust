# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
Description : Print the numbers from 1 to 10 in random orders.
"""


import random

list =  [x for x in range(10)]
random.shuffle(list)
print(list)