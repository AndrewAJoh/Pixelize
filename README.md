### Pixelize
# Convert an image to its pixelated form.

Pixelize is a fun python utility based on the Python Imaging Library (PIL) that converts a picture into a lower resolution.

<img src="https://imgur.com/a/zkKbQMw">

<img src="https://imgur.com/a/bgy39dJ">


# Requirements
Pixelize requires pillow to run. See https://pillow.readthedocs.io/en/stable/installation.html#old-versions for instructions to install.

# Usage
Insert this line of code to the beginning of your script to use the pixelize() function:
from pixelize import *

# Function Definition
def pixelize(image, chunk_size): returns a pillow Image object that has been pixelized

image [Image object] - see pillow documentation
chunk_size [int] - the length, in pixels, of the sides of each chunk in the generated photo. A chunk_size of 1 returns the original photo.
