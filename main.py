# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 17:09:51 2023

@author: belva
"""

import unit_test

message = input("Введите сообщение: ")        
shift = int(input("Введите шаг: "))
choise = input("Введите значение для шифровки(ш(rus)/e(eng))/для дешифровки(д(rus)/d(eng)):\n")

#тестирование работы программы
u1 = unit_test.test(message, shift, choise)
print(u1.testing(message,shift,choise))    