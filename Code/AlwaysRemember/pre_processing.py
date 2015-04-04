import pickle, re
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from gensim import corpora, models, similarities


def tokenize_doc(doc):
        tokenizer = RegexpTokenizer('\s+', gaps=True)
        doc = doc.lower()
        doc = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",doc).split())
        tokens = tokenizer.tokenize(doc)
        return(tokens)


def rem_stopwords(tokens):
        english_stops = list(stopwords.words('english'))
        token_rem_stop = [token for token in tokens if token not in english_stops]
        return(token_rem_stop)

def token_stemming(tokens):
        stemmer = PorterStemmer()
        stem_tokens = [stemmer.stem(token) for token in tokens]
        return(stem_tokens)

def token_lemmatize(tokens):
        #Importing WordNet Lemmatizer
        lemmatizer = WordNetLemmatizer()
        token_lemmatized = [lemmatizer.lemmatize(token) for token in tokens]
        return(tokens_lemmatized)

def pre_process(doc):
        tokens = tokenize_doc(doc)
        tokens = rem_stopwords(tokens)
        tokens = token_stemming(tokens)
        return(tokens)

def build_corpus(merge_file,dict_file,corp_file):
        dictionary = corpora.Dictionary(doc.split() for doc in open(merge_file))
        dictionary.save(dict_file)
        corpus = [dictionary.doc2bow(line.split()) for line in open(merge_file)]
        corpora.MmCorpus.serialize(corp_file,corpus)

