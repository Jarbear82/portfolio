# Overview

mdNoteSearch is a python script that reads all of the '.md' files in a given
directory and parses them into a note structure in python. The user is then
able to enter a keyword, and will be presented with the file names of all the
notes which contain that keyword.

mdNoteSearch is part of a larger project called TaoChat. TaoChat is an AI
Chatbot meant to answer questions and brainstorm your ideas based on your
notes. The purpose of this particular script is to locate relevant files,
tokenize them (optimized input for AI prompts) and feed the information to the
AI request API.

[Demonstration](https://youtu.be/sviw1MFwxEo)

# Development Environment

- Notepad++
- Python3
- Powershell

Python modules used:
- os (to interact with local files and directories)
- re (for splitting text into words)
- collections (for an alternate dictionary)

# Useful Websites

- [W3 Schools:](https://www.w3schools.com/python/) For reference
- [Python Documentation:](https://docs.python.org/3/library/re.html) For regular expressions
- [Python Documentation:](https://docs.python.org/3/tutorial/inputoutput.html) For reading files


# Future Work

- Format functions so they can be used as a module
- Refactor code so that it doesn't need to iterate through lists multiples times
- Write a tokenize function that takes in the located note names and returns the tokenized notes as a string
