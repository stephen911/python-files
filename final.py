import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from collections import Counter
import math
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report



# Question 1
df = pd.read_csv("recipes.csv")

#identifying missing data and cleaning
cuisine = df['cuisine'].replace(r'^\s*$', np.nan, regex=True)

# showing summary statistics
print(df[["rating_avg", "rating_val"]].describe())

# displaying 10 highest rated recipes
print("\n")
print(df.nlargest(10, 'rating_avg')["title"])
print("\n")
print(df.nlargest(10, 'rating_val')["title"])

# Question 2
# visualizing data
df.plot(x="rating_avg", y=["rating_val"], kind="scatter",)
# df.plot(x="rating_avg", y=["rating_val"])
plt.show()

# commenting of relationship or rating_val and rating_avg
print("\n")
print("The higher the rating_val the lower the rating_avg")
print("The threshold i suggest is 3 since 25% of rating_val is 3.\nTherefore any rating_val below or equal to 3 can be considered not significant")

print("\n")
# Question 3
features=['title','rating_avg','rating_val','total_time','category','cuisine', 'ingredients']


combined_features = []


for i in df.index:
    fresh = df.loc[i, features].values.flatten().tolist()
    new = " ".join(str(x) for x in fresh)
    combined_features.append(new)


# adding combine features to dataframe
df['combine_features'] = combined_features


# Defining vec_space_method
def vec_space_method(recipe_query):
    document = df["combine_features"]
    # print(document)


    #using the countVectorizer class
    # Create a Vectorizer Object
    vectorizer = CountVectorizer()

    vectorizer.fit(document)

    # Printing the identified Unique words along with their indices
    # print("Vocabulary: ", vectorizer.vocabulary_)

    # Encode the Document
    vector = vectorizer.transform(document)
    # print(vector)



    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(document)
    # print(vectorizer.get_feature_names())
    # print(X.shape)

    vector = X
    df1 = pd.DataFrame(vector.toarray(), columns=vectorizer.get_feature_names())
    # print(df1)


    nltk.download('punkt')
    nltk.download('stopwords')


    # print(stopwords.words('english'))
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
    # print("WORD TOKENS:")
    # print(tokens)
    doc_text = remove_stopwords(tokens)
    # print("\nAFTER REMOVING STOPWORDS:")
    # print(doc_text)
    # print("\nAFTER PERFORMING THE WORD STEMMING::")
    doc_text = word_stemmer(doc_text)
    # print(doc_text)


    doc_ = ' '.join(doc_text)
    # print(doc_)

    cleaned_document = []
    for doc in document:
      tokens = get_tokenized_list(doc)
      doc_text = remove_stopwords(tokens)
      doc_text  = word_stemmer(doc_text)
      doc_text = ' '.join(doc_text)
      cleaned_document.append(doc_text)
    # print(cleaned_document)


    vectorizerX = TfidfVectorizer()
    vectorizerX.fit(cleaned_document)
    doc_vector = vectorizerX.transform(cleaned_document)
    # print(vectorizerX.get_feature_names())

    # print(doc_vector.shape)



    df1 = pd.DataFrame(doc_vector.toarray(), columns=vectorizerX.get_feature_names())
    # print(df1)
    query = recipe_query
    query = get_tokenized_list(query)
    query = remove_stopwords(query)
    q = []
    for w in word_stemmer(query):
        q.append(w)
    q = ' '.join(q)
    query_vector = vectorizerX.transform([q])

    # calculate cosine similarities
    cosineSimilarities = cosine_similarity(doc_vector, query_vector).flatten()

    related_docs_indices = cosineSimilarities.argsort()[:-11:-1]

    return related_docs_indices


# Question 3(c)
# Use the vector space method using a matrix-vector product to show the first 10 recipe recommendations for a user who has liked that particular recipe
print("Title of recommended recipes using vector space method")
recipe= "Almond lentil stew"
recipe_list = vec_space_method(recipe)
for i, index in enumerate(recipe_list):
    print(i+1, df.loc[index]["title"])






