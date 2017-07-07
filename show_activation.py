#  this file is written to show the activation of hideen units(convokutinal and fullconnected)
# almost dead under high learning rate 
# by matplot
# or tensorboaed

# by matplot

#load model (final)

#extact acitvations 

#model.layers[0].input
#model.get_layer
from keras import backend as K

#mode 0  test 1 training
#get sequetial model  output of a layer...
#self a model instance = keras call back self

def get_layer_output(self,name,epoch_X):
	                     # tensorflow tensor
	print('shape of epoch_X')
	print(epoch_X.shape)
	# dont know how to  get traning activation ... so use test mode
	output  = K.function([self.model.layers[0].input,K.learning_phase()],
		                                                        #numpy array
                         [self.model.get_layer(name).output] )( [epoch_X,0])[0]

	return output # numpy array




#... load model and show information every epoch end
