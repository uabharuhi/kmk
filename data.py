from PIL import Image
import glob, os

rsize = 128, 128
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