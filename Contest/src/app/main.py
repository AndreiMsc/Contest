'''
Created on Oct 31, 2016

@author: AndreiMsc
'''
from UI.console_UI import setUp, run
from tests.tst import performAllTests


if __name__ == '__main__':
    pass



def main():
    global partList
    partList=[]
    partList=setUp(partList)
    performAllTests()
    run(partList)

main()
