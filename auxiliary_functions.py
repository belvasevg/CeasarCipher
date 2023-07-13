# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 17:10:41 2023

@author: belva
"""
#вспомогательная функция, переводящая заглавные буквы к прописным
def help_size(l : list) -> list: 
    for i in range(len(l)):
        l[i]=l[i].lower()
    return l
#РУССКИЕ БУКВЫ В ВЕРХНЕМ РЕГИСТРЕ
def rus_up() -> list: 
    up=["А","Б","В","Г","Д","Е","Ж","З","И","Й","К","Л","М","Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ","Ъ","Ы","Ь","Э","Ю","Я"]
    return up
#русские буквы в нижнем регистре
def rus_low() -> list: 
    listik=rus_up()
    help_size(listik)
    return listik
#АНГЛИЙСКИЕ БУКВЫ В ВЕРХНЕМ РЕГИСТРЕ
def eng_up() -> list: 
    up=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    return up
#англиские буквы в нижнем регистре
def eng_low() -> list: 
    listik=eng_up()
    help_size(listik)
    return listik

#print(rus_low(),eng_low(),sep='\n\n') #тест перевода в нижний регистр