import unittest
import data
class DataProcessTest(unittest.TestCase):
   def  test_image_name_dict(self):
   		d = data.get_images_name()
   		self.assertTrue(len(d['yome'])==56)
   #def  test_image_rescale(self):
   	#w,h = 255,255
   	#test rescale image from  ./image ,rescale to 255*255
   	
        

if __name__ == '__main__':
    tests = unittest.TestLoader().loadTestsFromTestCase(DataProcessTest)
    unittest.TextTestRunner(verbosity=2).run(tests)