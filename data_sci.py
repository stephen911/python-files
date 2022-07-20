import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from knn_model import knn, euclidean_distance
from sklearn.metrics import confusion_matrix


import nltk

from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import csv
df = pd.read_csv("recipes.csv")
# df.drop(columns"cuisine", inplace=True, axis=1)
# extr = df['cuisine'].str.extract(r'', expand=False)
cuisine = df['cuisine'].replace(r'^\s*$', np.nan, regex=True)
print(df[["rating_avg", "rating_val"]].describe())
print(df.nlargest(10, 'rating_avg'))
print(df.nlargest(10, 'rating_val'))

#
# df.plot(x="title", y=["rating_avg", "rating_val"])

df.plot(x="rating_avg", y=["rating_val"], kind="scatter",)
# df.plot(x="rating_avg", y=["rating_val"])
# plt.show()


print("the higher the rating_val the lower the rating_avg")
print("the threshold i suggest is 3 since 25% of rating_val is 3. therefore any rating_val below or equal to 3 can be considered not significant")

# Declare a list that is to be converted into a column
features=['title','rating_avg','rating_val','total_time','category','cuisine', 'ingredients']


# dfi = df.set_index('id')
# dfi.ix[features].tolist()
combined_features = []
count = 0
for i in df.index:
    fresh = df.loc[i, features].values.flatten().tolist()
    new = " ".join(str(x) for x in fresh)
    combined_features.append(new)
    count += 1

print(count)









# Using 'Address' as the column name
# and equating it to the list
df['combine_features'] = combined_features



# document = ["One Geek helps Two Geeks",
#             "Two Geeks help Four Geeks",
#             "Each Geek helps many other Geeks at GeeksforGeeks"]




def vec_space_method(recipe):
    document = df["combine_features"]

    # Create a Vectorizer Object
    vectorizer = CountVectorizer()

    vectorizer.fit(document)

    # Printing the identified Unique words along with their indices
    print("Vocabulary: ", vectorizer.vocabulary_)

    # Encode the Document
    vector = vectorizer.transform(document)
    print(vector)

    # Summarizing the Encoded Texts
    # print("Encoded Document is:")
    # vec = vector.toarray()
    # print(vector.toarray())



    # df = pd.DataFrame(np.random.randint(0, 2, (3, 5)))
    #
    # df
    # ##     0  1  2  3  4
    # ##  0  1  1  1  0  0
    # ##  1  0  0  1  1  1
    # ##  2  0  1  0  1  0
    #
    # print(cosine_similarity(vec))


    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(document)
    print(vectorizer.get_feature_names())
    # ['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third', 'this']
    print(X.shape)

    vector = X
    df1 = pd.DataFrame(vector.toarray(), columns=vectorizer.get_feature_names())
    print(df1)


    nltk.download('punkt')
    nltk.download('stopwords')


    print(stopwords.words('english'))
    stop_words = set(stopwords.words('english'))


    def get_tokenized_list(doc_text):
        tokens = nltk.word_tokenize(doc_text)
        return tokens

    # This function will performing stemming on tokenized words
    def word_stemmer(token_list):
      ps = nltk.stem.PorterStemmer()
      stemmed = []
      for words in token_list:
        stemmed.append(ps.stem(words))
      return stemmed

    # Function to remove stopwords from tokenized word list
    def remove_stopwords(doc_text):
      cleaned_text = []
      for words in doc_text:
        if words not in stop_words:
          cleaned_text.append(words)
      return cleaned_text


    #Check for single document
    tokens = get_tokenized_list(document[1])
    print("WORD TOKENS:")
    print(tokens)
    doc_text = remove_stopwords(tokens)
    print("\nAFTER REMOVING STOPWORDS:")
    print(doc_text)
    print("\nAFTER PERFORMING THE WORD STEMMING::")
    doc_text = word_stemmer(doc_text)
    print(doc_text)


    doc_ = ' '.join(doc_text)
    print(doc_)

    cleaned_document = []
    for doc in document:
      tokens = get_tokenized_list(doc)
      doc_text = remove_stopwords(tokens)
      doc_text  = word_stemmer(doc_text)
      doc_text = ' '.join(doc_text)
      cleaned_document.append(doc_text)
    print(cleaned_document)


    vectorizerX = TfidfVectorizer()
    vectorizerX.fit(cleaned_document)
    doc_vector = vectorizerX.transform(cleaned_document)
    print(vectorizerX.get_feature_names())

    print(doc_vector.shape)



    df1 = pd.DataFrame(doc_vector.toarray(), columns=vectorizerX.get_feature_names())
    print(df1)

    query = recipe
    query = get_tokenized_list(query)
    query = remove_stopwords(query)
    q = []
    for w in word_stemmer(query):
        q.append(w)
    q = ' '.join(q)
    print(q)
    query_vector = vectorizerX.transform([q])

    # calculate cosine similarities
    cosineSimilarities = cosine_similarity(doc_vector, query_vector).flatten()

    related_docs_indices = cosineSimilarities.argsort()[:-10:-1]
    print("mmmmm")
    print(related_docs_indices)
    print("mmmmm")
    return  related_docs_indices
    # Initialize array
    # arr = related_docs_indices
    # temp = 0;
    #
    # # Displaying elements of original array
    # # print("Elements of original array: ");
    # for i in range(0, len(arr)):
    #     print(arr[i]),
    #
    #     # Sort the array in descending order
    # for i in range(0, len(arr)):
    #     for j in range(i + 1, len(arr)):
    #         if (arr[i] < arr[j]):
    #             temp = arr[i];
    #             arr[i] = arr[j];
    #             arr[j] = temp;
    #
    #
    #
    # # Displaying elements of array after sorting
    # # print("Elements of array sorted in descending order: ");
    # for i in range(0, len(arr)):
    #     print(arr[i]),


    # rating = []
    # arr = []
    # for i, index in enumerate(related_docs_indices):
    #     print(i, index)
    #
    #     for j in range(i + 1, len(related_docs_indices)):
    #         if (df.loc[index]["rating_avg"] < df.loc[j]["rating_avg"]):
    #             temp = related_docs_indices[i]
    #             related_docs_indices[i] = related_docs_indices[j]
    #             related_docs_indices[j] = temp
    #
    #
    #
    #
    #
    #
    #
    # # for i in range(0, len(related_docs_indices)):
    # #     for j in range(i + 1, len(related_docs_indices)):
    # #         if (df.loc[i]["rating_avg"] < df.loc[i]["rating_avg"]):
    # #         # if (arr[i] < arr[j]):
    # #
    # #             temp = arr[i];
    # #             arr[i] = arr[j];
    # #             arr[j] = temp;
    #
    #
    #     # great = i
    #     # if df.loc[i]["rating_avg"] > next(df.loc[i]["rating_avg"]):
    #     #
    #     #     great = i
    #     #     arr.append(great)
    #     # else:
    #     #     great = next(i)
    #     #     arr.append(great)
    #
    #
    #
    #
    #
    #     print(df.loc[i]["title"])
    #     print(df.loc[i]["rating_avg"])
    #     rating.append(df.loc[i]["rating_avg"])
    #
    # for i in related_docs_indices:
    #     print(df.loc[i]["rating_avg"])
    #
    # print("nnnnnn")
    # print(related_docs_indices)
    #
    # output = sorted(rating, reverse=True, key=lambda x:float(x))
    # print(output)
    # print(arr)






