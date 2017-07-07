from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D#, MaxPooling2D
import keras
import data

num_classes = 3

#label shape !!! : n*1 or n
X,y  = data.read_dataset_from_pkl()
X_train,X_val,X_test = X['train'].astype('float32')/255,X['val'].astype('float32')/255,X['test'].astype('float32')/255
y_train,y_val,y_test = y['train'],y['val'],y['test']

y_train = keras.utils.to_categorical(y_train, num_classes)
y_val = keras.utils.to_categorical(y_val, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

print('x_train shape:', X_train.shape)
#print(y_train)
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')

def simple_model(batch_size,epochs):
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

	return model

## defined callback
class ActivationLogger(keras.callbacks.Callback):
	activation_history = {}
	X_batch = None

	def __init__(self,X_batch):
		self.X_batch = X_batch

	def on_train_begin(self, logs={}):
		self.losses = []

	def on_epoch_end(self, epoch, logs={}):

		import show_activation
		#print('== ==')
		if 'conv1_a' not in self.activation_history:
			self.activation_history['conv1_a'] = []
		#print('batch shape')
		print('epoch:%d'%epoch)
		a = show_activation.get_layer_output(self,'conv1_a',self.X_batch)
		self.activation_history['conv1_a'].append(a)
