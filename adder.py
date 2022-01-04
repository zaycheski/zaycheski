import random
import PIL.Image

ADD_FOLDER = "./ascii_images"

ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

def resize(image, new_width = 300):
    width, height = image.size
    new_height = int(new_width * height / width * 0.55)
    return image.resize((new_width, new_height))

def to_greyscale(image):
    return image.convert("L")

def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "";
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//25];
    return ascii_str

def main():
    path = input("Path to image file: ")

    desired_width = input("Desired image width (default 300): ")

    if len(desired_width) > 0:
        desired_width = int(desired_width)
    else:
        desired_width = 300

    try:
        image = PIL.Image.open(path)
    except:
        print(path, "Unable to find image ")
        return

    image = resize(image, desired_width);

    greyscale_image = to_greyscale(image)

    ascii_str = pixel_to_ascii(greyscale_image)
    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img=""

    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"

    print(ascii_img)

    ans = input("\n\n\n Do you want to save this version (y/n): ")
    if ans == 'y':
	    with open(ADD_FOLDER + "/" + "i_love_varya_" + str(random.randint(0, 1000000)), "w") as f:
	        f.write(ascii_img);
main()