recipe = "Almond lentil stew"
vec_space_method(recipe)

def most_popular():
    df_elements = df.sample(n=1)
    fres = df.loc[df_elements.index, "title"].values.flatten().tolist()
    Str = ' '.join([str(elem) for elem in fres])
    related_docs_indices = vec_space_method(Str)
    rating = []
    arr = []
    for i, index in enumerate(related_docs_indices):
        print(i, index)

        for j in range(i + 1, len(related_docs_indices)):
            if (df.loc[index]["rating_avg"] < df.loc[j]["rating_avg"]):
                temp = related_docs_indices[i]
                related_docs_indices[i] = related_docs_indices[j]
                related_docs_indices[j] = temp

        # for i in range(0, len(related_docs_indices)):
        #     for j in range(i + 1, len(related_docs_indices)):
        #         if (df.loc[i]["rating_avg"] < df.loc[i]["rating_avg"]):
        #         # if (arr[i] < arr[j]):
        #
        #             temp = arr[i];
        #             arr[i] = arr[j];
        #             arr[j] = temp;

        # great = i
        # if df.loc[i]["rating_avg"] > next(df.loc[i]["rating_avg"]):
        #
        #     great = i
        #     arr.append(great)
        # else:
        #     great = next(i)
        #     arr.append(great)

        print(df.loc[i]["title"])
        print(df.loc[i]["rating_avg"])
        rating.append(df.loc[i]["rating_avg"])

    for i in related_docs_indices:
        print(df.loc[i]["rating_avg"])

    print("nnnnnn")
    print(related_docs_indices)

    output = sorted(rating, reverse=True, key=lambda x: float(x))
    print(output)
    print(arr)

    print("most popular")

    print(Str)
    return Str


most_popular()





