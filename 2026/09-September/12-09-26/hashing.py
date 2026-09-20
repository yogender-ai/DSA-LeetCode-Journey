"""
DSA Lesson · Hashing

Pattern : Arrays & Hashing
Written : 12 Sep 2026
Time    : O(n)
Space   : O(1)
"""

#Hashing
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
