# -*- coding: utf-8 -*-
"""
Created on Wed May  1 17:34:31 2019

@author: Suleman
"""

import re, math
from collections import Counter

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)


def similarity_sentences(text1, text2):
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2) 

    cosine = get_cosine(vector1, vector2)

    return cosine

text1 = 'Lahore is a beautiful city what the hell is going on'
text2 = 'Computer science relevant field'

print(similarity_sentences(text1, text2))
       