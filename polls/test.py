# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 14:23:35 2019

@author: Admin
"""
from pymongo import MongoClient
from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from sklearn.metrics.pairwise import cosine_similarity
from keras.models import model_from_json
from keras.models import Model
import numpy as np
import os

class model:

	def __init__(self, idi):
		self.name= idi

	def done(self):
		model = VGG16()
		new_model=Model(model.input,model.layers[-4].output)
		'''json_file = open('C:\\Users\\Admin\\Desktop\\signature_verification\\mysite\\polls\\model.json', 'r')
		loaded_model_json = json_file.read()
		json_file.close()
		loaded_model = model_from_json(loaded_model_json)
		new_model=loaded_model.load_weights("C:\\Users\\Admin\\Desktop\\signature_verification\\mysite\\polls\\model.h5")
		print("Loaded model from disk")'''

		conn = MongoClient("mongodb://localhost:27017/")
		myDb = conn["signature"]
		myCol = myDb["info"]
		print("connected")
		image1= load_img(os.path.join(os.getcwd(),'polls\\xyz.jpg'), target_size=(224, 224))
		image1 = img_to_array(image1)
		image1 = image1.reshape((1, image1.shape[0], image1.shape[1], image1.shape[2]))
		image1 = preprocess_input(image1)
		test = new_model.predict(image1)
		print("image loaded")
		'''pair_list=[]
		print("processed")
		ans=-2
		_id=[]
		for doc in myCol.find():
		    arr=doc['avgv']
		    val=cosine_similarity(test,arr)
		    pair_list.append((val[0][0],doc['_id']))

		pair_list.sort(reverse=True)
		for i in range(0,min(len(pair_list),5)):
		    _id.append(pair_list[i][1])

		myquery = { "_id": {"$in" : _id} }'''
		myquery = { "name": self.name}
		mydoc = myCol.find(myquery)

		res=[]
		self.fin_list=[]
		for doc in mydoc:
			print(doc['name'])
			arr=doc['avgv']
			val=cosine_similarity(test,arr)
			if(val[0][0]<0.7):
				continue
			arr=doc['vector']
			print(doc['name'])
			j=0
			ans=-2
			for i in arr:
				feed=np.asarray(i);
				feed=feed.reshape(1,-1)
				#feed=np.reshape(feed, (1,-1))
				val=cosine_similarity(test,feed)
				ans=val[0][0]
				person=doc['name']
				path=doc['images'][j] 
				j+=1
				value={}
				value["person"]=person
				value["ans"]=round(ans*100,4)
				value["path"]=path
				res.append(value)
		
		res=sorted(res, key = lambda i: i['ans'],reverse=True)
		for i in range(0,min(len(res),5)):
			self.fin_list.append(res[i])

		        
		#print("HI {} {}".format(person,path))
		 