#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    num = bin(n)
    
    maxim = 0
    current = 0
    
    for i in num:
        if i == '1':
            current += 1
        else:
            maxim = max(maxim,current)
            current = 0
    
    print(max(maxim,current))
    
    
    
    
