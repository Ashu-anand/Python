from typing import List
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        d={}
        previous_num=64
        c=''
        for idx,val in enumerate(s):
            if val+c in d:
                d[val+c][0]+=1
                d[val+c][2]=idx
            else:
                previous_num+=1
                c=chr(previous_num)
                d[val+c]=[1,idx,idx]
        ans=[]
        for idx in d.items():
            if idx[1][0]>=3:
                ans.append(idx[1][1:])
        return sorted(ans)


s=Solution()
txt="abcdddeeeeaabbbcd"
print(s.largeGroupPositions(txt))