#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 21:01:21 2021

@author: alivaliyev
"""

class Maze: 
    def __init__(self,mazelist):
        
        length = len(mazelist)
        length_of_first_row = len(mazelist[0])
        Set = set([])
        count = 0
        count_s = 0
        count_e = 0
        
        if length <= 3: 
          raise Exception("InvalidMazeException")   
        if length_of_first_row <= 3: 
          raise Exception("InvalidMazeException")   

        for i in range(length):
            Set = set(mazelist[i]) | Set            
            if len(mazelist[i]) == length_of_first_row: 
              pass
            else: 
              raise Exception("InvalidMazeException")           
      
        if Set.issubset({"S","E","X","O"}) == 0: 
          raise Exception("InvalidMazeException")   
        
        for j in range(length):
            for k in range(length_of_first_row):
                count += 1
                if mazelist[j][k] == "E":
                    count_e += 1
                    position_of_e = count -1
                if mazelist[j][k] == "S":
                    count_s += 1
                    position_of_s = count -1
        if count_s != 1 or count_e != 1: 
          raise Exception("InvalidMazeException") 
        
        self._mazelist = mazelist
        self._position_of_s = position_of_s
        self._position_of_e = position_of_e
        column_index_of_s = position_of_s % length_of_first_row 
        column_index_of_e = position_of_e % length_of_first_row   
        row_index_of_s = int(position_of_s/length_of_first_row)
        row_index_of_e = int(position_of_e/length_of_first_row)
        
  
        if column_index_of_s != (length_of_first_row - 1 ) and column_index_of_s != 0: 
            if row_index_of_s != length -1 and row_index_of_s != 0:  
              raise Exception("InvalidMazeException")    
        if column_index_of_e != (length_of_first_row - 1 ) and column_index_of_e != 0 : 
            if row_index_of_e != length -1 and row_index_of_e != 0:  
              raise Exception("InvalidMazeException") 
            
    def rowdim_of_maze(self):
        return len(self._mazelist[0])

    def index_to_point(self, m, n): 
        if m <= -1 :
            raise Exception("Index cannot be negative")
        if n <= -1 :
            raise Exception("Index cannot be negative")
        return self._mazelist[m][n]
            
    def get_start(self): 
        arr = self._position_of_s
        length = len(self._mazelist[0])
        column_index_of_s =  (arr % length)
        row_index_of_s = int(arr / length)
        return (row_index_of_s, column_index_of_s)
    
    def get_exit(self): 
        arr = self._position_of_e
        length = len(self._mazelist[0])
        column_index_of_e = (arr % length)
        row_index_of_e = int(arr / length)
        return (row_index_of_e, column_index_of_e)

class Empty(Exception): 
    pass

def binary_search(arr, low, high, x): 
    if high >= low: 
        mid = (high + low) // 2
        if arr[mid] == x: 
            return True
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else: 
            return binary_search(arr, mid + 1, high, x)
    else: 
        return False

class ArrayStack: 
    
    def __init__(self):
        
        self._data = [] 

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0
    def push(self, e):
        self._data.append(e) 

    def top(self):
        if self.is_empty():
            raise Empty( "Stack is empty" )
        return self._data[-1]
           
    def pop(self):

        if self.is_empty():
            raise Empty("Stack is empty" )
        return self._data.pop() 
    
    def __str__(self):
        return self._data



class MazeSolver(Maze): 
    
    def __init__(self, path):

        self._path = path
        self._maze = Maze(MazeSolver.text_to_array(self)) 
        self._cellstack = ArrayStack()
        self._explored = []
        self._sorted_explored = []
     
    def add_sort_explored(self,Tuple):
        Sorted = self._sorted_explored
        maze = self._maze
        dim_row = Maze.rowdim_of_maze(maze)        
        a = Tuple[0]
        b = Tuple[1]
        cardinality = (a*dim_row) + b
        Sorted.append(cardinality)
        Sorted.sort()
        
    def find_in_explored_list(self,Tuple):
        Sorted = self._sorted_explored
        maze = self._maze
        dim_row = Maze.rowdim_of_maze(maze)
        cardinality_tuple = (dim_row*Tuple[0]) + Tuple[1]
        return binary_search(Sorted,0,len(Sorted)-1,cardinality_tuple)

    def text_to_array(self): 
        
        file_name = open(self._path,"r")
        return [list(l.strip().split()[0]) for l in file_name]
        file_name.close()
              
    def get_a_neighbour(self,a_tuple): 
        row = a_tuple[0]
        column = a_tuple[1]

        #left 
        try:
            left = self._maze.index_to_point(row,column-1)

            if left == "O" or left == "E":
                c = (a_tuple[0],a_tuple[1]-1)
                if MazeSolver.find_in_explored_list(self,c) == 1: 
                  pass
                else: 
                  return c
        except: 
          pass
        #right
        try: 
            right = self._maze.index_to_point(row,column+1)

            if right == "O" or right == "E":
                c = (a_tuple[0],a_tuple[1]+1)
                if MazeSolver.find_in_explored_list(self,c) == 1: 
                  pass
                else: 
                  return c
        except: 
          pass
        #up
        try:
            up = self._maze.index_to_point(row+1,column)

            if up == "O" or up == "E":
                c = (a_tuple[0]+1,a_tuple[1])
                if MazeSolver.find_in_explored_list(self,c) == 1: 
                  pass
                else: 
                  return c
        except: 
          pass
        #down         
        try:
            down = self._maze.index_to_point(row-1,column)

            if down == "O" or down == "E":
                c = (a_tuple[0]-1,a_tuple[1])
                if MazeSolver.find_in_explored_list(self,c) == 1: 
                  pass
                else: 
                  return c
        except: 
          pass               
    def solve_maze(self): 
        stack = self._cellstack
        stack.push(Maze.get_start(self._maze))
        k = 0
        while len(stack) > 0:
            a = stack.top()
            if MazeSolver.find_in_explored_list(self,a) == 0 :
                MazeSolver.add_sort_explored(self,a)
            if a == Maze.get_exit(self._maze) : 
                arr = []
                while len(stack) > 0:
                        arr += [stack.pop()]
                arr.reverse()
                k = 1
                return arr
            b = MazeSolver.get_a_neighbour(self,a)
            if b != None:
                stack.push(b)
            else: 
              stack.pop()
        if k == 0: 
          return [-1,-1]
ms = MazeSolver('Test5.txt') 
ms.solve_maze()