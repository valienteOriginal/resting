from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .test import model
import sys
import os
sys.path.insert(0, 'C:\\Users\\Admin\\Desktop\\detection and verification\\mysite\\polls\\python')
from predict import predfin
from .bounding_tf import crop
from .signature import sign
#sys.path.insert(0, 'C:\\Users\\Admin\\Desktop\\detection and verification\\mysite\\polls\\python')

def index(request):

    return render(request, 'index.html')

def post(request):
    if 'myImage' in request.FILES:
        print("yesnnnnnnnnnnnnnnnn")
        col=sign()
        col.helping()
        f = request.FILES['myImage']
        idi = request.POST['idi']
        print(idi)
        print(os.path.join(os.getcwd(),'polls\\abc.jpg'))
        destination = open(os.path.join(os.getcwd(),'polls\\abc.jpg'), 'wb+')
        for chunk in f.chunks():
            destination.write(chunk)
        destination.close()
        filename=os.path.join(os.getcwd(),'polls\\abc.jpg')
        obj2=predfin(filename)
        obj2.pred()
        prediction=obj2.predictions
        top=prediction[0]['boundingBox']['top']
        left=prediction[0]['boundingBox']['left']
        leng=prediction[0]['boundingBox']['height']
        wid=prediction[0]['boundingBox']['width']
        obj1=crop(top,left,leng,wid)
        obj1.cropping()
        obj=model(idi)
        obj.done()
        dictr=obj.fin_list
        if(len(dictr)==0):
            return HttpResponse("Signature does not match")
        return render(request, 'new.html', {'dictr':dictr})
    return HttpResponse("Signature does not match")




    '''fin_list=[]

for doc in mydoc:
    arr=doc['vector']
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
            print(person)
        j+=1
    fin_list.append((person,(ans,path))

for x in pair_list:
    print(x[0])
    print(x[1][0])
    print(x[1][1])'''