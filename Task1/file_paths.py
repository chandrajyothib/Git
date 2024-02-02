import os
import pandas as pd
   
#function to count word frequency in xlsx file
def word_excel(filepath,dict1):
        data = pd.read_excel(filepath)
        s=" "
        s= s.join(data.to_string(index=False).split())
        words=s.lower().split()
        for word in words:
            if word in dict1:
                dict1[word]+=1
            else:
                dict1[word]=1
        #word_counts = Counter(text.lower().split())
        return dict1

#function to count word frequency in text file
def word_csv(filepath,dict1):
        data = pd.read_csv(filepath)
        s=" "
        s= s.join(data.to_string(index=False).split())

        words=s.lower().split()
        for word in words:
            if word in dict1:
                dict1[word]+=1
            else:
                dict1[word]=1
        #word_counts = Counter(text.lower().split())
        return dict1

d=dict()
path = input('Enter the Directory path:')
for root,dirnames,filenames in os.walk(path):
    for i in filenames:
        filepath = os.path.join(root,i)
        print(filepath)
        if(filepath.endswith('.csv')):
            word_csv(filepath,d)
        elif(filepath.endswith('.xlsx')):
            word_excel(filepath,d)
          
print(d)
