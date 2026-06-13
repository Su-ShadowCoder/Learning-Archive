###############################################

# Lesson: Images With Python

# from PIL import Image, ImageFilter

# #  asiging a filter to the image
# img = Image.open('./photos/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save("blur.png", "png")

# img = Image.open('./photos/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img.save("SHARPEN.png", "png")

# converting image to grey
# img = Image.open('./photos/pikachu.jpg')
# filtered_img = img.convert('L')
# filtered_img.save("grey2.png", 'png')

# img = Image.open('./photos/pikachu.jpg')
# filtered_img = img.convert("P")
# filtered_img.save("ok.png", 'png')




###############################################

# # Lesson: Images With Python 2


# showing a image by using a third party aplication
# it is necessary  to do that ina terminal because of the installation that has been used. as it is difficult to connect with other apps trough this method of installation. 
# img = Image.open('./photos/pikachu.jpg')
# filtered_img = img.convert('L')
# crooked = filtered_img.rotate(90)
# crooked.save("grey2.png", 'png')
# crooked.show()


# resize image
# img = Image.open('./photos/pikachu.jpg')
# filtered_img = img.convert('L')
# resize = filtered_img.resize((300, 300))
# resize.save("grey2.png", 'png')

# cropping an image

# img2 = Image.open('./photos/squirtle.jpg')
# cropped_img = img2.crop((100, 100, 400, 400))
# cropped_img.save("cropped_img.png","png")




###############################################

# # Lesson: Images With Python 3

# This lesson explains how to produce memory-efficient thumbnails for large images by performing in-memory transformations and saving the result as a new file to protect the original data.

# from PIL import Image, ImageFilter

# basic_astro_img = Image.open('./photos/astro.jpg')

# basic_astro_img.show()
# print(basic_astro_img.size)

# astro_img_resized = basic_astro_img.resize((400,400))
# astro_img_resized.show()
# astro_img_resized.save('astro_resized.jpg', format='JPEG')


# # using the thumnail method would allow you to keep the aspect ratio which would mean that in accordance with the specification that the ratio of the image would be tuned while resizing the image. of course somethime the size could differe based on the ratio of the image within the specified range. 
# basic_astro_img.thumbnail((400, 400))
# # with the thumbnail method, it requires you to just use the existing image and an for the duration that is In-memory makes changes on the origial one. so you cannot assign a new object to it as a changed object using the method directly. 
# basic_astro_img.save('astro_thumbnail.jpg', format='JPEG')
# # you just save the modified object then under a different name as the method  changed the basic image object only In-Memory. by doing this you would have a new image with permanent modification(On-Disk) that you have applied. 
# # In-memory means temporarily in ram, until closing the script or reload the file
# # On-Disk is permanent
# astro_thumbnail = Image.open('./astro_thumbnail.jpg')
# print(astro_thumbnail.size)




###############################################

# # Lesson: Exercise: JPG to PNG Pokedex Converter


import sys
import os
from PIL import Image

# grab first and second argument

try:
    first_arg = sys.argv[1]
    second_arg = sys.argv[2]
except: pass

# Check if second argument exists, if not create it
if not os.path.exists(second_arg):
    os.makedirs(second_arg, exist_ok=True)

accessable_file = os.listdir(first_arg)

for img in accessable_file :
    if img.endswith(".jpg"):
        # 1. Open the image using the FULL path (using comma-separated join)
        source_path = os.path.join(first_arg, img)
        default_img = Image.open(source_path)
        # 2. Get the name string (splitting the filename, not the image object)
        name_of_img = os.path.splitext(img)[0]
        # 3. Create the destination path (using comma-separated join)
        destination_path = os.path.join(second_arg, name_of_img + ".png")
        # 4. Save the actual image object to the destination path
        default_img.save(destination_path)


# Loop trough the first argument folder

# and convert all the images to png

# and save those converted png images to a new folder that is the second argument. 



###############################################

# # Lesson: