#--------file paths------

# import os

# directory =input("Input :")
# print("Output :")

# for root, dir, files in os.walk(directory):
#     for file in files:
#         #file_path = os.path.join(root,file)
#         print(root,file)


#--------count word frequency in csv file---

# import pandas as pd

# def count_word(file_path):
#     try:
#         data = pd.read_csv(file_path)
#         s=" "
#         s= s.join(data.to_string(index=False).split())
#         dict1={}
#         words=s.lower().split()
#         for word in words:
#             if word in dict1:
#                 dict1[word]+=1
#             else:
#                 dict1[word]=1
        
#         return sorted(dict1.items(),key=lambda x:x[1],reverse=True)
    
#     except Exception as e:
#         print(f"Error processing {file_path}: {e}")
#         return None

# csv_file = "/home/chandu/Desktop/sample.csv"
# word= count_word(csv_file)

# if word:
#     print("\nWord frequencies in the CSV file:")
#     print(word)

#-------count word frequency in excel files----

import pandas as pd

def count_word(file_path):
    try:
        data = pd.read_excel(file_path)
        s=" "
        s= s.join(data.to_string(index=False).split())
        dict1={}
        words=s.lower().split()
        for word in words:
            if word in dict1:
                dict1[word]+=1
            else:
                dict1[word]=1
        
        return sorted(dict1.items(),key=lambda x:x[1],reverse=True)
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

csv_file = "FINAL450.xlsx"
word_frequencies = count_word(csv_file)

if word_frequencies:
    print("\nWord frequencies in the CSV file:")
    print(word_frequencies)
