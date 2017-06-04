import argparse
import sys
import os
from PIL import Image


def create_parser():
    parser = argparse.ArgumentParser(description='This script resize images')
    parser.add_argument('image', type=str, help='Path to file will resize')
    parser.add_argument('-o', '--output', type=str, help='Path to output file')
    parser.add_argument('--width', type=int, help='width result image')
    parser.add_argument('--height', type=int, help='height result image')
    parser.add_argument('--scale', type=float, help='scale result image')
    return parser


def rescale_image(im, scale):
    return im.resize((int(size * scale) for size in im.size))


def resize_image(im, width, height):
    proportional = im.size[0]/im.size[1]
    if width and not height:
        height = round(width / proportional)
    elif height and not width:
        width = round(height * proportional)
    new_size = (width, height)
    return im.resize(new_size)


def add_suffix_to_filename(filepath, suffix):
        folder, filename = os.path.split(filepath)
        name, extension = filename.split('.')
        return ''.join([folder, name, suffix, '.', extension])


def is_equal_proportional(old_image, new_image):
    old_size = old_image.size
    new_size = new_image.size
    if old_size[0] / old_size[1] != new_size[0] / new_size[1]:
        return False
    else:
        return True


def main(image, output, width, height, scale):
    im = Image.open(image)
    if width or height:
        new_image = resize_image(im, width, height)
    elif scale:
        new_image = rescale_image(im, scale)
    if not is_equal_proportional(im, new_image):
        print('Warning: proportinal new image is not equal to the original image')
    if not output:
        output = add_suffix_to_filename(image, '__{0}x{1}'.format(*new_image.size))
    new_image.save(output)
    return 0


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    if(args.width or args.height) and args.scale:
        sys.exit('--wigth and --height|--scale are mutually exclusive')
    status = main(**vars(args))
    sys.exit(status)
