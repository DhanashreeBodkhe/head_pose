import os
import cv2
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from feature_extract import extract_features

dataset_path = "dataset/AFLW2000/"

X = []
y = []

print("Training started...")

for file in os.listdir(dataset_path):

    if file.endswith(".jpg") or file.endswith(".png"):

        path = os.path.join(dataset_path, file)
        image = cv2.imread(path)

        features = extract_features(image)

        if features is None:
            continue

        X.append(features)

        
        nose_shift = features[30] - features[1]

        if nose_shift > 0.02:
            y.append("right")
        elif nose_shift < -0.02:
            y.append("left")
        else:
            y.append("center")

X = np.array(X)

model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

joblib.dump(model, "model/model.pkl")

print("Training completed!")