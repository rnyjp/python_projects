from array import array
from audioop import findfactor
from operator import le
from os import system
import math
import random

system('cls')

def combination_ways(word):
    factorial_denominator = 1
    repeat_list = []
    for x in word_input:
        if word_input.count(x)>1:
            #print(x)
            if repeat_list.count(x)>0:
                continue
            else:
                repeat_list.append(x)                

    #print("\n")
    #print(repeat_list)
    #print("\n")

    for i in repeat_list:
        #print(i+" repeated : "+str(word_input.count(i))) 
        factorial_denominator*=math.factorial(word_input.count(i))

    #print("\n")

    #print("Value of denominator factorial = " +str(factorial_denominator))

    w = int((math.factorial(word_length))/(factorial_denominator))
    #print("\n No: of ways : "+str(w))

    return w


word_list = []
word_count = 0
word_input = input("\n Enter the word : ")

word_length = len(word_input)
print("\n Word length : "+str(word_length))

ways = combination_ways(word_input)
print("\n No: of ways : "+str(ways))

while word_count<ways:
    j = random.sample(word_input, len(word_input))
    new_word = ''.join(j)
    #print(new_word)
    if new_word in word_list:
        #print("Repetition !")
        continue
    else:
        word_list.append(new_word)
        print("\n"+new_word)
        word_count+=1
        
    new_word = None

print("\n Total word count : "+str(len(word_list)))


print("\n")
k = input("Print Enter key to Exit")
