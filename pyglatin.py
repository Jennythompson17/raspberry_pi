#!/usr/bin/env python

""" Pyglatin translator based on Codeacademy Python course"""


"""create Pyg latin suffix"""
pyg = "ay"

print "Welcome to the English to Pig Latin Translator!"

"""User input prompt"""
original = raw_input("Give me a word, any word...")

"""check to make sure the user entered a  word"""
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    
    if first =="a" or first == "e" or first =="i" or first == "o" or first == "u" or first == "y":
        new_word = word + pyg
        print new_word

    else:
        s = word
        second = s[1]
        if second =="a" or second == "e" or second =="i" or second == "o" or second == "u" or second == "y":
            new_word = s[1:]+s[0]+pyg
        else:
            new_word = s[2:]+s[0:2]+pyg
        print new_word

else:
    print "Hey! That's not a word!"
    original = raw_input("Give me another word")
    if original.isalpha() == False:
        print "You're not playing by the rules...come back when you want to play nice"

