import numpy as np
import Database.CRUD as db

class Dictionary:

    class Node:

        def __init__(self):
            self.children=np.empty([26], dtype=object)
            self.eow=False

    
    root=Node()


    def insert(self,word):
        word=word.lower()
        temp=self.root
        for i in word:
            idx=ord(i)-ord('a')
            
            if(temp.children[idx]==None):
                temp.children[idx]=self.Node()
            
            temp=temp.children[idx]
        temp.eow=True
        

    def search(self,word):
        word=word.lower()
        temp=self.root
        for i in word:
            idx=ord(i)-ord('a')

            if(temp.children[idx]==None):
                return False
            
            temp=temp.children[idx]
        
        return temp.eow==True
    
    def startWith(self,prefix):
        
        temp=self.root
        for i in prefix:
            idx=ord(i)-ord('a')
            temp=temp.children[idx]
        self.printAllWordOfPrefix(prefix,temp,"")
    
    def printAllWordOfPrefix(self,prefix,curr,str):
        if(curr.eow==True):
            print(prefix+str)
            
        
        for i in range(26):
            if curr.children[i]!=None:
                self.printAllWordOfPrefix(prefix,curr.children[i],str+chr(ord("a")+i))

    def printAllWord(self,root,str):
        if root.eow==True:
            print(str)
            
        
        curr=root
        for i in range(26):
            if(curr.children[i]!=None):
                self.printAllWord(curr.children[i],str+chr(ord("a")+i))
                

    def wordBreakProblem(self,key):
        length=len(key)
        if length==0:
            return True
        
        for i in range(length):
            if(self.search(key[:i]) and self.search(key[i:])):
                return True
            
        return False
    


    def main(self):

        try:

            for i in db.getWordFromDB():
                self.insert(i['key'])

        except:

            print("Some Error From DB")

        while(True):

            print("(1)new Add \n(2)Search \n(3)Search Word From Prefix \n(4)Show All Word \n(5)Word Break Problem \n(6)Exit")
            choice=int(input())

            if choice==1:

                word=input("Enter Word : ")
                self.insert(word)
                db.insertInDB(word)

            elif choice==2:

                word=input("Enter Word For Search : ")

                if self.search(word):
                    print("Word is Exist")
                else:
                    print(word,"is not Exist")

            elif choice==3:

                prefix=input("Enter Prefix : ")
                self.startWith(prefix)

            elif choice==4:

                print("\nwords In Dictionary : ")
                self.printAllWord(self.root,"")

            elif choice==5:

                key=input("Enter Full Word")
                if self.wordBreakProblem(key):
                    print("It Exist")
                else:
                    print("It Not Exist")

            elif choice==6:
                break
            
            else:
                print("Invalid Option")
            print()

    


d=Dictionary()
d.main()


        

