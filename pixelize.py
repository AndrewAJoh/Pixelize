from PIL import Image, ImageDraw

def average_color(x, y, n, image, im):
    r, g, b = 0, 0, 0
    count = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            red, green, blue = im.getpixel((i, j))
            r += red
            g += green
            b += blue
            count +=1
    return [r//count, g//count, b//count]

def resize(im, width, height, n):
    decrease_width = 0
    decrease_height = 0
    while (width % n != 0):
        width -= 1
        decrease_width += 1
    while (height % n != 0):
        height -= 1
        decrease_height += 1
    im = im.resize((width, height))
    print("We had to resize your image.")
    print("The width decreased by " + str(decrease_width) + " pixels.")
    print("The height decreased by " + str(decrease_height) + " pixels.")
    return [im, width, height]

def pixelize(file, n):
    im = Image.open(file)
    
    width_iter = 0
    height_iter = 0
    rgb = [0, 0, 0]
    image_size = im.size
    width = image_size[0]
    height = image_size[1]
    if (width%n != 0 or height%n != 0):
        result = resize(im, width, height, n)
        im = result[0]
        width = result[1]
        height = result[2]
    idraw = ImageDraw.Draw(im)
    for s in range(0, height, n):
        width_iter=0
        for t in range(0, width, n):
            current_x = n*width_iter
            current_y = n*height_iter
            rgb = average_color(current_x, current_y, n, file, im)
            idraw.rectangle([(current_x, current_y), (current_x+n, current_y+n)], fill=(rgb[0], rgb[1], rgb[2]))
            width_iter +=1
        height_iter +=1
    im.show()



    #idraw.rectangle([(x, y), (n, n)], fill=(r//count, g//count, b//count), outline=(0, 0, 0))
