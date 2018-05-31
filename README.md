# wordcount
-------------
Introduction
-------------
This project gets a text file as an input from the command line and counts the number of time a particular word occurs in 
that text file and sorts the occurances in ascending order. 

-------------
How it works:
-------------
This code gets the file as input and reads it. The file is then converted into a list. All the punctuations are removed and all the letters are converted to lowercase. The program uses dictionary to get the values of each key and adds 1 to it if the word is being repeated or adds 0 when it's not. the list that contsind the wordcount is then sorted from least to the most number of times the word occured. 

----------------
Compile and run
----------------
This program is excuted on the command line.  

# SpellCheck
-------------
Introduction
-------------
This project gets a text file as an input from the command line and identified the misspelled words (American English dictionary) and provide suggestions for the words that are wrongly spelled. 

------------
Installation
------------
 Pip install pyenchant

-------------
How it works:
-------------
This program gets the file as input and reads it. The file is then converted into a list. For every word in the list pyenchant checks if it exisits in the dictionary if not it suggestes words that are more accurate and close to the misspelled words. 

----------------
Compile and run
----------------
This program is excuted on the command line.  
