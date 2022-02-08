#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 20:22:17 2021

@author: alivaliyev
"""

class SparseArray():

  def __init__(self, n=0):
      self._arr = n*[0]

  def __setitem__(self, j, e):
      self._arr[j] = e

  def __getitem__(self, j):
      return self._arr[j]   

#main code
sa = SparseArray(100) # All cells will have value None
sa[23] = 'C'
sa[24] = [1,2] # at this moment linked list should have only two nodes
print(sa[23])
sa[25] # should return None, but internally no node #25 should exist.
sa[100] = 1 # should raise IndexError
