# Write a program to demonstrate association rule mining for market basket analysis for suitable support/confidence values.  
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori 

print("extracting records...")
file1 = open('market2.csv', 'r')
Lines = file1.readlines()

datalist = []
count = 0

for line in Lines:
    wordlist = line.strip().split(',')
    datalist.append(wordlist)
file1.close()

print("building rules...")
association_rules = apriori(datalist, min_support=0.007, min_confidence=0.5, min_lift=3, min_length=2)
association_results = list(association_rules)
print(len(association_results))

for item in association_results :
    print("\n===")
    print("items purchased together :", item[0])
    print("Support: " , item[1])
    print("Confidence: " , item[2][0][2])
    print("Lift: " , item[2][0][3])