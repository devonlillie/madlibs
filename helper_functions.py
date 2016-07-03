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
	
def is_animal(word,base ='lamb'):
	animal = wn.synset(base+'.n.01')
	if wn.synsets(word,'n'):
		syns = wn.synsets(word,'n')[0]
	else:
		return False
	return wn.synset('animal.n.01') in animal.common_hypernyms(syns)



	