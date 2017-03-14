# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m=(raw_input().split(' '))
n=int(n)
m=int(m)

class Node:
    def __init__(self, nodeNumber):
        self.nodeNumber=nodeNumber
        self.paths={}
        self.pathsList=[0]
        self.distances={}
        self.distancesList=[]
        self.hasPushed=False
        
       
    def addPath(self,destination, distance):
        bpathLen=len(self.paths)
        self.paths[destination]=distance
        apathLen=len(self.paths)
        if apathLen!=bpathLen:
            self.pathsList.append(destination)        
        
    def printInfo(self): #for debugging
        print '========'
        print 'nodeNumber:', self.nodeNumber
        print 'Paths:', self.pathsList, self.paths
        print 'Distances:', self.distancesList, self.distances
        print 'hasPushed', self.hasPushed
        print '========='
        
        
        #Adds Dist from D to B in B.distances
        #in B, adds dist from C to D in C.distances via B.distances+lenght of path from C to B
    def revUpdateDistancesinit(self):
        global lst
        global targetList
        for i in range(1, len(self.paths)+1):
            goal=lst[self.pathsList[i]]    
            if self.hasPushed==False:
                #Shares distance info of current node to each connected node
                goalDist= self.paths.get(self.pathsList[i])
                goal.distances[self.nodeNumber]=goalDist
                goal.distancesList.append(self.nodeNumber)                
                targetList.append(goal.nodeNumber)                
        self.hasPushed=True
        
    def revUpdateDistances(self):
        global lst
        global targetList
        for i in range(1, len(self.paths)+1):
            
            #i should be the paths linked to current node
            goal=lst[self.pathsList[i]]    
                #Shares distance info of current node to each connected node

            
            for j in range(0, len(self.distances)):

                targetDictValue=goal.distances.get(self.distancesList[j], None)

                if targetDictValue==None or targetDictValue>self.distances[self.distancesList[j]]+self.paths[self.pathsList[i]] :

                    
                    if targetDictValue==None:goal.distancesList.append(self.distancesList[j])
                    totalDist=self.distances.get(self.distancesList[j])+self.paths[self.pathsList[i]]  
                    goal.distances[self.distancesList[j]]=totalDist

                    targetList.append(goal.nodeNumber)


        
        
def getDistance(start, target):
    lst[start].routeTo(target)
    
#Creates empty nodes based on n
lst=[]
lst.append(0)
for i in range(n):
    #lst[i]=Node()
    lst.append(Node(i+1))

    #Fills Nodes with path information
for _ in range (m):
    a, b, c=(raw_input().split(' '))
    a=int(a)
    b=int(b)
    c=int(c)
    lst[b].addPath(a, c)
    
d=int(raw_input())

targetList=[]
#targetList acts as a queue

def pathFind(e, f):
    global targetList
    targetList=[]
    targetList.append(f) 
    
    while len(targetList)!=0:
        if lst[targetList[0]].hasPushed==False:
            lst[targetList[0]].revUpdateDistancesinit()
        else:
            lst[targetList[0]].revUpdateDistances()
        del targetList[0]

   

        
for i in range(d):
    e, f=(raw_input().split(' '))
    e=int(e)
    f=int(f)
    pathFind(e, f)
    answer=lst[e].distances.get(f, None)
    if e==f: print 0
    elif answer==None: 
        print -1
    else: print answer




