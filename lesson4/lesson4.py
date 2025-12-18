from PIL import Image

image = Image.open('monro.jpg')
red_image, green_image, blue_image = image.split()

coordinates_left = (100, 0, image.width, image.height)
coordinates_middle = (50, 0, image.width-50, image.height)
coordinates_right = (0, 0, image.width-100, image.height)

image_left = red_image.crop(coordinates_left)
image_middle = red_image.crop(coordinates_middle)
new_image_red = Image.blend(image_left, image_middle, 0.3)

image_right = blue_image.crop(coordinates_right)
image_middle = blue_image.crop(coordinates_middle)
new_image_blue = Image.blend(image_right, image_middle, 0.3)

new_image_green = green_image.crop(coordinates_middle)

final_image = Image.merge('RGB', (new_image_red, new_image_green, new_image_blue))

final_image.save('new_monro.jpg')
final_image.thumbnail((80, 80))
final_image.save('avatar.jpg')