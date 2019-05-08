#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy
import os
from keras import applications
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from keras.models import Sequential, Model
from keras.layers import Dropout, Flatten, Dense, GlobalAveragePooling2D
from keras import backend as k
from keras.callbacks import ModelCheckpoint, LearningRateScheduler, TensorBoard, EarlyStopping
from ipykernel.kernelapp import IPKernelApp

# ### 1. Load Test and Train Files

# In[7]:


files_train = 0
files_validation = 0

cwd = os.getcwd()
folder = 'train_data/train'
train_folder = os.listdir(folder)
# in case ".DS_Store" was in the output of os.listdir(folder)
if ".DS_Store" in train_folder:
    train_folder.remove(".DS_Store")
for sub_folder in train_folder:
    path, dirs, files = next(os.walk(os.path.join(folder,sub_folder)))
    files_train += len(files)

folder = 'train_data/test'
test_folder = os.listdir(folder)
if ".DS_Store" in test_folder:
    test_folder.remove(".DS_Store")
for sub_folder in test_folder:
    path, dirs, files = next(os.walk(os.path.join(folder,sub_folder)))
    files_validation += len(files)

print(files_train,files_validation)


# ### 2. Set key parameters

# In[8]:


img_width, img_height = 48, 48
train_data_dir = "train_data/train"
validation_data_dir = "train_data/test"
nb_train_samples = files_train
nb_validation_samples = files_validation
batch_size = 32
epochs = 15
num_classes = 2


# ### 3. Build model on top of a trained VGG

# In[10]:


model = applications.VGG16(weights = "imagenet", include_top=False, input_shape = (img_width, img_height, 3))
# Freeze the layers which you don't want to train. Here I am freezing the first 5 layers.
for layer in model.layers[:10]:
    layer.trainable = False


# In[11]:


x = model.output
x = Flatten()(x)
# x = Dense(512, activation="relu")(x)
# x = Dropout(0.5)(x)
# x = Dense(256, activation="relu")(x)
# x = Dropout(0.5)(x)
predictions = Dense(num_classes, activation="softmax")(x)

# creating the final model
model_final = Model(input = model.input, output = predictions)

# compile the model
model_final.compile(loss = "categorical_crossentropy", 
                    optimizer = optimizers.SGD(lr=0.0001, momentum=0.9), 
                    metrics=["accuracy"]) # See learning rate is very low


# In[12]:


# Initiate the train and test generators with data Augumentation
train_datagen = ImageDataGenerator(rescale = 1./255,
                                   horizontal_flip = True,
                                   fill_mode = "nearest",
                                   zoom_range = 0.1,
                                   width_shift_range = 0.1,
                                   height_shift_range=0.1,
                                   rotation_range=5)

test_datagen = ImageDataGenerator(rescale = 1./255,
                                  horizontal_flip = True,
                                  fill_mode = "nearest",
                                  zoom_range = 0.1,
                                  width_shift_range = 0.1,
                                  height_shift_range=0.1,
                                  rotation_range=5)

train_generator = train_datagen.flow_from_directory(train_data_dir,
                                                    target_size = (img_height, img_width),
                                                    batch_size = batch_size,
                                                    class_mode = "categorical")

validation_generator = test_datagen.flow_from_directory(validation_data_dir,
                                                        target_size = (img_height, img_width),
                                                        class_mode = "categorical")


# In[13]:


# Save the model according to the conditions
checkpoint = ModelCheckpoint("car1.h5", monitor='val_acc', verbose=1, 
                             save_best_only=True, save_weights_only=False, 
                             mode='auto', period=1)

early = EarlyStopping(monitor='val_acc', min_delta=0, patience=10, verbose=1, mode='auto')


steps_per_epoch = int(nb_train_samples / batch_size)
print(steps_per_epoch)

type(train_generator)

for line in train_generator:
    print(line)

### Start training!
#steps_per_epoch = int(nb_train_samples / batch_size)
#history_object = model_final.fit_generator(
#    train_generator, 
#    steps_per_epoch = steps_per_epoch)
   # epochs = epochs,
   # validation_data = validation_generator,
    #nb_val_samples = nb_validation_samples,
    #callbacks = [checkpoint, early])


# In[1]:


#import matplotlib.pyplot as plt
#print(history_object.history.keys())
#plt.plot(history_object.history['acc'])
#plt.plot(history_object.history['val_acc'])
#plt.title('model accuracy')
#plt.ylabel('acc')
#plt.xlabel('epoch')
#plt.legend(['train', 'test'], loc='upper left')
#plt.show()
#
#
## In[2]:
#
#
#plt.plot(history_object.history['loss'])
#plt.plot(history_object.history['val_loss'])
#plt.title('model loss')
#plt.ylabel('loss')
#plt.xlabel('epoch')
#plt.legend(['train', 'test'], loc='upper left')
#plt.show()
#
#
## In[ ]:
#
#
#
#
