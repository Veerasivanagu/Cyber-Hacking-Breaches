import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# use available dataset
path = 'model/Dataset/upload.csv'
df = pd.read_csv(path, encoding='unicode_escape')
if 'url' not in df.columns or 'status' not in df.columns:
    raise SystemExit('Dataset missing required columns url/status')

X = df['url']
y = df['status']

# simple label mapping, keep as is

vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_tfidf = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.3, random_state=250)

clf = RandomForestClassifier(random_state=0)
clf.fit(X_train, y_train)
print('train score', clf.score(X_train, y_train))
print('test score', clf.score(X_test, y_test))

pickle.dump(clf, open('model.pkl','wb'))
pickle.dump(vectorizer, open('tfidf_vectorizer.pkl','wb'))
print('model saved')
