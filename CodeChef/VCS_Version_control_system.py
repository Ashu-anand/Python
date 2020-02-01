PROBLEM: https://www.codechef.com/problems/VCS

Logic: This question requires the Intersection of Tracked and Ignored list and difference of all the files and tracked+ignored list.

for _ in range(int(input())):
    N,I,T=map(int,input().split())
    total=set([i for i in range(1,N+1)])
    ignored=set(map(int,input().split()))
    tracked=set(map(int,input().split()))
    track_ignore=len(ignored.intersection(tracked))
    untack_ignored=len(total.difference(ignored.union(tracked)))
    print(track_ignore,untack_ignored)

