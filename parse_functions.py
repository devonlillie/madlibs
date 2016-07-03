import pandas as pd
import nltk
def find_subtrees(tree,code):
	matches = []
	for br in tree:
		if type(br) is tuple:
			return True
			
def tag_text(title,sentences,t):
	tags = [t.tag(sent) for sent in sentences]
	wds = [w[0] for x in tags for w in x]
	tgs = [w[1] for x in tags for w in x]
	return pd.DataFrame({'word':wds,'tag':tgs})
	
	
