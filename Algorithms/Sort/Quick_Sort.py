'''
O (nlogn)
                    Quick Sort

'''
class Quick_Sort:
    def helper(self,array_list,start,end):
        left=start+1
        right=end
        while True:
            while left<=right and array_list[start] <= array_list[right]:
                right-=1
            while left<=right and array_list[start]>=array_list[left]:
                left+=1
            if left<=right:
                array_list[left],array_list[right]=array_list[right],array_list[left]
            else:
                break
        array_list[start],array_list[right]=array_list[right],array_list[start]
        return right

    def quick_sort(self,num_list,start,end ):
        if start >= end:
            return
        pivot = self.helper(num_list, start, end)
        self.quick_sort(num_list, start, pivot-1)
        self.quick_sort(num_list, pivot+1, end)
        return num_list



n=[29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]

s=Quick_Sort()
print(s.quick_sort(n,0,len(n)-1))