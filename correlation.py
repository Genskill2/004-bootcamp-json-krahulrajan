import json
import math as m
import sys

def load_journal(fname):
	file = open(fname)
	f = json.load(file)
	return f

def compute_phi(fname, event):

    data = load_journal(fname)

    #write down the correlation of event and squirrel
    n11 = 0  #when event is present and squirrel is true
    n00 = 0  #when event is not present and squirrel is false
    n01 = 0  #when event is not present and squirrel is true
    n10 = 0  #when event is present and squirrel is false
    n1p = 0  #count of event
    n0p = 0  #count of absence of event
    np1 = 0  #count squirrel is true
    np0 = 0  #count squirrel is false

    for d in data:
        #print(d)
        if event in d['events']:
            #print(event)
            n1p+=1
            if d['squirrel'] == True:
                n11+=1
                np1+=1
            else:
                n10+=1
                np0+=1
        else:
            n0p+=1
            if d['squirrel'] == True:
                #print(d['squirrel'])
                #print(type(d['squirrel']))
                n01+=1
                np1+=1
            else:
                n00+=1
                np0+=1
                

    #print(n11)
    #print(n00)
    #print(n1p)
    
    
    corr = (n11*n00 - n10*n01) / m.sqrt(n1p*n0p*np1*np0) 
    


    return corr

#works properly
def compute_correlations(fname):

    file = open(fname)
    f = json.load(file)
    d = dict()
    for i in f:
        #print(i)
        for event in i['events']:
            #print(event)
            if event not in d.keys():
                #print(event)
                corr = compute_phi(fname, event)
                d[event] = corr
    return d

def diagnose(fname):
    desired_key1 = ""
    d = compute_correlations(fname)
    desired_key2 = ""
    check_min = 1
    check_max = -1
    #print(d)
    for key,value in d.items():
        if value < check_min:
            check_min = value
            desired_key1 = key
        if value > check_max:
            check_max = value
            desired_key2 = key
    return desired_key2,desired_key1
