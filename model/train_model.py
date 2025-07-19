import os
import numpy as np
import cv2
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load images and labels from folder
def load_data(data_dir):
    X, y = [], []
    labels = {'fresh': 0, 'spoiled': 1}
    for label_name, label_index in labels.items():
        path = os.path.join(data_dir, label_name)
        for file in os.listdir(path):
            img_path = os.path.join(path, file)
            img = cv2.imread(img_path)
            if img is None:
                print(f"Skipped unreadable image: {img_path}")
                continue
            img = cv2.resize(img, (100, 100))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            X.append(img.flatten())
            y.append(label_index)
    return np.array(X), np.array(y)

# Training
X, y = load_data('../Dataset')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save model
os.makedirs("model", exist_ok=True)
with open("model/trained_model.pkl", "wb") as f:
    pickle.dump(model, f)
