# # import numpy as np
# # from sklearn.feature_extraction.text import CountVectorizer
# # from sklearn.feature_extraction.text import TfidfTransformer
# # from sklearn.neighbors import KNeighborsClassifier
# # from sklearn.pipeline import Pipeline
# # from sklearn.datasets import fetch_20newsgroups
# # import pandas as pd
# #
# #
# # # We defined the categories which we want to classify
# # categories = ['rec.motorcycles', 'sci.electronics',
# #               'comp.graphics', 'sci.med']
# #
# # df = pd.read_csv("recipes.csv")
# #
# # category = df["category"][1]
# #
# # print(category)
# # # sklearn provides us with subset data for training and testing
# # train_data = fetch_20newsgroups(subset='train',
# #                                 categories=categories, shuffle=True, random_state=42)
# #
# # print(train_data.target_names)
# #
# # print("\n".join(train_data.data[0].split("\n")[:3]))
# # print(train_data.target_names[train_data.target[0]])
# #
# # # Let's look at categories of our first ten training data
# # for t in train_data.target[:10]:
# #     print(train_data.target_names[t])
#
#
#
#
# # ['comp.graphics', 'rec.motorcycles', 'sci.electronics', 'sci.med']
# # From: kreyling@lds.loral.com (Ed Kreyling 6966)
# # Subject: Sun-os and 8bit ASCII graphics
# # Organization: Loral Data Systems
# # comp.graphics
# # comp.graphics
# # comp.graphics
# # rec.motorcycles
# # comp.graphics
# # sci.med
# # sci.electronics
# # sci.electronics
# # comp.graphics
# # rec.motorcycles
# # sci.electronics
#
#
# # Builds a dictionary of features and transforms documents to feature vectors and convert our text documents to a
# # matrix of token counts (CountVectorizer)
# count_vect = CountVectorizer()
# X_train_counts = count_vect.fit_transform(train_data.data)
#
# # transform a count matrix to a normalized tf-idf representation (tf-idf transformer)
# tfidf_transformer = TfidfTransformer()
# X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
#
#
#
# knn = KNeighborsClassifier(n_neighbors=7)
#
# # training our classifier ; train_data.target will be having numbers assigned for each category in train data
# clf = knn.fit(X_train_tfidf, train_data.target)
#
# # Input Data to predict their classes of the given categories
# docs_new = ['I have a Harley Davidson and Yamaha.', 'I have a GTX 1050 GPU']
# # building up feature vector of our input
# X_new_counts = count_vect.transform(docs_new)
# # We call transform instead of fit_transform because it's already been fit
# X_new_tfidf = tfidf_transformer.transform(X_new_counts)
#
#
#
# # predicting the category of our input text: Will give out number for category
# predicted = clf.predict(X_new_tfidf)
#
# for doc, category in zip(docs_new, predicted):
#     print('%r => %s' % (doc, train_data.target_names[category]))
#
#
#
# # We can use Pipeline to add vectorizer -> transformer -> classifier all in a one compound classifier
# text_clf = Pipeline([
#     ('vect', CountVectorizer()),
#     ('tfidf', TfidfTransformer()),
#     ('clf', knn),
# ])
# # Fitting our train data to the pipeline
# text_clf.fit(train_data.data, train_data.target)
#
# # Test data
# test_data = fetch_20newsgroups(subset='test',
#                                categories=categories, shuffle=True, random_state=42)
# docs_test = test_data.data
# # Predicting our test data
# predicted = text_clf.predict(docs_test)
# print('We got an accuracy of',np.mean(predicted == test_data.target)*100, '% over the test data.')
#
#

import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import genesis
nltk.download('genesis')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
genesis_ic = wn.ic(genesis, False, 0.0)

import csv
import numpy as np
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords
from sklearn.metrics import roc_auc_score



