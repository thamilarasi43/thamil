string=raw_input("Enter string:")
char=0
word=1
for i in string:
  char=char+1
  if(i==' '):
    word=word+1
print("number of words in a string:")
print(word)
print("Number of charactrs in a string:")
print(char)
