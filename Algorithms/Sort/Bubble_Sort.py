'''
O (n^2)
                    Bubble Sort   
'''
class Sorting:
    def Bubble_sort(num_list):
        for idx in range(len(num_list)):
            for jdx in range(len(num_list)-1):
                if num_list[jdx]>num_list[jdx+1]:
                    num_list[jdx],num_list[jdx+1]=num_list[jdx+1],num_list[jdx]
        return num_list


n=[5,4,1,6,9,2,7,3,8]

print(Sorting.Bubble_sort(n))