class KNN_NLC_Classifer():
    def __init__(self, k=1, distance_type = 'path'):
        self.k = k
        self.distance_type = distance_type

    # This function is used for training
    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    # This function runs the K(1) nearest neighbour algorithm and
    # returns the label with closest match.
    def predict(self, x_test):
        self.x_test = x_test
        y_predict = []

        for i in range(len(x_test)):
            max_sim = 0
            max_index = 0
            for j in range(self.x_train.shape[0]):
                temp = self.document_similarity(x_test[i], self.x_train[j])
                if temp > max_sim:
                    max_sim = temp
                    max_index = j
            y_predict.append(self.y_train[max_index])
        return y_predict

    def convert_tag(self, tag):
        """Convert the tag given by nltk.pos_tag to the tag used by wordnet.synsets"""
        tag_dict = {'N': 'n', 'J': 'a', 'R': 'r', 'V': 'v'}
        try:
            return tag_dict[tag[0]]
        except KeyError:
            return None

    def doc_to_synsets(self, doc):
        """
            Returns a list of synsets in document.
            Tokenizes and tags the words in the document doc.
            Then finds the first synset for each word/tag combination.
        If a synset is not found for that combination it is skipped.

        Args:
            doc: string to be converted

        Returns:
            list of synsets
        """
        tokens = word_tokenize(doc + ' ')

        l = []
        tags = nltk.pos_tag([tokens[0] + ' ']) if len(tokens) == 1 else nltk.pos_tag(tokens)

        for token, tag in zip(tokens, tags):
            syntag = self.convert_tag(tag[1])
            syns = wn.synsets(token, syntag)
            if (len(syns) > 0):
                l.append(syns[0])
        return l

    def similarity_score(self, s1, s2, distance_type='path'):
        """
        Calculate the normalized similarity score of s1 onto s2
        For each synset in s1, finds the synset in s2 with the largest similarity value.
        Sum of all of the largest similarity values and normalize this value by dividing it by the
        number of largest similarity values found.

        Args:
            s1, s2: list of synsets from doc_to_synsets

        Returns:
            normalized similarity score of s1 onto s2
        """
        s1_largest_scores = []

        for i, s1_synset in enumerate(s1, 0):
            max_score = 0
            for s2_synset in s2:
                if distance_type == 'path':
                    score = s1_synset.path_similarity(s2_synset, simulate_root=False)
                else:
                    score = s1_synset.wup_similarity(s2_synset)
                if score != None:
                    if score > max_score:
                        max_score = score

            if max_score != 0:
                s1_largest_scores.append(max_score)

        mean_score = np.mean(s1_largest_scores)

        return mean_score


#score = s1_synset.jcn_similarity(s2_synset, genesis_ic)
  #score = s1_synset.jcn_similarity(s2_synset, brown_ic)
  #score = s1_synset.lin_similarity(s2_synset, semcor_ic)
  #score = s1_synset.res_similarity(s2_synset, genesis_ic)
  #score = s1_synset.res_similarity(s2_synset, brown_ic)
  #score = s1_synset.wup_similarity(s2_synset)
  #score = s1_synset.lch_similarity(s2_synset)
  #score = s1_synset.wup_similarity(s2_synset)#

    def document_similarity(self, doc1, doc2):
        """Finds the symmetrical similarity between doc1 and doc2"""

        synsets1 = self.doc_to_synsets(doc1)
        synsets2 = self.doc_to_synsets(doc2)

        return (self.similarity_score(synsets1, synsets2) + self.similarity_score(synsets2, synsets1)) / 2
doc1 = 'I like rains'
doc2 = 'I like showers'
x = KNN_NLC_Classifer()
print("Test Similarity Score: ", x.document_similarity(doc1, doc2))




# 1. Importing the dataset
#we'll use the demo dataset available at Watson NLC Classifier Demo.
# FILENAME = "https://raw.githubusercontent.com/watson-developer-cloud/natural-language-classifier-nodejs/master/training/weather_data_train.csv"
FILENAME = "recipes.csv"


dataset = pd.read_csv(FILENAME, header = None)

dataset.rename(columns = {2:'text', 8:'answer'}, inplace=True)

dataset['output'] = np.where(dataset['answer'] == 'category', 1,0)
Num_Words = dataset.shape[0]

print(dataset.head())
print("\nSize of input file is ", dataset.shape)




import re
nltk.download('stopwords')
s = stopwords.words('english')
#add additional stop words
s.extend(['today', 'tomorrow', 'outside', 'out', 'there'])
ps = nltk.wordnet.WordNetLemmatizer()
for i in range(dataset.shape[0]):
    review = re.sub('[^a-zA-Z]', ' ', dataset.iloc[i, 2])
    review = review.lower()
    review = review.split()
    review = [ps.lemmatize(word) for word in review if not word in s]
    review = ' '.join(review)
    dataset.loc[i, 'text'] = review
X_train = dataset['text']
y_train = dataset['output']
print("Below is the sample of training text after removing the stop words")
print(dataset['text'][:10])

# 4. Train the Classifier
classifier = KNN_NLC_Classifer(k=1, distance_type='path')
classifier.fit(X_train, y_train)

final_test_list = ['Almond lentil stew', 'Chicken tikka masala', 'Albanian baked lamb with rice', 'Baked salmon with chorizo rice', 'Chicken and coconut curry']

test_corpus = []
for i in range(len(final_test_list)):
    review = re.sub('[^a-zA-Z]', ' ', final_test_list[i])
    review = review.lower()
    review = review.split()

    review = [ps.lemmatize(word) for word in review if not word in s]
    review = ' '.join(review)
    test_corpus.append(review)

y_pred_final = classifier.predict(test_corpus)

output_df = pd.DataFrame(data={'text': final_test_list, 'code': y_pred_final})
output_df['answer'] = np.where(output_df['code'] == 1, 'category', 'food')
print(output_df)