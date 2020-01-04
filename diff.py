from PIL import Image, ImageChops, ImageDraw
point_table = ([0] + ([255] * 255))

def new_gray(size, color):
    img = Image.new('L',size)
    dr = ImageDraw.Draw(img)
    dr.rectangle((0,0) + size, color)
    return img

def black_or_b(a, b, opacity=0.85):
    diff = ImageChops.difference(a, b)
    diff = diff.convert('L')
    thresholded_diff = diff
    for repeat in range(3):
        thresholded_diff  = ImageChops.add(thresholded_diff, thresholded_diff)
    h,w = size = diff.size
    mask = new_gray(size, int(255 * (opacity)))
    shade = new_gray(size, 0)
    new = a.copy()
    new.paste(shade, mask=mask)
    
    new.paste(b, mask=thresholded_diff)
    return new


a = Image.open('xx.jpg')
b = Image.open('xy.jpg')
c = black_or_b(a, b)
c.save('c.jpg')