def knn_similarity(recipe_query, k_recommendations):
    raw_recipe_data = []
    with open('recipes.csv', 'r', encoding="utf8") as md:
        # Discard the first line (headings)
        next(md)

        # Read the data into memory
        for line in md.readlines():
            data_row = line.strip().split(',')
            raw_recipe_data.append(data_row)

    # print(raw_movies_data)

    # Prepare the data for use in the knn algorithm by picking
    # the relevant columns and converting the numeric columns
    # to numbers since they were read in as strings
    recipe_recommendation_data = []
    for i in df.index:
        # fresh = df.loc[i, ["rating_avg"]].values.flatten().tolist()
        # print(fresh)
    # for row in raw_movies_data:
    #     print(df.loc[row.index]["rating_avg"])
        # print(row[6])
        try:
            # if row[6].startswith("https"):


            # print(row[6])
            data_row = list(map(float, df.loc[i, ["rating_avg", "rating_val", "total_time"]].values.flatten()))
            recipe_recommendation_data.append(data_row)
        except Exception as e:

            # print("im here")
            print(e)

    # Use the KNN algorithm to get the 5 movies that are most
    # similar to The Post.
    recommendation_indices, _ = knn(
        recipe_recommendation_data, recipe_query, k=k_recommendations,
        distance_fn=euclidean_distance, choice_fn=lambda x: None
    )

    recipe_recommendations = []
    for _, index in recommendation_indices:
        recipe_recommendations.append(raw_recipe_data[index])

    return recipe_recommendations

if __name__ == '__main__':
    the_post = [7, 1619, 2430, 1618, 1613, 2334, 1615, 1612, 1306]  # feature vector for The Post
    recommended_recipe = knn_similarity(recipe_query=the_post, k_recommendations=10)

    # Print recommended movie titles
    for recommendation in recommended_recipe:
        # print(df.loc[])
        print(recommendation[2])

    # Use the KNN algorithm to get the 5 movies that are most
    # similar to The Post.





# def get_query(recipe):
#     query = recipe
#     query = get_tokenized_list(query)
#     query = remove_stopwords(query)
#     q = []
#     for w in word_stemmer(query):
#       q.append(w)
#     q = ' '.join(q)
#     print(q)
#     query_vector = vectorizerX.transform([q])
#
#
#     # calculate cosine similarities
#     cosineSimilarities = cosine_similarity(doc_vector, query_vector).flatten()
#
#     related_docs_indices = cosineSimilarities.argsort()[:-10:-1]
#     print(related_docs_indices)
#
#
#
#     for i in related_docs_indices:
#         print(df.loc[i]["title"])
#         # print(i)
#         # print(cleaned_document)
#         # data = [cleaned_document[i]]
#         # print(data)
#         # print(type(data))
#
#
#     get_query('Almond lentil stew')
#
#     get_query(most_popular())
#



# x = []
# y = []
#
#
# with open('recipes.csv', 'r') as csvfile:
#     plots = csv.reader(csvfile, delimiter=',')
#
#     for index, row in enumerate(plots):
#         if index == 0:
#             pass
#         else:
#
#             x.append(row["rating_val"])
#             y.append(int(row["rating_avg"]))
#
# plt.bar(x, y, color='g', width=0.72, label="Age")
# plt.xlabel('Names')
# plt.ylabel('Ages')
# plt.title('Ages of different persons')
# plt.legend()
# plt.show()

# find maximum value of a
# single column 'x'
# find the maximum values of each row
# maxValues = df["rating_avg"].max(axis=1, skipna=False)
# print(maxValues)





# cuisine = df['cuisine'].fillna("None", inplace=True)
# print(cuisine.head(10))
# data_new1 = df.copy()
# data_new2 = data_new1.replace(r'^s*$', float('NaN'), regex=True)
# data_new2.to_csv("new.csv")

# making data frame from csv file
# data = pd.read_csv("recipes.csv")
# filling  null value using fillna() function
# data = df["cuisine"].fillna("None", inplace=True)

# print(data_new2)

# creating bool series True for NaN values
# bool_series = pd.notnull(data["cuisine"])

# filtering data
# displayind data only with Gender = Not NaN
# print(data[bool_series])
# print(df.head(5))



X = df.iloc[:, 2].values
y = df.iloc[:, 8].values

print(X)
print(y)

X = pd.get_dummies(X)

print(X)
# print(y)

X = X.values
print(X)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)



from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5, weights="uniform", algorithm="kd_tree", leaf_size=30, p=2, metric="minkowski",n_jobs=-1)
classifier.fit(X_train, y_train)

print("stephen")
print(X_test)

# x_pred = classifier.predict(X_test)
y_pred = classifier.predict(X_test)




from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


# import warnings
# warnings.filterwarnings('always')  # "error", "ignore", "always", "default", "module" or "once"
# metrics.f1_score(y_test, y_pred, average='weighted', labels=np.unique(y_pred))
# (_, _, f1, _) = metrics.precision_recall_fscore_support(y_test, y_pred,
#                                                         average='weighted',
#                                                         warn_for=tuple())







error = []

# Calculating error for K values between 1 and 40
for i in range(1, 40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error.append(np.mean(pred_i != y_test))



plt.figure(figsize=(12, 6))
plt.plot(range(1, 40), error, color='red', linestyle='dashed', marker='o',
         markerfacecolor='blue', markersize=10)
plt.title('Error Rate K Value')
plt.xlabel('K Value')
plt.ylabel('Mean Error')