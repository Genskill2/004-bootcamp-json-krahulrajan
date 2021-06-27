# Add the functions in this file
# Add the functions in this file
import math as m
import json

def load_journal(fname):

	f = json.load(fname)
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
		if event in d.values():
			n10+=1
			if d['squirrel'] == 'true':
				n11+=1
				np1+=1
			else:
				n10+=1
				np0+=1
		else:
			n0p+=1
			if d['squirrel'] == 'true': 
				n01+=1
				np1+=1
			else:
				n00+=1
				np0+=1
	corr = (n11*n00 - n10*n01) / m.sqrt(n1p*n0p*np1*np0) 



	return corr

def compute_correlations(fname):
	f = json.load(fname)
	d = dict()
	for i in f:
		for event in i.values():
			if event not in d.keys():
				corr = compute_phi(fname, event)
				d[event] = corr
	return d

def diagnosis(fname):
	desired_key = ""
	d = compute_correlations(fname)
	check_val = 1
	for key,value in d.items():
		if value < check_val:
			desired_key = key
	return desired_key



