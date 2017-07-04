import data

name_dict = data.get_images_name()

for key in name_dict :
	imgname_list = name_dict[key]
	data.resize_images(imgname_list)