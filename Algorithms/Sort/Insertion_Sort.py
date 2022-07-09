'''
O (n^2)
                    Insertion Sort

'''
class Insertion_Sort:
    def insert_sort(self,num_list):
        for idx in range(1,len(num_list)):
            jdx=idx
            val=num_list[idx]
            while jdx>0 and num_list[jdx-1]>val:
                num_list[jdx]=num_list[jdx-1]
                jdx-=1
            num_list[jdx]=val
        return num_list


n=[5,4,1,6,9,2,7,3,8]
n=[9,5,1,4,3]

s=Insertion_Sort()
print(s.insert_sort(n))