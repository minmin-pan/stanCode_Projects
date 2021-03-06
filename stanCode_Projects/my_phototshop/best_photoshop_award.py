"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage
# Controls the threshold of detecting white screen pixel
THRESHOLD = 0.93
# Controls the upper bound for black pixel
BLACK_PIXEL = 320


def combine(bg, me):
    """
    : param1 bg: SimpleImage, the background image
    : param2 me: SimpleImage, green screen figure image
    : return me: SimpleImage, the white screen pixels are replaced by pixels of background image
    """
    for y in range(me.height):
        for x in range(me.width):
            pixel_me = me.get_pixel(x, y)
            avg = (pixel_me.red+pixel_me.blue+pixel_me.green) // 3
            total = pixel_me.red+pixel_me.blue+pixel_me.green
            if pixel_me.green > avg * THRESHOLD and pixel_me.red > avg * THRESHOLD and pixel_me.blue > avg * THRESHOLD \
                    and total > BLACK_PIXEL:
                pixel_bg = bg.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
    return me


def main():
    """
    This function conducts white screen replacement
    which is able to photoshop a person onto any background
    -----------------------------------------------------------
    This picture was created in the hope that through prayer,
    all darkness can be quickly ended and light can be regained.
    """
    fg = SimpleImage('image_contest/3.jpg')
    bg = SimpleImage('image_contest/8.jpg')
    bg.make_as_big_as(fg)
    combined_img = combine(bg, fg)
    combined_img.show()



if __name__ == '__main__':
    main()
