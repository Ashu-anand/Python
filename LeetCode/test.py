def main_fact(num):
    print(num)
    if num==1:
        return 1
    ans=num*main_fact(num-1)
    return ans

n=1000
print(main_fact(n))