from sklearn.cluster import KMeans
import sklearn.datasets as skld
import zipfile
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.snowball import SnowballStemmer
import sklearn.metrics as sklm
import numpy as np

dir_newsgroups = 'Data/20newsgroups'
data_20newsgroups = skld.fetch_20newsgroups(data_home=dir_newsgroups, subset='all')

# NOTE: this dataset has to be manually downloaded from: http://mlcomp.org/datasets/379
#   mlcomp.org requires free registration
zipname_20news = 'Archive/dataset-379-20news-18828_OLBVH.zip'
if zipfile.is_zipfile(zipname_20news):
    zip_20news = zipfile.ZipFile(zipname_20news)
    zip_20news.extractall(path='Data/20newsgroups')
data_20newsgroups_train = skld.load_mlcomp('20news-18828', mlcomp_root=dir_newsgroups, set_="train")
data_20newsgroups_test = skld.load_mlcomp('20news-18828', mlcomp_root=dir_newsgroups, set_="test")
data_20newsgroups = data_20newsgroups_train.data + data_20newsgroups_test.data
targets_20newsgroup = np.append(data_20newsgroups_train.target,
                                data_20newsgroups_test.target)

# create a derived Vectorizer class that includes stemming as preprocessing
english_stemmer = SnowballStemmer(language='english')
class StemmedTfidfVectorizer(TfidfVectorizer):
    def build_analyzer(self):
        analyser = super(TfidfVectorizer, self).build_analyzer()
        return(lambda document: (english_stemmer.stem(word) for word in analyser(document)))

# get the DTM as coo_matrix
vectoriser_20news = StemmedTfidfVectorizer(min_df=10, max_df=0.5, stop_words='english', decode_error='ignore')
vectors_20news = vectoriser_20news.fit_transform(data_20newsgroups)

# fit a KMeans model to the data
kmeans_20news = KMeans(n_clusters=20, verbose=True)
kmeans_20news_fit = kmeans_20news.fit(vectors_20news)

# compute the clustering metrics
sklm.cluster.homogeneity_completeness_v_measure(targets_20newsgroup, kmeans_20news_fit.labels_)

# test the prediction on a new document
new_data = '''
Disk drive problems. Hi, I have a problem with my hard disk. After 1 year it is working only sporadically now.
I tried to format it, but now it does not boot any more. Any ideas? Thanks.
'''
new_data_cluster = kmeans_20news_fit.predict(vectoriser_20news.transform([new_data]))

# what are some of the other documents in the same cluster?
np.mean(targets_20newsgroup == new_data_cluster)*100
idx_20news_cluster19 = (targets_20newsgroup == new_data_cluster)
data_20newsgroups_cluster19 = np.take(data_20newsgroups, idx_20news_cluster19.nonzero())

# what are the effective keywords for the new document?
np.take(vectoriser_20news.get_feature_names(),
        vectoriser_20news.transform([new_data]).toarray().nonzero()[1])


