import numpy as np
import os

from keras.models import  load_model
from keras.preprocessing import image
import tensorflow as tf

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        try:
            model = load_model(os.path.join('artifacts', 'training', 'model.h5'))
            test_img = image.load_img(self.filename, target_size=(299, 299))
            test_img = image.img_to_array(test_img)
            test_img = np.expand_dims(test_img, axis=0)
            result = np.argmax(model.predict(test_img), axis=1)
            print(result)

            if result[0] == 1:
                prediction = 'glioma'
                return [{'image': prediction}]
            elif result[0] == 0:
                prediction = 'meningioma'
                return [{'image': prediction}]
        except Exception as e:
            print(f"Error in prediction: {e}")
            return {"error" : str(e)} 




    



