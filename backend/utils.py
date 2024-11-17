import numpy as np
import cv2
import os

def extract_features(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sift = cv2.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(gray, None)
    return descriptors

def euclidean_dist(x, y):
    return np.linalg.norm(x - y)

def cosine_similarity(x, y):
    dot_product = np.dot(x, y)
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    return dot_product / (norm_x * norm_y)

def pcc(x, y):
    return np.corrcoef(x, y)[0, 1]

def calculate_similarity(query_features, all_features, method, normalized):
    similarity_list = []
    for img_path, features in all_features.items():
        if normalized:
            features = features / np.linalg.norm(features)
            query_features = query_features / np.linalg.norm(query_features)
        
        if method == 'euclidean':
            score = euclidean_dist(query_features, features)
        elif method == 'cosine':
            score = cosine_similarity(query_features, features)
        elif method == 'pcc':
            score = pcc(query_features, features)

        similarity_list.append((img_path, score))
    similarity_list.sort(key=lambda x: x[1])
    return similarity_list
