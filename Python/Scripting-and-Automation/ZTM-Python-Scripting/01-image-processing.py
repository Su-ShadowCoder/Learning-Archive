###############################################

# Lesson: Images With Python

from PIL import Image, ImageFilter

# #  asiging a filter to the image
# img = Image.open('./photos/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save("blur.png", "png")

# img = Image.open('./photos/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img.save("SHARPEN.png", "png")

# converting image to grey
img = Image.open('./photos/pikachu.jpg')
filtered_img = img.convert('L')
filtered_img.save("grey2.png", 'png')

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

