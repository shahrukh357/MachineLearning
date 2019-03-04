import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


df = pd.read_pickle('modelreadyfortraining.pkl')
X=df.drop(['y1','y2'],1)

target_y2_4label=pd.cut(df['y2'], 
              bins=[-1.7,-1.02,-0.34,0.34,1.02, 1.7], 
              labels=['1', '2','3','4','5'])
target_y2_4label=target_y2_4label.astype('float')
X_train,X_test,y_train,y_test = train_test_split(X,target_y2_4label,test_size=0.05, random_state=0,shuffle=False)


exported_pipeline = KNeighborsClassifier(n_neighbors=59, p=1, weights="distance")

exported_pipeline.fit(X_train, y_train)
results = exported_pipeline.predict(X_test)
accuracy=exported_pipeline.score(X_test,y_test)
print(accuracy)
