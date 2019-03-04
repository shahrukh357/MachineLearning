import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier, GradientBoostingClassifier
from sklearn.feature_selection import RFE
from sklearn.kernel_approximation import RBFSampler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline

# NOTE: Make sure that the class is labeled 'target' in the data file
df = pd.read_pickle('modelreadyfortraining.pkl')

df["target"]=pd.cut(df['y1']*100, 
              bins=[-0.1, 5.11, 10.11, 15.11], 
              labels=['1', '2', '3'])

X=df.drop(['target','y1','y2'],1)
y=df['target']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.05, random_state=0,shuffle=False)


# Average CV score on the training set was:0.7091260400796906
exported_pipeline = make_pipeline(
    RBFSampler(gamma=0.30000000000000004),
    RFE(estimator=ExtraTreesClassifier(criterion="gini", max_features=0.9000000000000001, n_estimators=100), step=0.9000000000000001),
    GradientBoostingClassifier(learning_rate=0.01, max_depth=10, max_features=0.7000000000000001, min_samples_leaf=11, min_samples_split=11, n_estimators=100, subsample=0.6000000000000001)
)

exported_pipeline.fit(X_train,y_train)
results = exported_pipeline.predict(X_test)
accuracy=exported_pipeline.score(X_test,y_test)
print(accuracy)
