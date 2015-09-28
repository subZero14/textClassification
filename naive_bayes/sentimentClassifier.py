# Assuming you already have nltk setup on your system, you just need to do "sudo pip # install sentiment_classifier" and run this program using python2.7.

import nltk
from senti_classifier import senti_classifier
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
import sys
# from sentiwordnet import SentiWordNetCorpusReader, SentiSynset

word = sys.argv[1] #"amazing" # replace this with the word you want

sentences = [word] # check polarity for exact word
pos_score, neg_score = senti_classifier.polarity_scores(sentences)
print("For:", sentences)
print ("Positive_Score: ", pos_score, "Negative Score: ", neg_score) 

synonym = ""
count = 0 # reference. 
  
# if neutral polarity then do:  
if (pos_score == 0 and neg_score == 0) or (neg_score == 0 and pos_score == 0):
    # print("We are where we are not supposed to be")
    for ss in wn.synsets(word): # Each synset represents a diff concept.
        # print ss.definition(); # print ss.pos(); Uncomment if you want to check the available contexts in wordnet
        print("Synset_", count)  
        if ss.pos() == 's': # s indicates adjective, since we're only considering adjectives
            # print(ss.lemmas()) lemmas give the synonyms for each synset, in a particular format eg: great.01.b.great but we need just the name
            for a in ss.lemmas():
                # print a.name() a.name gives you the name of the synonym          
                if str(a.name()) != word: # sometimes you get the same word, if not then break.
                    synonym = a.name()
                    break
                    
            if synonym != "": # found synonym, calculate polarity
                sentences = [synonym]
                pos_score, neg_score = senti_classifier.polarity_scores(sentences)
                print ("For synonym: ", synonym)
                print ("Positive_Score: ", pos_score, "Negative Score: ", neg_score)                                     
                if pos_score > 0 or neg_score > 0: # if synonym is not neutral break, else move on to next lemma.
                    print ("Positive_Score: ", pos_score, "Negative Score: ", neg_score)                     
                    break
                                   
        count += 1;
