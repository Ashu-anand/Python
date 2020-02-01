PROBLEM LINK:
https://www.codechef.com/problems/POTATOES


Logic:
1) We need to first the 2 numbers and then we need to find the prime number greater then these 2 numbers
2) if this is a one time code, then we should run the loop till the number and keep adding untill we find something. This is a brute force logic
3) Else, we can make a array of all the prime numbers till 4000 and then just keep checking there is if exists or not.


Solution:

lt=[True]*4000
lt[0]=False
lt[4::2]=[False]*len(lt[4::2])
for i in range(3,65,2):
    lt[i*i::i]=[False]*len(lt[i*i::i])
for _ in range(int(input())):
    s1,s2=map(int,input().split())
    idx=s1+s2+1
    while True:
        if lt[idx]:
            print(idx-s1-s2)
            break
        else:
            idx=idx+1


