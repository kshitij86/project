import os
import sys
import re
from PIL import Image
from PIL.ExifTags import TAGS
from text import responses

# Changed to report modification if exif data has 'Software' field.


def faker(filename):
    string = re.compile('Software')
    for param, value in Image.open(filename)._getexif().items():
        if string.search(str(TAGS.get(param))):
            return f"'{filename}'{responses[1]}'{value}'."
        else:
            continue
    return responses[0]


# The image must be in the same directory.
# filename can be passed a second argument.

filename = sys.argv[1]

try:
    print(faker(filename))
except Exception as e:
    print(f"Something went wrong : {e}")
