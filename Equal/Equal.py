t=int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    arr =map(int, raw_input().split())
    
    
    #logic:
    #diff between largest and smallest
    #if diff>5 also check second largest
    #   add 5 as many times as possible until second largest surpasses largest
    #   
    #if 5>diff>2 add 2
    #if 2>diff>0 add 1

    def distribute():
        count=0
        while isFair()==False:
            aMin=min(arr)
            aMax=max(arr)
            if (aMax-aMin)>=5:
                reps=(aMax-secondSmallest())/5
                if reps>1: 
                    addAll(reps*5, aMax)
                    count+=reps
                else: 
                    addAll(5, aMax)
                    count+=1
            #if (aMax-aMin)>=5:
            #    reps=(aMax-aMin)/5
            #    addAll(reps*5, aMax)
            #    count+=reps
                
                
            elif (aMax-aMin)>=2:
                addAll(2, aMax)
                count+=1
                
            elif(aMax-aMin)>=1:
                addAll(1, aMax)
                count+=1
           
    
        return count

    def secondSmallest():
        tempArr=arr
        tempArr.remove(max(tempArr))
        return max(tempArr)
        
    def addAll(n, aMax):
        global arr
        arr.remove(aMax)
        #need to add n to all arr except largest number
        arr=map(lambda x:x+n, arr)
        arr.append(aMax)
        return arr
        
    def isFair():
        if max(arr)==min(arr): 
            return True
        else: 
            return False
    
    
    print distribute()