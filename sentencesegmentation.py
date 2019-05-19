# -*- coding: utf-8 -*-
"""
Created on Sun Sep 02 22:33:09 2018

@author: deadp
"""
#import csv 

'''  Took help from the internet/book/friend. Not solely my idea !!  '''

import re

'''  Initializing the prefixes and suffixes and else   '''
caps = "([A-Z])"
digits = "([0-9])"
lower = "([a-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr|MR|MRS)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
caps = "([A-Z])"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](edu|com|net|org|io|gov)"
digits = "([0-9])"


def split_sentences(text):
#    print text
    text = " " + text + "  "
#    print text
    ''' Get the whole corpus removing all the new lines'''
    text = text.replace("\n"," ")
#    print text
    ''' Replace the dot on prefeixes with <use>  '''
    text = re.sub(prefixes,"\\1<use>",text)
    text = re.sub(digits + "[.]" + digits,"\\1<prd>\\2",text)
#    print text
    ''' For the websites : Not really applicable for this project '''
    text = re.sub(websites,"<use>\\1",text)
    print text
    ''' For Ph.D'''
#    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + caps + "[.] "," \\1<use> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    
    '''A.B.C '''
    text = re.sub(caps + "[.]" + caps + "[.]" + caps + "[.]","\\1<use>\\2<use>\\3<use>",text)
    '''  A.B  '''
    text = re.sub(caps + "[.]" + caps + "[.]","\\1<use>\\2<use>",text)
    ''' a.b, e.g, i.e'''
    text = re.sub(lower + "[.]" + lower + "[.]","\\1<use>\\2<use>",text)
    ''' i.e., e.g. '''
    text = re.sub(lower + "[.]" + lower + "[.]"+ lower + "[.]","\\1<use>\\2<use>",text)
    
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<use>",text)
    
    ''' .A.'''
    text = re.sub(" " + caps + "[.]"," \\1<use>",text)
    
    '''checking for special cases like ...., ? , ! '''
    if "..." in text: text = text.replace("...","<prd><prd><prd>")
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<use>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    i=1
    
    ''' writing output.txt'''
    with open('output.txt','w') as text_file:
        for s in sentences:
            print str(i) + ':' +s.strip()
           
            text_file.write(str(i) + ':' +s.strip()+"\n")
            i+=1
#    return sentences
with open('input.txt') as r:
    sentence= r.read()
#    print 'sentence         =',sentence  
    split_sentences(sentence)
    
#    print split_into_sentences(sentence)
    
    
