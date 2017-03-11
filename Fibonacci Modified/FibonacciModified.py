t1, t2, n=raw_input().split()
t1=int(t1)
t2=int(t2)
n=int(n)
fibList=[]
fibList.append(t1)
fibList.append(t2)

def findN():
    
    while n>len(fibList):
        computeNext()
        
def computeNext():
    x=len(fibList)
    x=fibList[x-2]+(fibList[x-1]*fibList[x-1])
    fibList.append(x)

findN()
print fibList[n-1]
