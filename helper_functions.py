from nltk.corpus import wordnet as wn

def has_alpha(word):
	abet = 'abcdefghijklmnopqrstuvqrstuvwxyz'
	return any([c in abet for c in word.lower()])

def standard_body(body):
	body = body.replace('\n', ' ').replace("\'","'")
	i=0
	while body[i].isupper() or body[i]==' ':
		i=i+1
	return body[0:i].lower() + body[i:]
	
def is_hyper_of(word,base):
	base = wn.synset(base+'.n.01')
	if wn.synsets(word,'n'):
		w = wn.synsets(word,'n')[0]
	else:
		return False
	return base in base.lowest_common_hypernyms(w)

	