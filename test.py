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
from keras.models import Model
import numpy as np
import os

model = VGG16()
new_model=Model(model.input,model.layers[-4].output)

conn = MongoClient("mongodb://localhost:27017/")
myDb = conn["signature"]
myCol = myDb["info"]

print("here")
image1= load_img('C:\\Users\\Admin\\Desktop\\signature_verification\\mysite\\abc.jpg', target_size=(224, 224))
image1 = img_to_array(image1)
image1 = image1.reshape((1, image1.shape[0], image1.shape[1], image1.shape[2]))
image1 = preprocess_input(image1)
test = new_model.predict(image1)

pair_list=[]
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

myquery = { "_id": {"$in" : _id} }
mydoc = myCol.find(myquery)

fin_list=[]
for doc in mydoc:
    arr=doc['vector']
    print(doc['name'])
    j=0
    ans=-2
    for i in arr:
        feed=np.asarray(i);
        feed=feed.reshape(1,-1)
        #feed=np.reshape(feed, (1,-1))
        val=cosine_similarity(test,feed)
        if(val[0][0]>=ans):
            ans=val[0][0]
            person=doc['name']
            path=doc['images'][j]
        j+=1
    fin_list.append((person,(ans,path)))

'''for x in fin_list:
    print(x[0])
    print(x[1][0])
    print(x[1][1])'''
        
#print("HI {} {}".format(person,path))
 