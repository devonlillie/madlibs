import nltk
import pandas as pd
import numpy as np
from helper_functions import *
from parse_functions import *

f = open('data\\fables.txt','r')
text = f.read()
fables = text.split('\n\n\n\n')
titles = []
bodies = []

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

stories['sents'] = stories['body'].map(lambda x: 
		[nltk.word_tokenize(sent) for sent in nltk.sent_tokenize(x)])

from nltk.tag.perceptron import PerceptronTagger
tagger = PerceptronTagger()
from nltk.corpus import wordnet as wn
	
all_nouns = pd.DataFrame()
for i in range(len(stories)):
	story = stories.iloc[i]
	tags = tag_text(story['title'],story['sents'],tagger)
	nouns = tags.loc[tags['tag']=='NN',['word']]
	nouns['animal'] = nouns['word'].map(lambda x: is_animal(x))
	all_nouns = all_nouns.append(nouns)
	
	