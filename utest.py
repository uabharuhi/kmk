import unittest
import data
import numpy as np
class DataProcessTest(unittest.TestCase):
	@unittest.skip('')
	def  test_image_name_dict(self):
		d = data.get_images_name()
		self.assertTrue(len(d['yome'])==56)
	@unittest.skip('')
	def test_read_tvt_imgs(self):
		pass
		#img_dict = data.get_characters_ttv_imgs(['yome','reina','other'],['resize/train','resize/val','resize/test'])
		#yome_train,yome_val ,yome_test  = img_dict['yome'][0][0], img_dict['yome'][1][0], img_dict['yome'][2][0]
		#reina_train,reina_val ,reina_test  = img_dict['reina'][0][0], img_dict['reina'][1][0], img_dict['reina'][2][0]
		#other_train,other_val ,other_test  = img_dict['other'][0][0], img_dict['other'][1][0], img_dict['other'][2][0]
		#yome_train.show()
		#yome_val.show()
		#yome_test.show()
		#reina_train.show()
		#other_val.show()
	def  test_image2data(self):
		#read all images
		#all image to array1
		print('get  image dictionary...')
		img_dict = data.get_characters_ttv_imgs(['yome','reina','other'],['resize/train','resize/val','resize/test'])
		
		yome_a =[]
		for img in img_dict['yome'][0]:
			yome_a.append(np.asarray(img,dtype=np.uint8))

		yome_a = np.array(yome_a)


		yome_n = len(yome_a)
		

		print('len of train  yome %d'%(yome_n))

		#convert image to data
		data.dict2pkl(img_dict)

		X,y = data.read_dataset_from_pkl()

		print(yome_a[0])
		print('- - '*50)
		print(X['train'][0:yome_n][0])

		self.assertTrue(np.array_equal(X['train'][0:yome_n],yome_a) )
		_y = y['train'][0:yome_n]
		self.assertTrue(len( _y[_y==0] ) == yome_n )




		#read data




   	
   	
   	

   	
   	#convect  data to array2
   	#compare array1 and array2
   	#draw image (sample) from array2



   #def  test_image_rescale(self):
   	#w,h = 255,255
   	#test rescale image from  ./image ,rescale to 255*255
   	
        

if __name__ == '__main__':
    tests = unittest.TestLoader().loadTestsFromTestCase(DataProcessTest)
    unittest.TextTestRunner(verbosity=2).run(tests)