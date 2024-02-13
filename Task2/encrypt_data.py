import os
import pandas as pd
from threading import * 
from time import * 

#function to count word frequency in xlsx file
def word_excel(filepath,dict1):
        data = pd.read_excel(filepath)
        s=" "
        s= s.join(data.to_string(index=False).split())
        text=s[:]
        words=s.lower().split()
        for word in words:
            if word in dict1:
                dict1[word]+=1
            else:
                dict1[word]=1
                
        return dict1,text

#function to count word frequency in text file
def word_csv(filepath,dict1):
        data = pd.read_csv(filepath)        
        c=" "
        c= c.join(data.to_string(index=False).split())
        text=c[:]
        words=c.lower().split()
        for word in words:
            if word in dict1:
                dict1[word]+=1
            else:
                dict1[word]=1
                
        return dict1,text
    
#method for encrypting the data in the respective file   
def encrypt(text,output_file):
    encrypted_text=""
    for char in text:
        if char.isalpha():
            if char=='z':
                encrypted_text+='a'
            elif char=='Z':
                encrypted_text+='A'
            else:
                encrypted_text+=chr(ord(char)+1)
        else:
            encrypted_text+=char
    with open(output_file, 'w') as file:
                file.write(encrypted_text)

d=dict()
path = input('Enter the Directory path:')
for root,dirnames,filenames in os.walk(path):
    for i in filenames:
        filepath = os.path.join(root,i)
        print(filepath)
        if(filepath.endswith('.csv')):
            d,text_csv=word_csv(filepath,d)
            t1=Thread(target=encrypt,args=(text_csv,'/home/chandu/Documents/MAANG/python/Task/Task2/demo.txt'))
            t1.start()
            t1.join()
           
        elif(filepath.endswith('.xlsx')):
            d,text_excel=word_excel(filepath,d)
            t2=Thread(target=encrypt,args=(text_excel,'/home/chandu/Documents/MAANG/python/Task/Task2/demo.txt'))
            t2.start()
            t2.join()

print(d)

