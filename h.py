import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
a=int(input())
b=[int(j) for j in input().split()]
for elm in b:
    if elm%2==0:
        print(elm)
for elm in b:
    if elm%2!=0:
        print(elm)
