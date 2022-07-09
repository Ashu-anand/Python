'''
O (n^2)
                    Selection Sort

'''
class Selection_Sort:
    def select_sort(self,num_list):
        for idx in range(len(num_list)-1):
            val=num_list[idx]
            for jdx in range(idx+1,len(num_list)):
                if val>num_list[jdx]:
                    val,num_list[jdx]=num_list[jdx],val
            num_list[idx]=val
        return num_list


n=[5,4,1,6,9,2,7,3,8]
n=[9,5,1,4,3]

s=Selection_Sort()
print(s.select_sort(n))