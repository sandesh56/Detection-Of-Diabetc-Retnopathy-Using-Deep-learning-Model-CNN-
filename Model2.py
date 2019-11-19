def createModel():
  model = Sequential()
  model.add(Conv2D(32,(3,3),padding ='same',activation = 'relu', input_shape =(512,512,3),name='convolution1'))
  model.add(BatchNormalization(name='batchnormalization1'))
  model.add(Conv2D(32, (3, 3), activation='relu',name='convolution2'))
  
  model.add(MaxPooling2D(pool_size=(2, 2),name='max_pooling1'))
  model.add(Dropout(0.25))
  
  model.add(Conv2D(64, (3, 3), padding='same', activation='relu',name='convolution3'))
  model.add(BatchNormalization(name='batchnormalization2'))
  model.add(Conv2D(64, (3, 3), activation='relu',name='convolution4'))
  model.add(BatchNormalization(name='batchnormalization3'))
  
  model.add(MaxPooling2D(pool_size=(2, 2),name='max_pooling2'))
  model.add(Dropout(0.25))
  
  model.add(Flatten())
  model.add(Dense(512, activation= 'relu'))
  model.add(BatchNormalization(name='batchnormalization4'))
  model.add(Dropout(0.5))
  model.add(Dense(3, activation = 'softmax'))
  
  opt = Adam(lr= 1e-3, decay= 1e-3 /210)
  model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["accuracy"])
  model.summary()
  return model

  
  
  
  
  
