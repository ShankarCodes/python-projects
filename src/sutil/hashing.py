import hashlib
import os
from hashlib import sha256

def r():
    return hashlib.md5(os.urandom(50)).hexdigest()

def s(obj):
    return sha256(obj).hexdigest()

def grp(li):
    tr = []
    if len(li)==1:
        return li
    if len(li)%2!=0:
        li = li +[li[-1]]
    for i in range(0,len(li)-1,2):
        tr = tr + [[li[i],li[i+1]]]
    return tr

def hm(lis):
    if not isinstance(lis[0],bytes) and not isinstance(lis[1],bytes):
        return s(bytes(lis[0],"utf-8")+bytes(lis[1],"utf-8"))
    if not isinstance(lis[0],bytes):
        return s(bytes(lis[0],"utf-8")+lis[1])
    if not isinstance(lis[1],bytes):
        return s(lis[0]+bytes(lis[1],"utf-8"))
    return s(lis[0]+lis[1])

def mr(data):
    if len(data)==1:
        return data[0]
    data = [i for i in map(hm,grp(data))]
    print(data)
    print("************************************")
    return mr(data)

tr =['8082c583286c36670f42fe006f9bcf7d',
 '3929054118816d8b26fc18a7e35d7384',
 '2774770c037bfb8af79711767e8e6722',
 'b58fa2e0c3843c9419b1700c20f521ed',
 '888d9a302fe1ae7697cdf2cb8fc66af4',
 'd9fc7a9b44e74fe948d25ef44b6c206f',
 'd23787d362656bdb6b6d4a9da2057453']

print(mr(tr))