#!/bin/python
def insertionSort(ar):
    
    insertPos=findInsertPosition()
    x=1
    for i in range(insertPos, len(ar)):
        x+=1
        pos=len(ar)-x
        if i==len(ar)-1:
            ar[insertPos]=toInsert
        else:
            ar[pos+1]=ar[pos] 
        printResult()
     
    ar[insertPos]=toInsert

    return ar

def printResult():
    printString=''
    for i in range(len(ar)):
        printString=printString+str(ar[i])
        printString+=" "
    print printString
    
def findInsertPosition():
    InsertPos=0
    for i in range(len(ar)):
        if toInsert<ar[i]:
            InsertPos=i
            break
    #print InsertPos
    return InsertPos    
    
def sorted():
    result=True
    i1, i2=0, 0
    for i in range(len(ar)):
        i1=i2
        i2=ar[i]
        if i2<i1: result=False
    return result
        
    
m = input()
ar = [int(i) for i in raw_input().strip().split()]

toInsert=ar[len(ar)-1]

insertionSort(ar)