from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import dill

# Data Pre-Processing

# load the dataset
df = pd.read_csv('../data/stars.csv')

# select top languages from dataset
df = df[df.language.isin(['Python', 'Jupyter Notebook', 'C++', 'Java', 'Go', 'JavaScript', 'C', 'HTML', 'CSS', 'TypeScript', 'C#', 'Kotlin', 'R', 'Ruby', 'Scala'])]
popular = pd.DataFrame(df['repo'].value_counts())

# repo having atleast 5 stars
select_repos = popular[popular['repo'] >= 5].index.tolist()
select_repos = select_repos[1:]
df = df[df['repo'].isin(select_repos)]
df = df.groupby(["user"])["repo"].apply(lambda x: ",".join(x))

# final data
df = pd.DataFrame(df)


# NN-Recommender model
class NNRecommender:
    def __init__(self, n_neighbors=10, max_features=1000, tokenizer=lambda x: x.split(",")):
        self.cv = CountVectorizer(tokenizer=tokenizer, max_features=max_features)
        self.nn = NearestNeighbors(n_neighbors=n_neighbors)

    def fit(self, X):
        self.X = X
        X = self.cv.fit_transform(X)
        self.nn.fit(X)
        return self

    def predict(self, X):
        Xp = []
        for Xi in X:
            Xt = self.cv.transform([Xi])
            _, neighbors = self.nn.kneighbors(Xt)
            repos = []
            for n in neighbors[0]:
                r = self.X.iloc[int(n)].split(",")
                repos.extend(r)
            repos = list(set(repos))
            repos = [r for r in repos if r not in Xi.split(",")]
            Xp.append(repos)
        return Xp

# Hyperparameters
n_neighbors = 10
max_features = 1000

model = NNRecommender(n_neighbors, max_features)
model.fit(df["repo"])

# serialise the model
with open("model.pkl", "wb") as f:
    dill.dump(model, f)
