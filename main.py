#Be able to input the required filename to select any file in the folder.
filename = input("What file do you want to count? ")

#Select file automatically.
#filename = "story.txt"

def read_file(filename):
    with open(filename) as openfile:
        lines = openfile.read()
    return lines
      
def count_words():
    text = read_file(filename)
    split_text = text.lower().split()
    count = {}
    for i in split_text:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
   
print(count_words())