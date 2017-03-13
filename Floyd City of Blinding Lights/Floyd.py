n, m=(raw_input().split(' '))
n=int(n)
m=int(m)

class Node:
    def __init__(self, nodeNumber):
        #id must=position in lst
        self.nodeNumber=nodeNumber
        self.paths={}
        self.pathsList=[0]
        self.distances={}
        self.distancesList=[]
        
       
    def addPath(self,destination, distance):
        self.paths[destination]=distance
        self.pathsList.append(destination)
        #self.distances[destination]=distance
        
    def routeTo(self, target):
        1+1
        
        
        #Adds Dist from D to B in B.distances
        #in B, adds dist from C to D in C.distances via B.distances+lenght of path from C to B
    def revUpdateDistances(self):
        global lst
        for i in range(1, len(self.paths)+1):
            #Shares distance info of current node to each connected node
            goal=lst[self.pathsList[i]]
           # goalDist= self.paths.get(i)
            goalDist= self.paths.get(self.pathsList[i])
            #print 'int test',self.paths.get(3)
            #print type(self.pathsList[i])
 

            goal.distances[self.nodeNumber]=goalDist
            print i
            #print self.paths
            print goalDist
            #self.paths[i]
           # print 'adding',self.paths[i], 'to Goaldistances'
            goal.distancesList.append(self.nodeNumber)
           # print 'adding ',self.nodeNumber ,'to GoaldistancesList'
            #Top part works at the moment
            
            for j in range(0, len(self.distances)):
                print 'start distShare'
                share = self.distancesList[j]
                share= self.distances[share]
                #share distance info of other nodes
                #share stored distance plus distance of path
                #TODO: need to only do if destination distances dict
                #is empty for that value, or has a higher value
                targetDictValue=goal.distances.get(self.distancesList[j], None)
                if targetDictValue==None or targetDictValue<self.distances[self.distancesList[j]]:
                    goal.distancesList.append(self.distancesList[j])
                    goal.distances[self.distancesList[j]]=self.distances.get(self.distancesList[j])+self.paths[i]
        
        
        
def getDistance(start, target):
    lst[start].routeTo(target)
    
#Creates empty nodes based on n
lst=[]
lst.append(0)
for i in range(n):
    #lst[i]=Node()
    lst.append(Node(i+1))

    #Fills Nodes with path information
for _ in range (n+1):
    a, b, c=(raw_input().split(' '))
    a=int(a)
    b=int(b)
    c=int(c)
    #print 'addingpath', a, b, c, len(lst)
    #print lst
    lst[b].addPath(a, c)
    
d=int(raw_input())

for i in range(d):
    e, f=(raw_input().split(' '))
    e=int(e)
    f=int(f)
#    getDistance(e, f)

#print lst[4].paths
#for x in range(1, n):
#    lst[x].revUpdateDistances() 

#print lst[2].paths
#print lst[2].pathsList
lst[4].revUpdateDistances()
lst[2].revUpdateDistances()
#lst[2].revUpdateDistances()

#print lst[3].distances

print lst[1].distances
print lst[3].distances
