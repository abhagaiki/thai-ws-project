
#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import Dictionary
dictionary = Dictionary.dictionary

print("Welcome to Thai Word Segmentation")
print("----------------------------------")
word = input("Typing Text Here: ")
print("----------------------------------")

def Segment(word):

    global CurrentText
    Stop = 0
    new = ""
    text = ""
    NText = ""
    CurText = ""
 
    for i in range(len(word)):
        for j in range(len(word)):
            if i < j:
                text = word[i:j+2] 
                if text in dictionary:
                    NText = text
                if (CurText + NText) in dictionary:
                    CurText = CurText + NText
                else:
                    if CurText in NText:
                        CurText = NText
                    else:
                        if NText in CurText:
                            CurText = CurText
                        else:
                            new = word[j-1:] 
                            print(CurText,end='|') 
                            Segment(new)
                            Stop = 1
                            break
       
        if Stop == 1:
            break
    
Segment(word)
print('\n')

    



    
