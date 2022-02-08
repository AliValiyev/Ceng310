import random
def check_the_data_type_of_array(arr):
    type_of_elem = set()  
    for i in range(len(arr)):
        type_of_elem.add(type(arr[i]))
    if len(type_of_elem) != 1:
      elem = array()
      while len(type_of_elem) > 0:
        Sample_Type = type_of_elem.pop()
        for l in random.sample(range(0,len(arr)), len(arr)):
          if type(arr[l]) == Sample_Type: 
            elem.append(arr[l])
            break
      for m in range(len(elem)):
        for n in range(m,len(elem)):
          try:
            elem[m] == elem[n]
            elem[m] > elem[n]
            elem[m] < elem[n]
          except:
            return [elem[l],elem[n]]
      return 1
    else:
       return 1
   
def insertion_sort(A):
    for i in range(1, len(A)): 
        cur = A[i] 
        j = i
        while j > 0 and A[j-1] > cur: 
            A[j] = A[j-1]
            j -= 1
            A[j] = cur 
def merge(S1, S2, S):
    i = j = 0
    while i+j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i] 
            i += 1
        else:
            S[i+j] = S2[j] 
            j += 1  
def merge_sort(S):
    n = len(S)
    if n < 2:
        return 
    mid = n //2
    S1 = S[0:mid] 
    S2 = S[mid:n] 
    merge_sort(S1)
    merge_sort(S2) 
    merge(S1, S2, S)
    
#main
def smart_sort(arr, max_of_arr = 50):
    if len(arr)<2:
      return arr
    data_type_of_elem = type(arr) 
    if data_type_of_elem != array:
        arr_type = array()
        try:
            for i in range(len(arr)):
                arr_type.append(arr[i])
        except:
            raise TypeError("Error")
        smart_sort(arr_type)
        for i in range(len(arr_type)):
            try:
                if arr_type[i] != arr[i]:
                    arr.remove(arr[i])
                    arr.insert(i,arr_type[i])
            except:
                raise TypeError("Error")
    else:
        rez = check_the_data_type_of_array(arr) 
        if rez == False: 
            ob = str()
            print(rez)
            for i in range(len(rez)-1):
                ob += str(rez[i]) + ", "
            ob += str(rez[-1])
            raise TypeError("Error, not comparable:" + ob)
        else: 
            if len(arr) < max_of_arr: 
              insertion_sort(arr)
            else: 
              merge_sort(arr)  
#main
from array import array
a = array('i', [1, 3, 4, 2, 1, 6, 13, 2])
smart_sort(a)
print(a) #array('i', [1, 1, 2, 2, 3, 4, 6, 13])


