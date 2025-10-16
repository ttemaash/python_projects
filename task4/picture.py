from PIL import Image

image = Image.open("monro.jpg")
displacement = 50
red, green, blue = image.split()

coordinates_blue_channel_right = (0, 0, blue.width-displacement, blue.height)
blue_channel_right = blue.crop(coordinates_blue_channel_right)
coordinates_blue_channel_middle = (displacement//2, 0, blue.width-displacement//2, blue.height)
blue_channel_middle = blue.crop(coordinates_blue_channel_middle)
blue_blank = Image.blend(blue_channel_right, blue_channel_middle, 0.5)

coordinates_red_channel_left = (displacement, 0, red.width, red.height)
red_channel_left = red.crop(coordinates_red_channel_left)
coordinates_red_channel_middle = (displacement//2, 0, red.width-displacement//2, red.height)
red_channel_middle = red.crop(coordinates_red_channel_middle)
red_blank = Image.blend(red_channel_left, red_channel_middle, 0.5)

coordinates_green_channel_middle = (displacement//2, 0, green.width-displacement//2, green.height)
green_blank = green.crop(coordinates_green_channel_middle)

blank_pictures = (red_blank,green_blank,blue_blank)
full_size_image = Image.merge("RGB",blank_pictures)
full_size_image.save("ava_test_full.jpg")
full_size_image.thumbnail((80, 80))
full_size_image.save("ava_test_final.jpg")


