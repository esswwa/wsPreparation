import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier

# чтение csv файла
dfHabr1 = pd.read_csv(r'C:\Users\МОиБД\Downloads\Report3.csv')

# Выбор целевой и обучающей переменной
X = dfHabr1['TextPost']
y = dfHabr1['Nomination']

# Деление на обучающие и тестовые переменные
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Создание модели с помощью Pipeline
sgd = Pipeline([('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42, max_iter=5, tol=None)),
               ])

# Обучение методом SGDClassifier
sgd.fit(X_train, y_train)

# Предсказание и проверка предсказания
def predict_nomination(text):
    return sgd.predict([text])
