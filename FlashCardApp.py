# -*- coding: utf-8 -*-
"""
Created on Nov. 23  10:23:43 2022
@author: CS115
"""

from FlashCard import *
import random

        
def read_cards( filename ):
    file = open(filename, 'r')
    card_list = []
    for line in file:
        line = line.strip()
        data = line.split()
        card = FlashCard( data[0], data[1], data[2])
        if card not in card_list:
            card_list.append( card )
    return card_list

def is_smaller(obj1,obj2,attr):
    if attr=='Q':
        return obj1.getQuestion()<obj2.getQuestion()
    elif attr=='A':
        return obj1.getAnswer()<obj2.getAnswer()

def is_larger(obj1,obj2,attr):
    if attr=='Q':
        return obj1.getQuestion()>obj2.getQuestion()
        
    else :
        return obj1.getAnswer()>obj2.getAnswer()

def selection_sort(l,attr):
    if attr=='D':
        counter=0
        l1=l[:]
        while counter!=len(l1):
            for i in range(counter+1,len(l1)):
                if l1[counter]>l1[i]:
                    a=l1[counter]
                    l1[counter]=l1[i]
                    l1[i]=a
            counter+=1
        return l1
    elif attr=='Q':
        counter=0
        l1=l[:]
        while counter!=len(l1):
            for i in range(counter+1,len(l1)):
                if is_larger(l1[counter],l1[i],'Q'):
                    a=l1[counter]
                    l1[counter]=l1[i]
                    l1[i]=a
            counter+=1
        return l1  
    elif attr=='A':
        counter=0
        l1=l[:]
        while counter!=len(l1):
            for i in range(counter+1,len(l1)):
                if is_larger(l1[counter],l1[i],'A'):
                    a=l1[counter]
                    l1[counter]=l1[i]
                    l1[i]=a
            counter+=1
        return l1 

def binary_search(l,q):
    l=selection_sort(l, 'Q')
    flag=False
    minim=0
    maxim=len(l)-1
    while flag!=True:
        if minim<=maxim:
            if l[(minim+maxim)//2].getQuestion()<q:
                minim=(minim+maxim)//2+1
            elif l[(minim+maxim)//2].getQuestion()>q:
                maxim=(minim+maxim)//2-1
            else:
                flag=True
                return l[(minim+maxim)//2]
        else:
            break
        
    return None

def create_flash_cards(l,l1,n):
    if len(l1)==n:
        return l1
    else:
        chosen=random.choice(l)
        while chosen in l1:
            chosen=random.choice(l)
        l1.append(chosen)
        return create_flash_cards(l,l1,n)
    

master_liste=read_cards('turkish_english_words.txt')
l1=[]
n=int(input("Enter the number of flash cards to generate: "))
generated=create_flash_cards(master_liste,l1,n)
generated=selection_sort(generated,'D')
print(generated)
print()
inp=input("Enter word to search: ")

obj=binary_search(generated, inp)
if obj:
    print(obj)
else:
    print(f'No translation found for {inp}')
