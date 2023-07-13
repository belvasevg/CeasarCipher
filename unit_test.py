# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 12:24:28 2023

@author: belva
"""
class test:
    def __init__(self,m : str, s : int, c : str):
        self.message = m
        self.shift = s
        self.choise = c
    
    def testing(self, m,s,c) -> str:
        import encrypt
        import decrypt
        if c == "ш" or c == "e":
            return encrypt.encrypt(m, s)
            
        elif c == "д" or c == "d":
            return decrypt.decrypt(m, s)