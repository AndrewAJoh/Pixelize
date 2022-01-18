from PIL import Image, ImageDraw

def average_color(x_pixel, y_pixel, chunk_size, image):
    r, g, b = 0, 0, 0
    count = 0

    for i in range(x_pixel, x_pixel + chunk_size):
        for j in range(y_pixel, y_pixel + chunk_size):
            red, green, blue = image.getpixel((i, j))
            r += red
            g += green
            b += blue
            count += 1

    return [r // count, g // count, b // count]

def resize(image, width, height, chunk_size):

    while (width % chunk_size != 0):
        width -= 1
    
    while (height % chunk_size != 0):
        height -= 1

    image = image.resize((width, height))
    
    return [image, width, height]

def pixelize(image, chunk_size):
    if chunk_size <= 1:
        return image

    image_width = image.size[0]
    image_height = image.size[1]

    if (chunk_size > (image_width / 2) or chunk_size > (image_height / 2)):
        return image

    if (image_width % chunk_size != 0 or image_height % chunk_size != 0):
        resized_image = resize(image, image_width, image_height, chunk_size)
        image = resized_image[0]
        image_width = resized_image[1]
        image_height = resized_image[2]

    idraw = ImageDraw.Draw(image)
    chunk_rgb = [0, 0, 0]
    height_iter = 0

    for i in range(0, image_height, chunk_size):
        width_iter = 0
        for j in range(0, image_width, chunk_size):
            x_pixel = chunk_size * width_iter
            y_pixel = chunk_size * height_iter
            chunk_rgb = average_color(x_pixel, y_pixel, chunk_size, image)
            idraw.rectangle([(x_pixel, y_pixel), (x_pixel + (chunk_size - 1), y_pixel + (chunk_size - 1))], fill=(chunk_rgb[0], chunk_rgb[1], chunk_rgb[2]))
            width_iter += 1
        height_iter += 1

    return image