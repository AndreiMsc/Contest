'''
Created on Oct 31, 2016

@author: AndreiMsc
'''
global partList

from functions.func import replace, removeByScore, remove, add, insert, \
    listInRel


def testReplaceOp():
    assert(replace([[1,2,3],[4,5,6]],1,'P2','with',10)==[[1,2,3],[4,10,6]])
    try:
        replace([[1,2,3],[4,5,6]],5,'P2','with',10)
        assert(False)
    except IndexError:
        assert(True)
    try:
        replace([[1,2,3],[4,5,6]],1,'P4','with',10)
        assert(False)
    except ValueError:
        assert(True)

def testRemoveByScore():
    assert(removeByScore([[1,2,3],[4,5,6],[7,8,9]],'<',5)==[[0,0,0],[4,5,6],[7,8,9]])
    
def testRemoveOp():
    assert(remove([[1,2,3],[4,5,6],[7,8,9]],'1')==[[1,2,3],[0,0,0],[7,8,9]])
    
def testAddOp():    
    assert(add([],1,2,3)==[[1,2,3]])
    assert(add([[1,2,3],[4,5,6]],7,8,9)==[[1,2,3],[4,5,6],[7,8,9]])

def testInsertOp():
    assert(insert([[1,2,3],[7,8,9]],4,5,6,'at',1)==[[1,2,3],[4,5,6],[7,8,9]])
    
def testListInRel():
    list=[[1,1,1],[3,3,3],[10,4,6],[3,7,4],[1,5,3],[9,1,1]]
    command='list < 5'
    pos=command.find(" ")
    if pos==-1:
        return (command,"")
    cmd=command[:pos]
    args=command[pos:]
    args=args.split()
    lastOp=cmd
    assert(listInRel(list,*args)==[[1,1,1],[3,3,3],[3,7,4],[1,5,3],[9,1,1]])

'''
function that performs all tests
'''
def performAllTests():
    testAddOp()
    testRemoveOp()
    testInsertOp()
    testReplaceOp()
    testListInRel()
    testRemoveByScore()
