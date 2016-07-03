import nltk
import pandas as pd

f = open('data\\fables.txt','r')
text = f.read()
fables = text.split('\n\n\n\n')
titles = []
bodies = []

def standard_body(body):
	tmp = body.split(' ',2)
	body = ' '.join([w.capitalize() for w in tmp[0:1]]+[tmp[2]])
	body = body.replace('\n', ' ').replace("\'","'")
	return body

for story in fables:
	if '\n\n' in story:
		title,body = story.split('\n\n',1)
		title= title.replace('\n','')
		titles+=[title]
		bodies+=[standard_body(body)]
	else:
		titles+=['Unknown']
		bodies+=[standard_body(story)]
		
stories = pd.DataFrame({'title':titles,'body':bodies})

from nltk.tag.perceptron import PerceptronTagger
tagger = PerceptronTagger()

def madlib(title,body):
	sentences = [nltk.word_tokenize(sent) for sent in nltk.sent_tokenize(body)]
	tags = [[