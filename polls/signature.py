from pymongo import MongoClient
from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from sklearn.metrics.pairwise import cosine_similarity
from keras.models import Model
import numpy as np
import os

class sign:

	def helping(self):
		model = VGG16()

		new_model=Model(model.input,model.layers[-4].output)

		conn = MongoClient("mongodb://localhost:27017/")
		myDb = conn["signature"]
		myCol = myDb["info"]

		path='C:\\Users\\Admin\\Desktop\\detection and verification\\mysite\\static\\database'
		folder=os.listdir(path)
		for f in folder:
		    if(f[-9:]=="processed"):
		        continue
		    yhat=[]
		    img_path=[]
		    avg=[]
		    img=os.listdir(os.path.join(path,f))
		    for images in img:
		        if(images=="desktop.ini"):
		            continue
		        rel_path=os.path.join(f,images)
		        print(rel_path)
		        print(os.path.join(path,rel_path))
		        image = load_img(os.path.join(path,rel_path), target_size=(224, 224))
		        image = img_to_array(image)
		        image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
		        image = preprocess_input(image)
		        pre=new_model.predict(image)
		        yhat.append(pre.tolist())
		        avg.append(pre)
		        fin_name=f+"_processed"
		        fin_name=os.path.join('database',fin_name)
		        img_path.append(os.path.join(fin_name,images))
		    avgv = np.asarray(avg)
		    avgv = np.mean(avgv, axis=0)
		    myDict = { "name": f,"vector": yhat, "images":img_path, "avgv":avgv.tolist() }
		    myCol.insert_one(myDict)
		    fin_name=f+"_processed"
		    os.rename(os.path.join(path,f),os.path.join(path,fin_name))
	    
#yhat = np.asarray(yhat)
#yhat=np.mean(yhat, axis=0)
#xhat = np.asarray(xhat)
#xhat=np.mean(xhat, axis=0)



'''myDict = { "name": "Abinash Dutta","vector": xhat, "images":img_path1 }
myCol.insert_one(myDict)

image1= load_img('C:\\Users\\Admin\\Pictures\\asign1.jpeg', target_size=(224, 224))
image1 = img_to_array(image1)
image1 = image1.reshape((1, image1.shape[0], image1.shape[1], image1.shape[2]))
image1 = preprocess_input(image1)
test = new_model.predict(image1)

ans=-2
for doc in myCol.find():
    arr=doc['vector']
    j=0;
    for i in arr:
        feed=np.asarray(i);
        feed=feed.reshape(1,-1)
        #feed=np.reshape(feed, (1,-1))
        val=cosine_similarity(test,feed)
        print(val)
        if(val>=ans):
            ans=val
            person=doc['name']
            path=doc['images'][j]
            print(person)
        j+=1
        
print("HI {} {}".format(person,path))'''
 