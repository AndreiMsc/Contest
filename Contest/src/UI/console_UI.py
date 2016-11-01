'''
Created on Oct 31, 2016

@author: AndreiMsc
'''

'''
function that reads the command from the keyboard; the command is splitted at spaces, with the
first 'word' becoming the comand 'cmd' and the rest becoming arguments '*args'
input:
command - syntax from keyboard
output:
cmd - the actual command
*args - the arguments of the command (unknown number)
'''

'''
function that sets up the list of participants
'''
def setUp(partList):
    partList=[[0,0,0],[2,2,2],[1,1,1],[3,3,3],[5,5,5],[4,4,4],[7,7,7],[6,6,6],[8,8,8],[9,9,9]]
    return(partList)
    
from functions.func import add, remove, removeByScore, insert, replace, \
    listInRel, sortList, calcAvg, minAvg, fairToSqrt, top


def readCmd():
    command=input('Please type a command...\n')
    pos=command.find(" ")
    if pos==-1:
        return (command,"")
    cmd=command[:pos]
    args=command[pos:]
    args=args.split()
    return (cmd,*args)

def addUI(partList,*args):
    if len(args)!=3:
        raise ValueError('Invalid parameters number!')
        return partList
    try:
        a=int(args[0])+int(args[1])+int(args[2])
    except ValueError as ve:
        ve='Invalid parameters!'
        print(ve)
        return partList
    if int(args[0])>10 or int(args[1])>10 or int(args[2])>10 or int(args[0])<0 or int(args[1])<0 or int(args[2])<0:
        print('Values are too big, too small or invalid! Score is from 0 to 10.\n')
        return partList
    args=[args[0],args[1],args[2]]
    add(partList,*args)

def removeUI(partList,*args):
    if len(args)!=1 and len(args)!=3 and len(args)!=2:
        raise ValueError('Invalid parameters number!')
    if len(args)==1 or len(args)==3:
        try:
            remove(partList,*args)
        except ValueError as ve:
            print(ve)
    else:
        if args[0]!="=" and args[0]!=">" and args[0]!="<":
            print('Invalid relation sign!')
            return partList
        try:
            removeByScore(partList,*args)
        except ValueError as ve:
            print(ve)

def insertUI(partList,*args):
    if len(args)!=5:
        raise ValueError('Invalid parameters number!')
    if int(args[0])>10 or int(args[1])>10 or int(args[2])>10 or int(args[0])<0 or int(args[1])<0 or int(args[2])<0:
        print('Values are too big, too small or invalid! Score is from 0 to 10.\n')
        return partList
    try:
        a=int(args[0])+int(args[1])+int(args[2])
    except ValueError as ve:
        ve='Invalid parameters!'
        print(ve)
        return partList
    if args[3]!='at':
        print('Invalid syntax!')
        return partList
    else:
        try:
            int(args[4])
        except ValueError as ve:
            ve='Invalid position parameter!'
            print(ve)
            return partList
    insert(partList,*args)

def replaceUI(partList,*args):
    if len(args)!=4:
        raise ValueError('Invalid parameters number!')
        return partList
    if int(args[0])<0 or int(args[0])>len(partList)-1:
        print('Invalid position inside list!Minimum index:0; Maximum index:',len(partList)-1,'\n')
        return partList
    if args[2]!="with":
        print('Invalid syntax!')
        return partList
    try:
        a=int(args[0])+int(args[3])
    except ValueError as ve:
        ve='Invalid input!'
        print(ve)
        return partList
    if int(args[3])>10 or int(args[3])<0:
        print('Values are too big or too small! Score is from 0 to 10.\n')
        exit      
    replace(partList,*args)

def printListInRel(partList,*args):
    condList=listInRel(partList,*args)
    printList(condList)

def printList(list):
    for i in range(len(list)):
        print(list[i])

def listUI(partList,*args):
    if len(args)==1:
        if args==('sorted',):
            printList(sortList(partList))
            return(partList)
        elif args==('',):
            printList(partList)
        else:
            print('Invalid syntax!')
    elif len(args)==2:
        if (args[0]!='=' and args[0]!='>' and args[0]!='<'):
            print('Invalid relation sign!')
            return partList
        try:
            float(args[1])
        except ValueError as ve:
            ve='Invalid parameter'
            print(ve)
            return(partList)
        if float(args[1])<0.0 or float(args[1])>10.0:
            print('Invalid parameter!')
            return partList
        printListInRel(partList,*args)

