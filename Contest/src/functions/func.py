'''
Created on Oct 31, 2016

@author: AndreiMsc
'''

import math
global partList

'''
function that adds the list of results of a participant 'args*' to the list of
lists of results 'partList'
input data:
partList - the given list of 'resList'
args* - the list that will be added to the 'partList'
    args[0],args[2],args[4] - <P1>,<P2>,<P3> results
output data:
partList' = partList + [args[0],args[2],args[4]]
'''

def add(partList,*args):
    args=[int(args[0]),int(args[1]),int(args[2])]
    partList.append(args)
    return partList

'''
function that removes participants from position 'args[0]' to position 'args[2]'
input data:
partList - the given list of lists of results
args* = [args[0]] or [args[0],' ','to',' ',args[2]] (if command is 'remove..to..')
output data:
partList' = partList, with partList[args[0]],partList[arg[0]+1],..,partList[args[2]] each taking [0,0,0]
raises:
ValueError - when args[0] or arg[2] not a valid position inside the list 'partList'
           - when args[1] is not 'to'
           - when args[0] or args[2] are not integer numbers
'''

def remove(partList,*args):
    if len(args)==1:
        try:
            int(args[0])
        except ValueError as ve:
            raise ValueError('Invalid Input!')
        if int(args[0])<0 or int(args[0])>len(partList)-1:
            print('Invalid position inside list! Minimum index:0; Maximum index:',len(partList)-1,'\n')
            return partList
        else:
            partList[int(args[0])]=[0,0,0]
        return partList
    elif len(args)==3:
        try:
            a=int(args[0])+int(args[2])
        except ValueError as ve:
            raise ValueError('Invalid Input!')
        if args[1]!='to':
            raise ValueError('Invalid syntax!')
            return partList
        if int(args[0])<0 or int(args[0])>len(partList)-1 or int(args[2])<0 or int(args[2])>len(partList)-1 or int(args[0])>int(args[2]):
            print('Invalid positions inside list! Position1 </= Position2! Minimum index:0; Maximum index:',len(partList)-1,'\n')
            return partList
        else:
            for i in range(int(args[0]),int(args[2])+1):
                partList[i]=[0,0,0]
        return partList

'''
function that removes participants which have the average score smaller, larger than or equal to a given float or integer
input data:
partList - the given list of lists of results
args* = args[0] - the relation sign: '<'/'>'/'='
        args[1] - the given integer
output data:
partList' = partList with the scores of those participants set to 0 
raises:
ValueError - when args[1] is not an integer or float number
'''
def removeByScore(partList,*args):
    try:
        float(args[1])
    except ValueError as ve:
        raise ValueError('Invalid Input!')
    for i in range(len(partList)):
        if args[0]=='=':
            if float(partList[i][0])+float(partList[i][1])+float(partList[i][2])==float(args[1])*3:
                partList[i]=[0,0,0]
        elif args[0]=='<':
             if float(partList[i][0])+float(partList[i][1])+float(partList[i][2])<float(args[1])*3:
                partList[i]=[0,0,0]
        else:
             if float(partList[i][0])+float(partList[i][1])+float(partList[i][2])>float(args[1])*3:
                partList[i]=[0,0,0]
    return partList

'''
function that inserts the list of results of a participant 'args[0]','args[1]','args[2]' to the list
of lists of results 'partList' on a given position 'args[4]'
input data:
partList - the given list of 'resList'
args[1],args[2],args[3] - the results of <P1>,<P2> and <P3> that will be added to the 'partList'
args[4] - the position on which the results will be added to the 'partList'
output data:
partList' = partList[:args[4]] + [int(args[0]),int(args[1]),int(args[2])] + partList[args[4]+1:]
'''
def insert(partList,*args):
    if int(args[4])<0 or int(args[4])>len(partList):
        print('Invalid position inside list! Minimum index:0; Maximum index:',len(partList),'\n')
        return partList
    else:
        partList.insert(int(args[4]),[int(args[0]),int(args[1]),int(args[2])])
    return partList

'''
function that replaces the 'args[1]' score of participant 'args[0]' with 'args[2]'
input data:
spartList - the given list of results
args[0] - the position in 'partList' of the participant of which result will be modified
args[1] - the problem of which result will be modified
args[3] - the new score to which will be set for 'args[1]'
output data:
partList' - the list with the modification: 'partList[args[0]][int(args[1][p])]=args[3]' ; where p=0 if args[1]=P1, 1 is P2, 2 if P3
raises:
ValueError - when 'args[1]' is different than 'P1','P2' or 'P3'
'''
def replace(partList,*args):
    if args[1]!="P1" and args[1]!="P2" and args[1]!="P3":
        raise ValueError('Problems are called <P1>, <P2> or <P3>!\n')
    if args[1]=="P1":
        p=0
    else:
        if args[1]=="P2":
            p=1
        else:
            p=2
    partList[int(args[0])][p]=int(args[3])
    return partList

