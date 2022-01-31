from difflib import SequenceMatcher
with open('text1.txt') as file1, open('text2.txt') as file2:
    file1_data = file1.read()
    file2_data = file2.read()
    similarity = SequenceMatcher(None, file1_data, file2_data). ratio() 
    percent = similarity*100
    print(f"The contents of the files are {percent}%  similar.")
