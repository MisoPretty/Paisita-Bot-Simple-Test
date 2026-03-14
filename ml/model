
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.calibration import CalibratedClassifierCV
from sklearn.model_selection import train_test_split

class ProbabilityModel:

    def __init__(self):
        self.model=None

    def _build_features(self,df:pd.DataFrame)->pd.DataFrame:
        feats=pd.DataFrame()
        feats["yes_price"]=df["yes_price"].astype(float)
        feats["no_price"]=df["no_price"].astype(float)
        feats["spread"]=feats["no_price"]-feats["yes_price"]
        feats["volume"]=df.get("volume",0).astype(float)
        feats["time_to_expiry_minutes"]=df.get("time_to_expiry_minutes",0).astype(float)
        return feats

    def fit(self,historical:pd.DataFrame)->None:
        df=historical.copy()
        df=df[df["resolved"]==True]
        df=df.dropna(subset=["yes_price","no_price","outcome"])

        X=self._build_features(df)
        y=df["outcome"].astype(int)

        if len(df)<50:
            self.model=None
            return

        X_train,X_test,y_train,y_test=train_test_split(
            X,y,test_size=0.2,random_state=42,stratify=y
        )

        base=GradientBoostingClassifier(random_state=42)
        calibrated=CalibratedClassifierCV(base,cv=3,method="isotonic")
        calibrated.fit(X_train,y_train)
        self.model=calibrated

    def predict_proba(self,snapshot:pd.DataFrame)->np.ndarray:
        if self.model is None or snapshot.empty:
            return np.zeros(len(snapshot))
        X=self._build_features(snapshot)
        return self.model.predict_proba(X)[:,1]

    def compute_edges(self,snapshot:pd.DataFrame)->pd.Series:
        yes_price=snapshot["yes_price"].astype(float)
        probs=self.predict_proba(snapshot)
        edges=probs-yes_price
        return pd.Series(edges,index=snapshot.index)
