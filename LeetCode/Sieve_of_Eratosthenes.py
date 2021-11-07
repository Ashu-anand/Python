def SOE(list_of_num):
    prime_num_list = [idx for idx in range(3,list_of_num,2)]
    prime_num_list.insert(0,2)
    for idx in prime_num_list:
        if idx in prime_num_list:
            jdx=0
            p=pow(idx,2)
            while p+jdx*idx<=list_of_num:
                try:
                    prime_num_list.remove(p+jdx*idx)
                except:
                    pass
                jdx+=1

    return prime_num_list

num=10000

print(SOE(num))

