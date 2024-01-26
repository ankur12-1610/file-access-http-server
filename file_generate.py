import random
import string
import sys

def generateRandomWord(l):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=l))
    return res

def func(i):
    filename=f"tmp/data/{i}.txt"
    file=open(filename,'w')
    totalGenString=""
    line=1
    while sys.getsizeof(totalGenString)<1024*101*100:
        b=random.randint(0,5)
        a=random.randint(20,100)
        curString=f"{line} "+ generateRandomWord(a)+" "
        if b==0:
            curString+="\n"
            line+=1
        totalGenString+=curString
        file.write(curString)



for i in range(3,7):
    func(i)