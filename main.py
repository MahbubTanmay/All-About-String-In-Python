str = "Hello World"


#Length of string
print(len(str))




a = str[2]
print(a) #l

a = str[2:] #print star from position 2 to end
print(a) #llo World

a = str[:4] #print star from start position to position 4
print(a) #Hell

a = str[2:8] #print star from position 2 to position 5
print(a) #llo Wo







#To Capital Hand
print(str.upper())


#To Small Hand
print(str.lower())





#direct paragraph
para ='''Its me Bro
I need nothing.

he said"How are u?"
I ,said Im fine'''

print(para)






#in *str, the * syntax in Python is part of what's called unpacking.it unpacks the string "Hello" into individual characters—'H', 'e', 'l', 'l'

print(*str) #H e l l o   W o r l d
print(*str, sep="-") #H-e-l-l-o- -W-o-r-l-d





#print string character after character
for i in(str):
    print(i)
'''
This will print
H
e
l
l
o

W
o
r
l
d
'''







a="!!! Hello !!! Bro!!!!"
print(a.strip("!")) #Remove given character if it is at the begining or at the end. here output: Hello !!! Bro
print(a.rstrip("!")) #Remove given character if it is at the end. here output: !!! Hello !!! Bro








#finding position of a word or a character in a string
b=str.find("ll")
print(b) #2





# replace word or letter from string.  string_variable.replace(original_word , new_word)
b="Hello From Pithon"
print(b.replace("Pithon","Python"))  # Word Replace
print(b.replace("i","y"))  # Character Replace









# conut how much a word or char used in a line.This is case sensitive so hi and Hi will be two different word.
g="Hey John, are you John?"
print(g.count("John")) #2
print(g.count("o")) #3









# Convert every define character separated words into a list item. string_variable.split(define_word)
c="Player1 Player2 Player3"
print(c.split(" ")) # ['Player1', 'Player2', 'Player3']
d="Player4-Player5-Player6"
print(d.split("-")) # ['Player4', 'Player5', 'Player6']








# Capitalize the first word
e="this is a line"
print(e.capitalize()) # This is a line








# Put the line at the center of the page.  string_variable.center(percentage_of_char , what_will_use)
f="Put it at the center"
print(f.center(30," ")) #      Put it at the center
print(f.center(50,"*")) # ***************Put it at the center***************






# this is a bool type so print true or false
h="Bangladesh is beautiful!"
print(h.endswith("!")) #check the end
print(h.endswith("is",5,13)) #if string from 5 to 14 ends with --> is







# check if contain only A-Z or a-z or 0-9 .this is a bool type so print true or false
i="BangladeshZindabadX9999"
print(i.isalnum())


# check if contain only A-Z or a-z. this is a bool type so print true or false
i="BangladeshZindabadX"
print(i.isalpha())


'''
some useful:

string_variable.isdecimal() = to check if from 0-9

string_variable.isisascii() = to check if ASCII supported

string_variable.isupper() = to check if Uppercase

string_variable.istitle() = to check if 1st charcater  of every word is Capital






string_variable.swapcase() = to convert every uppar character into lower and lower into upper

string_variable.title() = to convert 1st charcater  of every word into Capital

'''


