#!/usr/bin/env python3
import sys
min_num = sys.argv[1]
max_num = sys.argv[2]
#convert to int
int_min_num = int(min_num)
int_max_num = int(max_num)
#list comp
my_list = [i for i in range(int_min_num, int_max_num)]
print(my_list)
    