'''
function that will change the score of particiants as follow: if the sum of scores of the participants is fair, the list of scores
will be replaced with a list with the form '[sqrt,sqrt,sqrt]', where sqrt is the square root of the sum of the scores of the participant
input:
partList - the given list of lists of scores/ the given list of participants
output:
partList' = partList with the following changes: if the sum of scores of a list in 'partList' is fair, the list will be replaced
with a list with the form [sqrt,sqrt,sqrt], where sqrt is the square root of the sum of the scores of the participant
'''
def fairToSqrt(partList):
    for i in range(1,len(partList)):
        sum=(partList[i][0]+partList[i][1]+partList[i][2])
        if sum%2==0:
            partList[i][0]=int(math.sqrt(sum))
            partList[i][1]=int(math.sqrt(sum))
            partList[i][2]=int(math.sqrt(sum))
    return partList

'''
function that prints the participants which have the average score =, < or > than a given number.
input:
partList - the given list of scores of participants
args = args[0]- the relation sign, args[1]- the given number
'''
def listInRel(partList,*args):
    condList=[]
    for i in range(len(partList)):
        if args[0]=='=':
            if float(partList[i][0])+float(partList[i][1])+float(partList[i][2])==float(args[1])*3:
                condList.append(partList[i])
        elif args[0]=='<':
             if float(partList[i][0])+float(partList[i][1])+float(partList[i][2])<float(args[1])*3:
                condList.append(partList[i])
        else:
             if float(partList[i][0])+float(partList[i][1])+float(partList[i][2])>float(args[1])*3:
                condList.append(partList[i])
    return(condList)

'''
function that calculates the average score of a participant inside the list 'partList'
input:
partList - the given list of participants
i - the position of the participant
output:
partAvg - the average of the participant
'''
def calcPartAvg(partList,i):
    partAvg=(float(partList[int(i)][0]+float(partList[int(i)][1])+float(partList[int(i)][2]))/3)
    return partAvg
    
'''
function that calculates the average of the average scores of participants between two given positions inside the list 'partList'
input:
partList - the given list of participants
args = args[0],args[2] positions between which the average is calculated
output:
average - the average of the participants between the two position
'''

def calcAvg(partList,*args):
    sumAvgPart=0
    for i in range(int(args[0]),int(args[2])+1): 
        sumAvgPart+=calcPartAvg(partList,i)
    average=sumAvgPart/(float(args[2])-float(args[0])+1)
    return (average)

'''
function that calculates the smallest average of the average scores of participants between two given positions inside the list 'partList'
input:
partList - the given list of participants
args = args[0],args[2] positions between which the smallest average is looked for
output:
min - the smallest average of the participants between the two position
'''
def minAvg(partList,*args):
    min=calcPartAvg(partList,args[0])
    for i in range(int(args[0])+1,int(args[2])+1): 
        if calcPartAvg(partList,i)<min:
            min=calcPartAvg(partList,i)
    return (min)

'''
function that sorts a given list of lists by the average of included lists descending
input:
partList - the given list of lists
output:
sortedList = 'partList' ordered descending by the average values
'''
def sortList(partList):
    sortedList = sorted(partList, key=lambda x: -(int(x[0])+int(x[1])+int(x[2])))
    return sortedList

'''
function that sorts descending a given list of lists by the value of a certain position in the included lists
input:
partList - the given list of lists
problem - the position from the included lists
output:
sortedList = 'partList' ordered descending by the values from the 'position' in he included lists
'''
def sortListProblem(partList,problem):
    sortedList = sorted(partList, key=lambda x: -(int(x[problem])))
    return sortedList

'''
functions that return the first 'x' participants with the highest average score or the highest score at a given problem
input:
sortedList - the given list of participants
args = the number of participants to be returned
 or
args = args[0] - the number of participants to be returned
       args[1] - the problem which to be taken into consideration
'''
def top(partList,sortedList,*args):
    topList=[]
    if len(args)==1:
        for i in range(int(args[0])):
            topList.append(sortedList[i])
        return topList
    else:
        if args[1]=="P1":
            p=0
        elif args[1]=="P2":
            p=1
        else:
            p=2
        sortedList= sortListProblem(partList,p)
        for i in range(int(args[0])):
            topList.append(sortedList[i])
        return topList
        