# defining most_popular function
def most_popular():
    #getting random recipe
    df_elements = df.sample(n=1)
    fres = df.loc[df_elements.index, "title"].values.flatten().tolist()
    Str = ' '.join([str(elem) for elem in fres])
    related_docs_indices = vec_space_method(Str)

    # sorting rating_val and displaying in descending order
    for i, index in enumerate(related_docs_indices):
        for j in range(i + 1, len(related_docs_indices)):

            if df.loc[index]["rating_avg"] < df.loc[j]["rating_avg"]:
                temp = related_docs_indices[i]
                related_docs_indices[i] = related_docs_indices[j]
                related_docs_indices[j] = temp

    print("10 most highly rated recipes\n")
    for i, index in enumerate(related_docs_indices):
        print(i+1, df.loc[index]["title"])


    return Str


most_popular()




def knn(data, query, k, distance_fn, choice_fn):
    neighbor_distances_and_indices = []

    # 3. For each example in the data
    for index, example in enumerate(data):
        # 3.1 Calculate the distance between the query example and the current
        # example from the data.
        distance = distance_fn(example[:-1], query)

        # 3.2 Add the distance and the index of the example to an ordered collection
        neighbor_distances_and_indices.append((distance, index))

    # 4. Sort the ordered collection of distances and indices from
    # smallest to largest (in ascending order) by the distances
    sorted_neighbor_distances_and_indices = sorted(neighbor_distances_and_indices)

    # 5. Pick the first K entries from the sorted collection
    k_nearest_distances_and_indices = sorted_neighbor_distances_and_indices[:k]

    # 6. Get the labels of the selected K entries
    k_nearest_labels = [data[i][-1] for distance, i in k_nearest_distances_and_indices]

    # 7. If regression (choice_fn = mean), return the average of the K labels
    # 8. If classification (choice_fn = mode), return the mode of the K labels
    return k_nearest_distances_and_indices, choice_fn(k_nearest_labels)


def mean(labels):
    return sum(labels) / len(labels)


def mode(labels):
    return Counter(labels).most_common(1)[0][0]


def euclidean_distance(point1, point2):
    sum_squared_distance = 0
    for i in range(len(point1)):
        sum_squared_distance += math.pow(point1[i] - point2[i], 2)
    return math.sqrt(sum_squared_distance)


def main():
    reg_data = [
        [65.75, 112.99],
        [71.52, 136.49],
        [69.40, 153.03],
        [68.22, 142.34],
        [67.79, 144.30],
        [68.70, 123.30],
        [69.80, 141.49],
        [70.01, 136.46],
        [67.90, 112.37],
        [66.49, 127.45],
    ]


    reg_query = [60]
    reg_k_nearest_neighbors, reg_prediction = knn(
        reg_data, reg_query, k=3, distance_fn=euclidean_distance, choice_fn=mean
    )


    clf_data = [
        [22, 1],
        [23, 1],
        [21, 1],
        [18, 1],
        [19, 1],
        [25, 0],
        [27, 0],
        [29, 0],
        [31, 0],
        [45, 0],
    ]

    clf_query = [33]
    clf_k_nearest_neighbors, clf_prediction = knn(
        clf_data, clf_query, k=3, distance_fn=euclidean_distance, choice_fn=mode
    )



def knn_similarity(recipe_query, k_recommendations):
    raw_recipe_data = []
    with open('recipes.csv', 'r', encoding="utf8") as md:



        next(md)


        # Read the data into memory
        for line in md.readlines():
            data_row = line.strip().split(',')
            raw_recipe_data.append(data_row)


    # Prepare the data for use in the knn algorithm by picking
    # the relevant columns and converting the numeric columns
    # to numbers since they were read in as strings
    recipe_recommendation_data = []
    for i in df.index:

        try:
            data_row = list(map(float, df.loc[i, ["rating_avg", "rating_val", "total_time"]].values.flatten()))
            recipe_recommendation_data.append(data_row)
        except Exception as e:
            print(e)

    # Use the KNN algorithm to get the 10 recipes that are most
    # similar to The list of recipes.
    recommendation_indices, _ = knn(
        recipe_recommendation_data, recipe_query, k=k_recommendations,
        distance_fn=euclidean_distance, choice_fn=lambda x: None
    )

    recipe_recommendations = []
    for i, index in recommendation_indices:
        # print(i)
        # print(i, index)
        recipe_recommendations.append(raw_recipe_data[index])

    return recipe_recommendations


