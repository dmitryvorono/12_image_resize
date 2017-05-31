import argparse
import sys


def create_parser():
    parser = argparse.ArgumentParser(description='This script resize images')
    parser.add_argument('image', type=str, help='Path to file will resize')
    parser.add_argument('-o', '--output', type=str, help='Path to output file')
    parser.add_argument('--width', type=int, help='width result image')
    parser.add_argument('--height', type=int, help='height result image')
    parser.add_argument('--scale', type=float, help='scale result image')
    return parser


def resize_image(image, output, width, height, scale):
    pass

if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    if(args.width or args.height) and args.scale:
        sys.exit('--wigth and --height|--scale are mutually exclusive')
    resize_image(**vars(args))
