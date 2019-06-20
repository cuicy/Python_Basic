#!/usr/local/bin/python3
# _*_ coding=utf-8 _*_
# 用于Python_Basic学习！

import random

result1 = random.randint(1,255)
result2 = random.randint(1,255)
result3 = random.randint(1,255)
result4 = random.randint(1,255)

rand_ip = str(result1)+'.'+str(result2)+'.'+str(result3)+'.'+str(result4)
print('随机产生的IP地址为:'+ rand_ip)

