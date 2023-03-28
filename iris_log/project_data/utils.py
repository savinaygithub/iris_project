import numpy as np
import config
import json
import pickle

class IrisPrediction():
    def __init__(self,sepal_length,sepal_width,petal_length,petal_width):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width

    def load_model(self):
        with open(config.MODEL_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_PATH, "r") as f:
            self.json_data = json.load(f)   

    def get_species(self):
        self.load_model()

        test_array=np.zeros(len(self.json_data["columns"]))
        print(test_array)
        test_array[0]=self.sepal_length
        test_array[1]=self.sepal_width
        test_array[2]=self.petal_length
        test_array[3]=self.petal_width
        print(test_array)

        predict = self.model.predict([test_array])[0]
        return predict
         