for _ in range(int(input())):
    company=input().split()
    offers=input().split()
    for val in company:
        if val in offers:
            print(val)
            break