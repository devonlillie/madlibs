import pandas as pd
import nltk
def find_subtrees(tree,code):
	matches = []
	for br in tree:
		if type(br) is tuple:
			return True

def find_tags(tree,tag):
	matches = []
	for br in tree:
		if type(br) is list:
			matches = matches+find_tags(br,tag)
		else:
			matches += br if br[1]==tag else []
	return matches
	
def print_tags(t):
	if type(t) is tuple:
		return '/'.join(t)
	else:
		return ' '.join([print_tags(i) for i in t])


def replace_tags(sents,newlbl,pos,func):
	return [[(a,'{%s}'%newlbl) if (func(a) and b==pos )else (a,b) for (a,b) in s ] for s in sents]
	
