import sys
import os
sys.path.insert(0, 'C:\\Users\\Admin\\Desktop\\detection and verification\\mysite\\polls\\python')
from predict import predfin
from .bounding_tf import crop
class first:
    def firstmet(self):
        filename=os.path.join(os.getcwd(),'polls\\abc.jpg')
        obj=predfin(filename)
        obj.pred()
        prediction=obj.predictions
        top=prediction[0]['boundingBox']['top']
        left=prediction[0]['boundingBox']['left']
        leng=prediction[0]['boundingBox']['height']
        wid=prediction[0]['boundingBox']['width']
        obj1=crop(top,left,leng,wid)
        print("done cropping")
        obj1.cropping()

