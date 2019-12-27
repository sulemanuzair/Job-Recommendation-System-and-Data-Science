# -*- coding: utf-8 -*-
"""
Created on Wed May  1 17:10:24 2019

@author: Suleman
"""

from fuzzywuzzy import process, fuzz


data =pd.read_csv("textcolumns.tsv", sep='\t')


r = data.assign(Output=[process.extract(i, data['Col-1']) for i in data['Col-2']])
r.to_csv('output.txt')


print (fuzz.ratio("Lahore is a beautiful city what the hell is going on", "among as long as sometimes its rank should be good what the hell is going ong beautiful city is Lahore"))



