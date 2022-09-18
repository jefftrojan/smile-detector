import os

# create a string variable to save datasets location
negative_img_loc = r"datasets/0"
positive_img_loc = r"datasets/1"

# list images from their specified locations 

negative_img = os.listdir(negative_img_loc)
positive_img = os.listdir(positive_img_loc)

print(positive_img)
print(negative_img)