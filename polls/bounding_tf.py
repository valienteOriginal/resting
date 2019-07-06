import cv2
import os
import matplotlib.pyplot as plt
import tensorflow as tf   
import numpy as np
from PIL import Image
class crop:

	def __init__(self,top,left,leng,wid):
		self.top=top
		self.left=left
		self.leng=leng
		self.wid=wid
		self.bottom= self.top+self.leng
		self.right= self.left+self.wid

	'''def tfcropping(self):
		image_raw_data = tf.gfile.FastGFile(os.path.join(os.getcwd(),'polls\\abc.jpg'),'rb').read()
		with tf.Session() as sess:
		    img_data = tf.image.decode_jpeg(image_raw_data)
		    boxes = tf.constant([[[self.top,  self.left, self.top+self.leng, self.left+self.wid]]])
		    batched = tf.expand_dims(tf.image.convert_image_dtype(img_data, tf.float32), 0)
		    image_with_box = tf.image.draw_bounding_boxes(batched, boxes)
		    #print (image_with_box[0].eval())
		    plt.imshow(image_with_box[0].eval()),plt.title("result")
		    print("going to save png")
		    plt.savefig(os.path.join(os.getcwd(),'polls\\xyz.png'))
		    im = Image.open(os.path.join(os.getcwd(),'polls\\xyz.png'))
		    rgb_im = im.convert('RGB')
		    rgb_im.save(os.path.join(os.getcwd(),'polls\\xyz1.jpg'))'''

	def cropping(self):
		img=cv2.imread(os.path.join(os.getcwd(),'polls\\abc.jpg'))
		height,width,ch= img.shape
		crop_img = img[round(self.top*height):round(self.bottom*height), round(self.left*width):round(self.right*width)]
		cv2.imwrite(os.path.join(os.getcwd(),'polls\\xyz.jpg'),crop_img)
		img1=cv2.rectangle(img, (round(self.left*width), round(self.top*height)), (round(self.right*width), round(self.bottom*height)), (255,0,0), 2)
		cv2.imwrite(os.path.join(os.getcwd(),'polls\\xyz1.jpg'),img1)
