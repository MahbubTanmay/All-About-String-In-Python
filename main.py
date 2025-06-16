str = "Hello World"


#Length of string
print(len(str))




a = str[2]
print(a) #l

a = str[2:] #print star from position 2 to end
print(a) #llo World

a = str[:4] #print star from start position to position 4
print(a) #Hell

a = str[2:8] #print star from position 2 to position 8
print(a) #llo Wo






#finding position of a word or a character in a string
b=str.find("ll")
print(b) #2






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