recipe_data = [7, 1619, 2430, 1618, 1613, 2334, 1615, 1612, 1306]  # feature vector for The Post
recommended_recipe = knn_similarity(recipe_query=recipe_data, k_recommendations=10)

# Print recommended recipes

print("\nKnn similarity recommendation")
for recommendation in recommended_recipe:
    print(recommendation[2])


#this is an alternative implemention of the knn similarity algorithm you can try and test how it works
# def knn_similarity_alt():
#     X = df.iloc[:, 2].values
#     y = df.iloc[:, 8].values
#
#     X = pd.get_dummies(X)
#
#     X = X.values
#
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)
#
#
#     scaler = StandardScaler()
#     scaler.fit(X_train)
#
#     X_train = scaler.transform(X_train)
#     X_test = scaler.transform(X_test)
#
#
#     classifier = KNeighborsClassifier(n_neighbors=5, weights="uniform", algorithm="kd_tree", leaf_size=30, p=2, metric="minkowski",n_jobs=-1)
#     classifier.fit(X_train, y_train)
#
#     y_pred = classifier.predict(X_test)
#
#
#     # print(confusion_matrix(y_test, y_pred))
#     print(classification_report(y_test, y_pred))




#Implementing it with most_popular function
user_1 = "Chicken tikka masala"


user_1_list = vec_space_method(user_1)
print("vector space method user 1")
for i, index in enumerate(user_1_list):
    print(i+1, df.loc[index]["title"])
print("\n")
user_2 = "Albanian baked lamb with rice"
user_2_list = vec_space_method(user_2)
print("vector space method user 2")
for i, index in enumerate(user_2_list):
    print(i+1, df.loc[index]["title"])
print("\n")
user_3 = "Baked salmon with chorizo rice"
user_3_list = vec_space_method(user_3)
print("vector space method user 3")
for i, index in enumerate(user_3_list):
    print(i+1, df.loc[index]["title"])
print("\n")
user_4 = "Chicken and coconut curry"
user_4_list = vec_space_method(user_4)
print("vector space method user 4")
for i, index in enumerate(user_4_list):
    print(i+1, df.loc[index]["title"])
print("\n")






knn_user_1 = [ 563, 3256,  963,  564, 2933,  562, 2303, 2497, 3217,  509] # feature vector for The Post
recommended_recipe = knn_similarity(recipe_query=knn_user_1, k_recommendations=10)
print("\nKnn similarity recommendation user 1")
for recommendation in recommended_recipe:
    print(recommendation[2])
print("\n")

knn_user_2 = [   3, 1549, 1543, 1305, 1536, 1556, 2859, 1532, 1535, 1818] # feature vector for The Post
recommended_recipe = knn_similarity(recipe_query=knn_user_2, k_recommendations=10)
print("\nKnn similarity recommendation user 2")
for recommendation in recommended_recipe:
    print(recommendation[2])
print("\n")



knn_user_3 = [ 102,  473,  703,  427,   92,  704,  295, 2309, 3151, 2403]# feature vector for The Post
recommended_recipe = knn_similarity(recipe_query=knn_user_3, k_recommendations=10)
print("\nKnn similarity recommendation user 3")
for recommendation in recommended_recipe:
    print(recommendation[2])
print("\n")



knn_user_4 = [ 476,  508, 1477, 1570,  775,  507, 2198,  463, 2497,  782]# feature vector for The Post
recommended_recipe = knn_similarity(recipe_query=knn_user_4, k_recommendations=10)
print("\nKnn similarity recommendation user 4")
for recommendation in recommended_recipe:
    print(recommendation[2])




