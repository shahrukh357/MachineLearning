import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# NOTE: Make sure that the class is labeled 'target' in the data file
df = pd.read_pickle('modelreadyfortraining.pkl')

df["target"]=pd.cut(df['y1']*100, 
              bins=[-0.1, 5.11, 10.11, 15.11], 
              labels=['1', '2', '3'])

X=df.drop(['target','y1','y2'],1)
y=df['target']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.05, random_state=0,shuffle=True)


exported_pipeline = RandomForestClassifier(bootstrap=True, criterion="entropy", max_features=0.4, min_samples_leaf=6, min_samples_split=14, n_estimators=100)

exported_pipeline.fit(X_train,y_train)
results = exported_pipeline.predict(X_test)
accuracy =exported_pipeline.score(X_test,y_test)
print(accuracy) 
