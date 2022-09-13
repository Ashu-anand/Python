'''
O(log n)
                Binary_Search
'''
class Binary_Search:
    def binary_search(self,num_list,num_to_be_found):
        left=0
        right=len(num_list)-1
        while left<=right:
            mid=(left+right)//2
            if num_list[mid]==num_to_be_found:
                return mid
            elif num_list[mid]>num_to_be_found:
                right=mid-1
            else:
                left=mid+1
        return -1
    
n_list=[1,2,3,4,5,6,7,8,9,10]
n_num=11
s=Binary_Search()
print(s.binary_search(n_list,n_num))