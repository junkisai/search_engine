from keras.preprocessing import image
from keras.applications.vgg16 import VGG16, preprocess_input
from keras.models import Model
import numpy as np
import tensorflow as tf

class FeatureExtractor:
  def __init__(self):
    base_model = VGG16(weights='imagenet')
    a = 3

  def extract(self, img):
    return [3, 3, 3]

if __name__ == "__main__":
  fe = FeatureExtractor()
  img = 123
  print(fe.extract(img))