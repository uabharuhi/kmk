from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D#, MaxPooling2D
from keras.utils import plot_model
import keras
import data

batch_size = 16
num_classes = 3
epochs = 20
X,y  = data.read_dataset_from_pkl()
X_train,X_val,X_test = X['train'].astype('float32')/255,X['val'].astype('float32')/255,X['test'].astype('float32')/255
y_train,y_val,y_test = y['train'],y['val'],y['test']

y_train = keras.utils.to_categorical(y_train, num_classes)
y_val = keras.utils.to_categorical(y_val, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
#label shape !!! : n*1 or n

print('x_train shape:', X_train.shape)
print(y_train)
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')




model = Sequential()
model.add(Conv2D(16, (3, 3), padding='same',data_format='channels_last',input_shape=X_train.shape[1:]))
# if not add input shape The first layer in a Sequential model must get an `input_shape` or `batch_input_shape` argument.
model.add(Activation('relu',name='conv1_a') )

#model.add(Conv2D(16, (3, 3), padding='same',data_format='channels_last'))#default is channels_last
#model.add(Activation('relu'))
#model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
#model.add(Dense(50))
model.add(Dense(10))
model.add(Activation('relu',name='dense1_a') )
model.add(Dense(num_classes))
model.add(Activation('softmax') )

#opt = keras.optimizers.Adadelta()
opt = keras.optimizers.SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)

model.compile(loss='categorical_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])

hist = model.fit(X_train, y_train,
		batch_size=batch_size,
		epochs=epochs,
		validation_data=(X_val, y_val),
		shuffle=True
		,callbacks=[keras.callbacks.ModelCheckpoint('./save/best_model.hdf5'),keras.callbacks.History()])
print(hist.history)
model.save('./save/final_model.hdf5')  # creates a HDF5 file 'my_model.h5'

plot_model(model, to_file='./model.png')

del model

