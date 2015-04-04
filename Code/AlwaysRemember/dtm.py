from gensim import corpora, models 
from csv import reader as csvr
from collections import Counter
import datetime
import importlib as il
import gensim

import pre_processing as pp

doc_file = "Code/AlwaysRemember/data/docs.csv"
date_file = "Code/AlwaysRemember/data/pub_date.csv"

docs = []
pub_date = []
with open(doc_file,'rt') as f:
        records = csvr(f,delimiter=",")
        for record in records:
                docs += record

with open(date_file,'rt') as f:
        records = csvr(f,delimiter=",")
        for record in records:
                pub_date += record

#Removing the empty articles, pre-processing them and converting pub_date to datetime
docs_str = [" ".join(pre_process(item)) for item in docs if item != '']
pub_date = [datetime.datetime.strptime(pub_date[i],"%Y-%m-%d").date() for i,item in enumerate(docs) if item != '']

#sorting the articles according date of publish
pub_date_so = sorted(pub_date)
docs_str = [doc for (doc,date) in sorted(zip(docs_str,pub_date_so))]

#Building the dictionary and corpora for the articles
obama_dict = corpora.Dictionary(item.split() for item in docs_str)
obama_corp = [obama_dict.doc2bow(item.split()) for item in docs_str]
tfidf = models.TfidfModel(obama_corp)
obama_tfidf = tfidf[obama_corp]

model = gensim.models.DtmModel("/home/tirthankar/Projects/TextAnalytics/Code/dtm_release/dtm/main",
                        obama_tfidf,
                        Counter(pub_date).values(),
                        num_topics=15,
                        id2word=obama_dict,
                        prefix="/home/tirthankar/JUNK/")
