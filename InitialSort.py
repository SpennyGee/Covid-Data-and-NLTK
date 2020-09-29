
import os, json
#import pandas as pd
import nltk
from nltk import FreqDist
from nltk.text import Text
from nltk.tokenize import word_tokenize


filename = 'noncomm_use_subset.tar.gz' 
file = "CORD-19-research-challenge.zip"
path = 'C:\\Users\\Spencer Gregory\\eclipse-workspace\\COVID DATA HANDLING\\2020-03-13\\noncomm_use_subset\\noncomm_use_subset.'



files = []
base_path = path

all_texts = []

for i in os.listdir(base_path):
    
    ab_text = []
    
    #if we have a new article, load it as a json and decode from unicode
    if i.endswith('.json'):
        full_path = '%s/%s' % (base_path, i)
        files.append((open(full_path, 'r', encoding='utf-8').read()))
        try:
            with open(full_path) as json_file:
                data = json.load(json_file) 
                
                for p in data['body_text']:
                    ab_text.append((p['text']))
                    
                text_string = ""
                for line in ab_text:
                    try:
                        
                        text_string += str(line)
                    except:
                        catch = True
                all_texts.append(text_string)
               
        except:
            print("hmm")
print(all_texts[3]) 
        #ab_text is a list containing each line of text from a given book.
for each in all_texts:
    
    try:
        text_list = word_tokenize(each)
        long_words = [w for w in text_list if len(w) > 10]
        text = Text(text_list)
        longies = Text(long_words)
        text_fd = FreqDist(longies)
        print(text_fd.most_common(20))
        text_fd.plot(cumulative = True)
        
        print(textList.concordance('viral'))
     
    except:
        breakcatch = True
        

#print(article_dsbt.most_common(50))
print(len(all_texts[3]))




