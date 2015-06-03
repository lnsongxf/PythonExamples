#=============================================================================
# purpose: example of the use of k-means clustering on text data
# author: tirthankar chakravarty
# created:
# revised:
# comments: based on the example in Richert & Coelho (2013), "Building Machine Learning
#      Systems with Python" 1e, Chapter 3.
#=============================================================================

from sklearn.feature_extraction.text import TfidfVectorizer
import sklearn.cluster as sklc
import os
import nltk
import pandas as pd

# create data directory
data_directory = 'Data/richert_coelho2013'
if not os.path.exists(data_directory):
    os.mkdir(data_directory)

# create dummy text data files
with open(os.path.join(data_directory, '1.txt'), 'w') as dummy_data_1, \
    open(os.path.join(data_directory, '2.txt'), 'w') as dummy_data_2, \
    open(os.path.join(data_directory, '3.txt'), 'w') as dummy_data_3, \
    open(os.path.join(data_directory, '4.txt'), 'w') as dummy_data_4, \
    open(os.path.join(data_directory, '5.txt'), 'w') as dummy_data_5:
    dummy_data_1.write('This is a toy post about machine learning.\n Actually, it contains not much interesting stuff')
    dummy_data_2.write('Imaging databases can get huge.')
    dummy_data_3.write('Most imaging databases save images permanently.')
    dummy_data_4.write('Imaging databases store images.')
    dummy_data_5.write('Imaging databases store images.\n Imaging databases store images.\n Imaging databases store images.')

# read in all the files as a list of documents
files = [os.path.join(data_directory, '%s.txt' % filenum) for filenum in range(1, 6)]
documents = [open(filename, 'r').read() for filename in files]

# write a custom TfidfVectorizer to add stemming as a pre-processing step
english_stemmer = nltk.stem.SnowballStemmer('english')
class StemmedCountVectorizer(TfidfVectorizer):
    def build_analyzer(self):
        analyser = super(StemmedCountVectorizer, self).build_analyzer()
        return(lambda document: (english_stemmer.stem(w) for w in analyser(document)))

# pass the documents to the vectorizer, and compute the TF-IDF DTM
vectorizer = StemmedCountVectorizer(min_df=1, stop_words='english')
tfidf_images = vectorizer.fit_transform(documents)
# vectorizer.get_feature_names()

# fit k-means (10 random starts)
sklc_images = sklc.KMeans(n_clusters=3, max_iter=100)
nda_tfidf_images = tfidf_images.toarray()  # conver to ndarray to pass to KMeans.fit()
sklc_images_fit = {i: sklc_images.fit(nda_tfidf_images).labels_ for i in range(1, 11)}
df_sklc_images_labels = pd.DataFrame(sklc_images_fit)  # check the concordance in lables across random starts



