import os
import re
from collections import defaultdict

# Define a data structure for notes
class Note:
    def __init__(self, filename, content):
        self.filename = filename
        self.content = content
        self.words = re.findall(r"\w+", content)

    def __str__(self):
        return f"Note Name: {self.filename}\n\n Content: {self.content}\n\n Words: {self.words}\n"

# convert all words to lowercase
def lower_words(word_list):
    for i in range(0, len(word_list)):
        word_list[i] = word_list[i].lower()
    return word_list

# Read all markdown files in a directory
def read_notes(directory):
   # print(f"directory: {directory}")
   notes = []
   # print(f" list_dir: {os.listdir(directory)}")

   for filename in os.listdir(directory):
       if filename.endswith(".md"):
           try:           
               with open(os.path.join(directory, filename), "r") as f:
                  content = f.read()
               notes.append(Note(filename, content))
           except:
               print(f"ERROR: Couldn't read {filename}")
   return notes

# Search notes for a keyword
def search_notes(notes, keyword):
   results = []
   for note in notes:
       if keyword in note.words:
           results.append(note)
   return results

# Main program
def main():
    notes_directory = input("What is the absolute path to the directory of notes? > ")
    notes = read_notes(notes_directory)

    # print(f"\nnotes: {notes}\n")
    
    # Convert words to lowercase
    for note in notes:
        note.words = lower_words(note.words)
        # Displays the words for each note
        # print(f"\nNote: {note.filename}\nWords:{note.words}")
        
    # Find all common words
    
    # Create a dictionary of all words and the number of times they appear
    common_words = []
    word_count = dict()
    all_word_list = []
    for note in notes:
        for word in note.words:
            all_word_list.append(word)
        
    # print(f"ALL WORD LIST: {all_word_list}")
    
    for word in all_word_list:
        #print(f"WORD: {word}")
        if word in word_count.keys():
           word_count[word] += 1
        else:
            word_count[word] = 1
            
    
    # Find the max count in common words
    max_count = 0
    common_articles = ['the', 'to', 'and', 'you', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'i', 'me', 'my', 'of', 'in', 'a']
    for key in word_count.keys():
        if key not in common_articles:
            if word_count[key] > max_count:
                max_count = word_count[key]
    
    for key in word_count.keys():
        if key not in common_articles:
            if (word_count[key] >= max_count - 5):
                common_words.append(key)
    
    # print(word_count)
    # print()
    # print(f"max_count: {max_count}")
    print(f"\nCommon words: {common_words}\n")
    
        
           

    keyword = input("Enter keyword: ")
    results = search_notes(notes, keyword)

    if results:
        print(f"Found notes containing keyword '{keyword}':")
        for result in results:
            print(result.filename)
    else:
        print(f"No notes found with keyword '{keyword}'")

if __name__ == "__main__":
   main()