#--------file paths------

# import os

# directory =input("Input :")
# print("Output :")

# for root, dir, files in os.walk(directory):
#     for file in files:
#         file_path = os.path.join(root,file)
#         print(file_path)


#--------count word frequency in csv file---

# import pandas as pd
# from collections import Counter

# def count_word(file_path):
#     try:
#         data = pd.read_csv(file_path)
#         text = " ".join(data.to_string(index=False).split())
#         word_counts = Counter(text.lower().split())
#         return word_counts
    
#     except Exception as e:
#         print(f"Error processing {file_path}: {e}")
#         return None

# csv_file = "/home/chandu/Desktop/sample.csv"
# word_frequencies = count_word(csv_file)

# if word_frequencies:
#     print("\nWord frequencies in the CSV file:")
#     for word, count in word_frequencies.most_common():
#         print(f"{word}: {count}")



#--------count word frequency in excel file---

import pandas as pd
from collections import Counter

def count_word_xlsx(file_path):
    try:
        data = pd.read_excel(file_path)
        text = " ".join(data.to_string(index=False).split())
        word_counts = Counter(text.lower().split())
        return word_counts

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

xlsx_file = "/home/chandu/anaconda3/FINAL450.xlsx"
word_frequencies = count_word_xlsx(xlsx_file)

if word_frequencies:
    print("\nWord frequencies in the XLSX file:")
    for word, count in word_frequencies.most_common():
        print(f"{word}: {count}")