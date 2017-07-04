from PIL import Image
import glob, os
import pickle
import  numpy as np
rsize = 128, 128
h5name = './data/data.hdf5' #contains input images & label  dataset ,sepereatd by category 
# read images name...
# convert images to hdf5
# using fixed size first ,than change to variable size..
# fixsize, simply rescale



#  get file names of each catogery ... -->save to a dict where key is character name

def get_images_name():

    character_names = ['yome','reina','other']
    #character_dirs = ['./image/yome','./image/reina','./image/other']
    image_names_wildcard = []

    for character_name in  character_names:
        image_names_wildcard.append('./image/%s/[0-9]*'%(character_name))

    image_names_dict= {}

    print('add dict...')
    for i,wildcard in enumerate(image_names_wildcard):
        character_name = character_names[i]

        if  character_name not in image_names_dict:
            image_names_dict[character_name] = []

        filename_list = image_names_dict[character_name]


        for infile in glob.glob(wildcard):
            filename, ext = os.path.splitext(infile)
            filename_list.append(filename)

            #im = Image.open(infile)
            #im = im.resize(size, Image.ANTIALIAS)
            #im.save(file + ".resize", "JPEG")
    return image_names_dict

# return dict
# imgs must name [0-9]*
# {
#  name:[train_data_img,val_data_img,test_img] 
#
#}
#                                            [to_train,to_val,to_test]
def get_characters_ttv_imgs(character_names,suffix_to_tvt_folders):

    img_dict ={}

    assert len(suffix_to_tvt_folders)==3

    #suffix_train,suffix_val,suffix_test = suffix_to_tvt_folders[0],suffix_to_tvt_folders[1],suffix_to_tvt_folders[2]
    #folder_train,folder_val,folder_test = None,None,None
    for name in character_names:
        tvt_list = []
        for suffix in suffix_to_tvt_folders:
            img_list = []
            wildcard = './image/%s/%s/[0-9]*'%(name,suffix)
           
            for infile in glob.glob(wildcard):
                filename, ext = os.path.splitext(infile)
               
                im = Image.open(filename)
                img_list.append(im)
                
            #print(wildcard)
            assert len(img_list)>0

            tvt_list.append(img_list)
        img_dict[name] = tvt_list
    return  img_dict
       


#resize image from ./images/yome,./images/reina ... to 128*128 , and save them to ./images/*/resize

def resize_images(filenames_list):
    print('resize images')
    for filename in filenames_list :
        dirname = os.path.dirname(filename)

        resize_dir_prefix = '%s/resize/'%(dirname)
        img_name = os.path.basename(filename)

        im = Image.open(filename)
        im = im.resize(rsize, Image.ANTIALIAS)

        im.convert('RGB').save(resize_dir_prefix + img_name, "JPEG")


#dict  form of get_characters_ttv_imgs(character_names,suffix_to_tvt_folders):
def dict2pkl(img_dict):
    dataset_name = ['train','val','test']
    characete_label_dict={'yome':0,'reina':1,'other':2}
    for i,name  in  enumerate(dataset_name): #create tranins set,val set..
        X_all =[] #n*128*128*3
        y_all = []
        #combine diffrent  characete  train to one set
        for character_name in img_dict:    
            X_character = img_dict[character_name][i] # n*128*128*3
            for  img in X_character:
                X_all.append(np.asarray(img, dtype=np.uint8))
                y_all.append(characete_label_dict[character_name])


        X_all = np.array(X_all) 

        y_all = np.array(y_all)
        y_all = np.reshape(y_all,(y_all.shape[0],1)) # n*1

        assert  X_all.shape[0]==y_all.shape[0]
        assert len(X_all.shape)== 4

        fx = open('./data/X_%s.hkl'%(name),'wb')
        fy = open('./data/y_%s.hkl'%(name),'wb')

        pickle.dump(X_all,fx)
        pickle.dump(y_all,fy)

#return 2 dicts X[data_set_name]
def read_dataset_from_pkl():   
    X={}
    y={}
    dataset_names = ['train','val','test']
    for name in dataset_names:
        X[name] = pickle.load( open('./data/X_%s.hkl'%(name),'rb') )
        y[name] = pickle.load( open('./data/y_%s.hkl'%(name),'rb') )
    return X,y
    #pickle.dump(a, f)
    #a = np.asarray(im, dtype=np.uint8)
#    # a w,h will interchange 5*6*3  --> 6*5*3
#    f = h5py.File(h5name, "a")
#    w,h  = rsize
#
#    if 'image' not in f:
#        f.create_dataset("image", (h,w,3,), dtype='i')
#    if 'label' not in f:
#        f.create_dataset("label", (1,), dtype='i')
#
#    dinput_image = f['image']
#    dlabel =  f['label']



    #add to image dataset


