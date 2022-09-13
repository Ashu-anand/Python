'''
O(N)
                Linear Search
'''
class Linear_Search:
    def linear_search(self,num_list,num_to_be_found):
        for idx,val in enumerate(num_list):
            if val==num_to_be_found:
                return idx
        return -1
    
n_list=[1,5,2,9,4,8,3,7]
n_num=8
s=Linear_Search()
print(s.linear_search(n_list,n_num))