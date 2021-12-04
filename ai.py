#!/usr/bin/env python

#panda is a module that is used for data manipulation and analysis. Importing it as pd allows us to use pd as the alias. Instead of typing pandas.function_name you type pd.function_name
import pandas as pd

#the next line sets the dataset variable and tells panda what to read to get the data from. 
dataset = pd.read_csv('cancer.csv')

#Now we set the x and y attributes. The x attribute is all of the details of the measured tumor. The Y access is the diagnosis. So to set the x axis as everything except the diagnosis
#column, we drop that column and use everything else.
x = dataset.drop(columns=["diagnosis(1=m, 0=b"])
y = dataset["diagnosis(1=m, 0=b)"]

#AI sometimes has trouble processing new data that is given outside of the original dataset. To mitigate this, we create a data split. Some of the data gets used while the rest is held.
#We then use this held data as another piece of data for the AI to process to be sure that it won't malfunction when given more datasets later.
#For this we use scikitlearn which is a popular machine learning library. I need to do more myself. But 20% of the data will be held as a test split.
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

#Now we will use Keras from Tensor Flow to build a basic neural network. We will use this to add modules to the neural network
import tensorflow as tf
model = tf.keras.models.Sequential()

#This is building a model for the neural network. 256 modules on the input layer is a bit much, but is good for example. Sigmoid function just plots data between 0 and 1
#The next line creates the layers in the middle of the neural network with 256 modules (Dense is the standard in keras it seems) and the final line is the output module where we determine
#if the tumor is malignant or benign. The sigmoid function gives this as a 0 or 1
model.add(tf.keras.layers.Dense(256, input_shape=x=train.shape, activation='sigmoid'))
model.add(tf.keras.layers.Dense(256, activation='sigmoid'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

#This is adding the optimizer which is how each neural module is being fine tuned to fit the data. Adam is a relatively common one.
#The loss function is used to help categorize discreet values? That is how it was explained in the video, will need to learn more.
#Accuracy of the AI is the metric we want to focus on.
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    
