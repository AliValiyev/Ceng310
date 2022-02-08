from collections.abc import MutableMapping
from random import randrange

class MapBase(MutableMapping):
    class _Item:
        __slots__ = '_key', '_value'
        def __init__(self, key, value):
            self._key = key
            self._value = value
        def __eq__(self, other):
            return self._key == other._key  
        def __ne__(self, other):
            return not self == other
        def __lt__(self, other):
            return self._key < other._key

class HashMapBase(MapBase):
    def __init__(self, cap=11, p=109345121):
        self._table = cap * [None]
        self._n = 0                        
        self._prime = p                     
        self._scale = 1 + randrange(p-1)    
        self._shift = randrange(p)          
    def _hash_function(self, k):
        return (hash(k)*self._scale + self._shift) % self._prime % len(self._table)
    def __len__(self):
        return self._n
    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j,k)     
    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j,k,v)             
        if self._n > len(self._table) // 2:     
            self._resize(2*len(self._table) - 1)
    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j,k)               
        self._n -= 1
    def _resize(self, c):                       
        old = list(self.items())            
        self._table = c * [None]               
        self._n = 0                             
        for (k,v) in old:
            self[k] = v

class ProbeHashMap(HashMapBase):
    _AVAIL = object()
    def _is_available(self, j):
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL
    def _find_slot(self, j, k):
        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j                  
                if self._table[j] is None:
                    return (False, firstAvail)      
            elif k == self._table[j]._key:
                return (True, j)                    
            j = (j+1) % len(self._table)            
    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k)) 
        return self._table[s]._value
    def _bucket_setitem(self, j, k, v):
        found , s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k,v)        
            self._n += 1                           
        else:
            self._table[s]._value = v               
    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
             raise KeyError('Key Error: ' + repr(k))
        self._table[s] == ProbeHashMap._AVAIL       
    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key

