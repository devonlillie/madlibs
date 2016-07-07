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

## Import stories into list and store as dataframe
for story in fables:
	if '\n\n' in story:
		title,body = story.split('\n\n',1)
		title= title.replace('\n','')
		titles+=[title]
		bodies+=[standard_body(body)]
	else:
		titles+=['Unknown']
		bodies+=[standard_body(story)]
		
### -------------------------- ###
#      Tokenize and tag text     #
### -------------------------- ###
stories = pd.DataFrame({'title':titles,'body':bodies})
stories['sents'] = stories['body'].map(lambda x: nltk.sent_tokenize(x))
stories['words'] = stories['sents'].map(lambda x: [[w.lower() for w in nltk.word_tokenize(s)] for s in x])

from nltk.tag.perceptron import PerceptronTagger
tagger = PerceptronTagger()
stories['tags'] = stories['words'].map(lambda x: [tagger.tag(s) for s in x])

### -------------------------- ###
#  Categorize tags into genres   #
### -------------------------- ###
# Note: Standards replace 'TG' with '{CLASS}' i.e. 'NN' -> '{ANML}'
""" Genres:
 - occupation
 - animals: is_animal
 - body parts: 
 - exclamation
 - food
 - location
"""
is_animal = lambda x: is_hyper_of(x,'animal')
is_bodypart = lambda x: is_hyper_of(x,'body_part')

stories['tags'] = stories['tags'].map(lambda x: replace_tags(x,'ANML','NN',is_animal))
stories['tags'] = stories['tags'].map(lambda x: replace_tags(x,'BPRT','NN',is_bodypart))

animals = find_tags(stories.loc[0,'tags'],'{ANML}')
all_parts =[]
for i in stories.index:
	all_parts += set(find_tags(stories.loc[i,'tags'],'{BPRT}'))

## NEXT : match tags by starting with to catch NNS and NN

	