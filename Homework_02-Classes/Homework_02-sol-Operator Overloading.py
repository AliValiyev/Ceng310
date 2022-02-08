#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 12:50:45 2021

@author: alivaliyev
"""
#task 1
class Vector:
    #”””Represent a vector in a multidimensional space.”””
    def __init__(self, d):
        #”””Create d-dimensional vector of zeros.””” 
        self._coords = [0]*d
        
    def __len__ (self):
        #”””Return the dimension of the vector.””” 
        return len(self._coords)
    
    def __getitem__(self, j):/Users/alivaliyev/Desktop/Metu sem 5/Ceng310/newalgo/2021Hw
       #”””Return jth coordinate of vector.””” 
        return self._coords[j]
    
    def __setitem__(self, j, val):
       #”””Set jth coordinate of vector to given value.””” 
        self._coords[j] = val
        
    def __add__(self, other):
        #”””Return sum of two vectors.”””
        if len(self) != len(other): 
            # relies on     len     method
            raise ValueError('dimensions must agree')
        result = Vector(len(self)) 
        for j in range(len(self)):
            result[j] = self[j] + other[j] 
        return result
            # start with vector of zeros
            
    def __eq__(self, other):
        #”””Return True if vector has same coordinates as other.””” 
        return self._coords == other._coords
    
    def __ne__(self, other):
        #”””Return True if vector differs from other.”””
        return not self == other 
    # rely on existing     eq     definition
    
    def __str__ (self):
        #”””Produce string representation of vector.”””
        return '<'+ str(self._coords)[1:-1] +  '>'
     # adapt list representation
    
    #task 2
    def __sub__(self, arr):
        
        if len(self) != len(arr):
             raise ValueError('Vectors must be of equal length')
             
        result_vector = Vector(len(self)) 
        
        for i in range(0,len(self)):
            result_vector[i] = self[i] - arr[i] 
            
        return result_vector
    
    #task 3
    def __neg__(self):
        
        result_vector = Vector(len(self))     
        
        for i in range(0,len(self)):
            result_vector[i] = -self[i]
            
        return result_vector
    
    #task 4
    def __radd__(self, arr):
        
        if len(self) != len(arr):
            raise ValueError('Vectors must be of equal length')
            
        result_vector = Vector(len(self))
        
        for i in range(len(result_vector)):
            result_vector[i] = self[i] + arr[i]
            
        return result_vector
    
    #task 5
    def __mul__(self, arr):
        
        result_vector = Vector(len(self))     
        
        for i in range(len(self)):
            result_vector[i] = self[i]*arr
            
            return result_vector
    
     #task 6
    def __rmul__(self, arr):
        
        result_vector = Vector(len(self)) 
        
        for i in range(len(self)):
            result_vector[i] = arr*self[i]
            
        return result_vector
    
    #task 7
    def __mul__(self, arr):
        
        if not isinstance(arr, (int, float, Vector, list)):
            raise ValueError('arr must be a number or vector')
            
        if isinstance(arr, (int, float)):
            prod = Vector(len(self))
            
            for j in range(len(self)):
                prod[j] = self[j]*arr
                
            return prod
        
        if len(self) != len(arr):
            raise ValueError('Vectors must be of equal length')
            
        else:
            dotprod = 0
            
            for i in range(len(self)):
                dotprod += self[i] * arr[i]
                
            return dotprod
    #task 8
    def __init__(self, arr):
        
        if isinstance(arr, int):
            self._coords = [0] * arr
            
        else:                                  
            try:
                self._coords = [i for i in arr]
                
            except TypeError:
                raise TypeError('invalid parameter')
   