class SpellChecker:
    def __init__(self, minim = 3, maxim = 3, _rwf = "google-10000-english.txt"):
        self._letter = "abcdefghijklmnopqrstuvwxyz"
        self._pm = [".",",",":",";","-","*","%","!","?","'","+","/","\"","(",")","[","]"]
        self._phm = ProbeHashMap()
        self._maxim = maxim
        self._minim = minim
        self._rwf = _rwf
    def rep_ch(self, text):
        arr = []
        for i in range(len(text)):
            for j in range(len(self._letter)):
                ans = text[0:i] + self._letter[j] + text[i+1:len(text)]
                arr.append(ans)
        return arr
    def get_ref(self):
        file_ = open(self._rwf, "r")
        nl = file_.readline()
        while nl != "":
            nl = nl.strip("\n")
            nl = nl.strip()
            if len(nl) >= self._minim :
                self._phm[nl] = None
            nl = file_.readline()
        return self._phm
    def ord_ch(self, text):
        arr = []
        for i in range(len(text)-1):
            ans = text[0:i] + text[i+1] + text[i] + text[i+2:len(text)]
            arr.append(ans)
        return arr
    def add_ch(self, text):
        arr = []
        for i in range(len(text)+1):
            for j in range(len(self._letter)):
                ans = text[0:i] + self._letter[j] + text[i:len(text)]
                arr.append(ans)
        return arr
    def shape_str(self, text):
        if text.isdigit() == 1 or text.isdecimal() == 1:
            self._flag_0 = 0
            return []
        if text.isalpha() == 1 :
            text = text.lower()
            return [text]
        else:
            for i in range(len(self._pm)):
                text = text.strip(str(self._pm[i]))
                if text.isalpha() == 1 :
                    text = text.lower()
                    return [text]
            array = []
            for i in range(len(self._pm)):
                arrayoftext = text.split(str(self._pm[i]))
                for j in range(len(arrayoftext)):
                    if arrayoftext[j].isalpha() == 1:
                        arrayoftext[j] = arrayoftext[j].lower()
                        array.append(arrayoftext[j])
            if len(array) == 0 : 
                if text.isidentifier() == 0: self._flag_0 = 2
                else: self._flag_0 = 3
            return array        
    def rem_ch(self, text):
        arr = []
        for i in range(len(text)):
            ans = text[0:i] + text[i+1:len(text)]
            arr.append(ans)
        return arr      
    def check(self, inpfile):
        self.get_ref()
        first_file = open(inpfile, "r")
        second_file = open("Solution.txt","w")
        nl = first_file.readline()
        while nl != "":
            nl = nl.strip("\n")
            nl = nl.strip()
            nl = nl.split()
            for i in range(len(nl)):
                word = nl[i]
                list_of_words = self.shape_str(word)                  
                for l in range(len(list_of_words)):
                    flag = 0
                    if len(list_of_words) >= 2:
                      flag = 1
                    if len(list_of_words[l]) + 1 < self._minim:
                            var = word + " --> " + " No Recommendation" + "\n"
                            second_file.write(var)
                    elif list_of_words[l] in self._phm :
                        if flag == 0:
                            var = word + " --> " + "OK" + "\n"
                            second_file.write(var)
                        else:
                            var = word + " --> " + "OK" + str(l+1) + "\n"
                            second_file.write(var)
                    else:
                        k = 0
                        max_k = self._maxim
                        rec_list = []
                        if k<max_k:
                            inser_list = self.add_ch(list_of_words[l])
                            for m in range(len(inser_list)):
                                if inser_list[m] in self._phm and inser_list[m] not in rec_list :
                                    rec_list.append(inser_list[m])
                                    k += 1
                                if k == max_k: 
                                  break
                            rem_list = self.rem_ch(list_of_words[l])
                            for n in range(len(rem_list)):
                                if rem_list[n] in self._phm and rem_list[n] not in rec_list :
                                    rec_list.append(rem_list[n])
                                    k += 1
                                if k == max_k: 
                                  break
                            adj_reor = self.ord_ch(list_of_words[l])
                            for p in range(len(adj_reor)):
                                if adj_reor[p] in self._phm and adj_reor[p] not in rec_list :
                                    rec_list.append(adj_reor[p])
                                    k += 1
                                if k == max_k: 
                                  break
                            replaced = self.rep_ch(list_of_words[l])
                            for t in range(len(replaced)):
                                if replaced[t] in self._phm and replaced[t] not in rec_list :
                                    rec_list.append(replaced[t])
                                    k += 1
                                if k == max_k: 
                                  break 
                        if len(rec_list) != 0:
                            rec = ""
                            for n in range(len(rec_list)-1):
                                rec += rec_list[n] + ", "
                            rec += rec_list[-1]
                            if flag == 0:
                                var = word + " --> " + rec + "\n"
                                second_file.write(var)
                            else:
                                var = word + " --> " + rec  +  str(l+1) + "\n"
                                second_file.write(var)
                        else:
                            if flag == 0:
                                var = word + " --> " + "No Recommendation" + "\n"
                                second_file.write(var)
                            else:
                                 var = word + " --> " + "No Recommendation" + str(l+1) + "\n"
                                 second_file.write(var)
                if len(list_of_words) == 0:
                    if self._flag_0 == 0: 
                        var = word + " --> " + "No Recommendation" + "\n"
                        second_file.write(var)
                    elif self._flag_0 == 1:
                        var = word + " --> " + "No Recommendation" + "\n"
                        second_file.write(var)
                    elif self._flag_0 == 2:
                        var = word + " --> " + "No Recommendation" + "\n"
                        second_file.write(var)                        
                    elif self._flag_0 == 3:
                        var = word + " --> " + "No Recommendation" + "\n"
                        second_file.write(var)         
            nl = first_file.readline()
        first_file.close()
        second_file.close()
        
        
        
Test = SpellChecker()
Test.check("Input.txt")

