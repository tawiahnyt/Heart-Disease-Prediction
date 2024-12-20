# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

# Loading the saved model
loaded_model = pickle.load(open('models/heart_disease_model.sav', 'rb'))

input_data = (64,1,4,128,263,0,0,105,1,0.2,2)
input_data_as_numpy_array = np.asarray(input_data)
reshaped_input_data = input_data_as_numpy_array.reshape(1, -1)

prediction = loaded_model.predict(reshaped_input_data)

print(prediction)

if (prediction[0] == 0):
    print('The person does not have a heart disease')
else:
    print('The person has heart disease')