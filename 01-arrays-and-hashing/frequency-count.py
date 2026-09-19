"""
Practice · Counting frequencies with a dict (hashing basics)
Written : 12 Sep 2026
Run     : python frequency-count.py   then type numbers separated by spaces
"""
print("Welcome")
print("/n Type here what u want: ")
n=list(map(int,input().split()))
freq={}
for x in n:
    if x in freq:
        freq[x]+=1
    else:
        freq[x]=1
print(freq)
