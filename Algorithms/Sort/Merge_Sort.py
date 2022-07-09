'''
O (n^2)
                    Merge Sort
1) Keep Spliting the number and call the function recursivly till, we have 1 number. Do this with left
    and right
2) Once then, just merging left list with right list.
'''
class Merge_Sort:
    def merge_sort(self,num_list):
        if len(num_list)<=1:
                return num_list
        mid=(len(num_list))//2
        left_list=self.merge_sort(num_list[:mid])
        right_list=self.merge_sort(num_list[mid:])

        i=j=0
        num_list=[]
        while i<len(left_list) and j<len(right_list):
            if left_list[i]>right_list[j]:
                num_list.append(right_list[j])
                j+=1
            else:
                num_list.append(left_list[i])
                i+=1
        num_list.extend(left_list[i:])
        num_list.extend(right_list[j:])

        return num_list


n=[5,4,1,6,9,2,7,3,8]
n=[2,3,8,9,1,6,7,10]

s=Merge_Sort()
print(s.merge_sort(n))