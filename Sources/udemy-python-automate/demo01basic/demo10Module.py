import sys # import sys module
print(sys.maxsize) # print sys module's maxsize

import os, math # import multiple module in a line
print(math.pi)

from random import * # import * (Everything)
print(randint(10, 20)) # may use module's function without dot operator

import random as rnd # import and assign a name to the module
print(rnd.randint(10, 20)) # use by assigned module name

sys.exit()
print('Goodbye') # Won't execute