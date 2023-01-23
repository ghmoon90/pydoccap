from PIL import Image
import os

sz_doctitle = input('document title :')
path_dir = './' + sz_doctitle 
file_list = os.listdir(path_dir)


img_list = []
img_path = path_dir+'/'+file_list[0]
im_buf      = Image.open(img_path)
cvt_rgb_0  = im_buf.convert('RGB')

for sz_img in file_list:
    img_path = path_dir+'/'+sz_img
    im_buf = Image.open(img_path)
    cvt_rgb = im_buf.convert('RGB')
    img_list.append(cvt_rgb)
    print(sz_img + " done")

    
cvt_rgb_0.save('./'+sz_doctitle+'.pdf', save_all = True, append_images = img_list )