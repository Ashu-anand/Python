'''
O(log n)
                Jump Search
'''
from math import sqrt

from numpy import block


class Jump_Search:
    def jump_search(self,num_list,num_to_be_found):
        block_size=int(sqrt(len(num_list)))
        for idx in range(0,len(num_list),block_size):
            if num_list[idx]==num_to_be_found:
                return idx
            if num_list[idx]>num_to_be_found:
                break
        if idx+block_size>=len(num_list):
            end=len(num_list)
        else:
            end=idx
        for i in range(idx-block_size+1,end):
            if num_list[i]==num_to_be_found:
                return i
        return -1
        
    
n_list=[1,2,3,11]
n_num=10
s=Jump_Search()
print(s.jump_search(n_list,n_num))