import cv2
from google.colab.patches import cv2_imshow

class Image_info():
  def __init__(self, path):
    self.path = path
    self.image = cv2.imread(self.path)

  
  def show_details(self):
    print("Image Shape : ", self.image.shape)
    print("Number of channels : ", self.image.shape[2])
    print("Image height : ",self.image.shape[0])
    print("Image width : ", self.image.shape[1])
    cv2_imshow(self.image)