def avgUI(partList,*args):
    if len(args)!=3 or args[1]!='to':
        print('Invalid syntax!')
        return partList
    else:
        try:
            int(args[0]+args[2])
        except ValueError as ve:
            ve='Invalid parameters!'
            print(ve)
            return partList
    if args[0]>args[2]:
        print('Invalid parameters!')
        return partList
    if int(args[2])>len(partList)-1  or int(args[0])<0:
        print('Invalid index! Minimum index:0; Maximum index:',len(partList)-1)
        return partList
    print(calcAvg(partList,*args))

def minUI(partList,*args):
    if len(args)!=3 or args[1]!='to':
        print('Invalid syntax!')
        return partList
    else:
        try:
            int(args[0]+args[2])
        except ValueError as ve:
            ve='Invalid parameters!'
            print(ve)
            return partList
    if args[0]>args[2]:
        print('Invalid parameters!')
        return partList
    if int(args[2])>len(partList)-1  or int(args[0])<0:
        print('Invalid index! Minimum index:0; Maximum index:',len(partList)-1)
        return partList
    print(minAvg(partList,*args))
    
def fairToSqrtUI(partList,*args):
    fairToSqrt(partList)

def topUI(partList,*args):
    sortedList=sortList(partList)
    if len(args)==1:
        try:
            int(args[0])
        except ValueError as ve:
            ve='Invalid parameter!'
            print(ve)
            return partList
        if int(args[0])>len(sortedList) or int(args[0])<1:
            print('Invalid parameter!')
            return partList
        printList(top(partList,sortedList,*args))
    else:
        if args[1]!='P1' and args[1]!='P2' and args[1]!='P3':
            print('Problems are called <P1>, <P2> and <P3>!')
            return partList
        else:
            try:
                int(args[0])
            except ValueError as ve:
                ve='Invalid parameter!'
                print(ve)
                return partList
        if int(args[0])>len(sortedList) or int(args[0])<1:
            print('Invalid parameter!')
            return partList
        printList(top(partList,sortedList,*args))
        
'''
function that will undo the last operation
input:
undoList - the list of command that were used; the last element will be deleted with every use of 'undo'
output:
partList' = 'partList' without the last command operated on
'''
def undo(partList,undoList):
    partList=setUp(partList)
    cmdsList={"add":addUI,"remove":removeUI,"insert":insertUI,"replace":replaceUI,"fairtosqrt":fairToSqrtUI}
    del undoList[len(undoList)-1]                    
    for i in range(len(undoList)):
        command=undoList[i]                             
        command=" ".join(command)
        pos=command.find(" ")
        if pos==-1:
            return (command,"")
        cmd=command[:pos]
        args=command[pos:]
        args=args.split()
        cmdsList[cmd](partList,*args)
    return partList

def undoUI(partList,undoList,*args):
    if args!=('',):
        print('Invalid syntax!')
        return partList
    if undoList==[]:
        print('There are no more commands to undo!\n')
        return partList
    partList=undo(partList,undoList)
    return partList
    
'''
function that will call, after using <run> function, one command from the dictionary of commands
'cmdsList',"exit" or "undo"
input:
cmd - the actual command returned by <run> function
*args - the arguments returned by <run> function
output:
'Invalid command!' - when the command 'cmd' does not exist in commands dictionarey 'cmdsList'
ValueError - through '<function>UI', when the numbers of arguments is invalid
'''
def run(partList):
    undoList=[]
    print('Wellcome user!')
    cmdsList={"add":addUI,"remove":removeUI,"insert":insertUI,"replace":replaceUI,"list":listUI,"fairtosqrt":fairToSqrtUI,"avg":avgUI,"min":minUI,"top":topUI}
    while True:
        ok=1
        (cmd,*args)=readCmd()
        if cmd=="exit":
            print('Not exactly the best choice...\n')
            break
        elif cmd in cmdsList:
            try:
                cmdsList[cmd](partList,*args)
            except ValueError as ve:
                ok=0
                print(ve)
            if ok==1:
                if cmd=='add' or cmd=='remove' or cmd=='insert' or cmd=='replace' or cmd=='fairtosqrt':
                    undoList.append([cmd,*args])
                else:
                    ok=0
            else:
                ok=0
        elif cmd=="undo":
            partList=[]
            partList=undoUI(partList,undoList,*args)
        else:
            print('Invalid command!\n')