#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 18:27:58 2022

@author: alivaliyev
"""
import time
from timeit import timeit
import random
import numpy as np
import pandas as pd
import matplotlib.pylab as plt

class PriorityQueueBase:
    class _Item:
        def __init__(self, k, v):
            self._key = k
            self._value = v
        def __lt__(self,other):
            return self._key < other._key
    def is_empty(self): 
        return len(self) == 0

class Empty:
    pass

class HeapPriorityQueue(PriorityQueueBase):   

    def _parent(self, j):
        return (j-1) // 2
    
    def _left(self, j):
        return 2*j+1
    
    def _right(self, j):
        return 2*j+2
    
    def _has_left(self, j):
        return self._left(j) < len(self._data)    
    
    def _has_right(self, j):
        return self._right(j) < len(self._data)    
    
    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]
    
    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)   
    
    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left    
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child) 

    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def add(self, key, value):
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)    
    
    def min(self):
        if self.is_empty(): raise Empty("Priority queue is empty.")
        item = self._data[0]
        return (item._key, item._value)
    
    def remove_min(self):
        if self.is_empty(): raise Empty("Priority queue is empty.")
        self._swap(0, len(self._data)-1)   
        item = self._data.pop()    
        self._downheap(0)   
        return (item._key, item._value)

def test_heap(n):
    _heap = HeapPriorityQueue()
    measures = []
    k = 0
    pts = random.sample(range(0,(10**3)*n), n)
    for i in range(n):
        key = pts[i]
        _heap.add(key,"identical elem")
    while len(_heap) != 0:
        sec = timeit(lambda: _heap.remove_min(), number = 1)
        nanosec = (10**9) * sec
        k += nanosec
        measures.append(nanosec)
    average = k/n
    maxim = max(measures)
    return (average, maxim)

def report_results():
    results_list = []
    for i in range(1000,100001,1000): 
        Data = test_heap(i)
        results_list.append((i, Data[0], Data[1]))
    df = pd.DataFrame(results_list , columns =['n', 'avg', 'max'])
    line_1 , = plt.plot(df['n'], df['avg'], color='red', label = "Average time")
    line_2 , = plt.plot(df['n'], df['max'], color='blue', label = "Maximum time")
    plt.title("Heap Performance Experiment", fontsize=15)
    plt.xlabel("Size of Heap Priority Queue", fontsize=10)
    plt.ylabel("Time Cost of remove_min() (nanoseconds)", fontsize=10)
    plt.grid(True)
    plt.legend(handles=[line_1, line_2])
    plt.savefig("Graph.pdf")
report_results()
        