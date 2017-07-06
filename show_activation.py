#  this file is written to show the activation of hideen units(convokutinal and fullconnected)
# almost dead under high learning rate 
# by matplot
# or tensorboaed

# by matplot

#load model (final)

#extact acitvations 

#model.layers[0].input
#model.get_layer
from keras.models import load_model
import data
from keras import backend as K
batch_size = 16
num_classes = 3

X,y  = data.read_dataset_from_pkl()
X_train,X_val,X_test = X['train'].astype('float32')/255,X['val'].astype('float32')/255,X['test'].astype('float32')/255
y_train,y_val,y_test = y['train'],y['val'],y['test']

model = load_model('./save/final_model.hdf5')

exp_test = X_test[0:batch_size]
y_pred = model.predict(exp_test, batch_size=batch_size)

conv_a = K.function([model.layers[0].input,K.learning_phase()], # if use dropout must use learning phase and set  mode
                                  [model.get_layer('conv1_a').output])([exp_test,0])[0]

f1_a = K.function([model.layers[0].input,K.learning_phase()],
                                  [model.get_layer('dense1_a').output ])([exp_test,0])[0]




print('type of  model.layers[0].input')
print(type(model.layers[0].input))

print('type of  model.get_layer(conv1_a).output')
print(type(model.get_layer('conv1_a').output)) # by this way we can get tensorflow tensor



print('type of conv1')
print(type(conv_a))

print('shape of conv activation')
print(conv_a.shape)
print('shape of fl_a')
print(f1_a.shape)

print('conv activation')
print(conv_a)
print('- - '*50)
print('f1')
print(f1_a)






#... load model and show information every epoch end