import numpy as np
import os
import cv2
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import euclidean_distances

IMG_SIZE = (100, 100)
DATASET_PATH = "faces_dataset"

class EigenFaceRecognizer:
    def __init__(self, dataset_path=DATASET_PATH, img_size=IMG_SIZE):
        self.dataset_path = dataset_path
        self.img_size = img_size
        self.X, self.y, self.label_map = self.load_images()
        self.pca = self.train_pca()

    def load_images(self):
        X, y = [], []
        label_map = {}
        label_counter = 0
        for person in os.listdir(self.dataset_path):
            folder = os.path.join(self.dataset_path, person)
            if not os.path.isdir(folder): continue
            label_map[person] = label_counter
            for img_file in os.listdir(folder):
                path = os.path.join(folder, img_file)
                img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                img = cv2.resize(img, self.img_size)
                X.append(img.flatten())
                y.append(label_counter)
            label_counter += 1
        return np.array(X), np.array(y), label_map

    def train_pca(self):
        n_components = min(20, self.X.shape[0], self.X.shape[1])
        pca = PCA(n_components=n_components, whiten=True)
        pca.fit(self.X)
        return pca

    def predict(self, face_img):
        # face_img: ảnh mặt (grayscale, đúng kích thước)
        img = cv2.resize(face_img, self.img_size).flatten()
        img_pca = self.pca.transform([img])
        X_pca = self.pca.transform(self.X)
        distances = euclidean_distances(img_pca, X_pca)
        nearest_idx = np.argmin(distances)
        predicted_label = self.y[nearest_idx]
        name = [k for k, v in self.label_map.items() if v == predicted_label][0]
        return name, distances[0][nearest_idx]
