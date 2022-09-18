import os
from PIL import Image

# create function to get images path from dataset
def img_path():

    # create a string variable to save datasets location
    negative_img_loc = r"datasets/0"
    positive_img_loc = r"datasets/1"

    # list images from their specified locations 

    negative_img = os.listdir(negative_img_loc)
    positive_img = os.listdir(positive_img_loc)

    # loop over the list of individual images and get full paths for each
    pos_fullpath = [positive_img_loc + r"/" + image for image in positive_img]
    neg_fullpath = [negative_img_loc + r"/" + image for image in positive_img]

    return pos_fullpath, neg_fullpath

pos_paths, neg_paths = img_path()
 
demo = pos_paths[0]
img = Image.open(demo)
img.show()