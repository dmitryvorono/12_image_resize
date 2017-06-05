# Image Resizer

This project resize an input image 

# Usage

usage: image_resize.py [-h] [-o OUTPUT] [--width WIDTH] [--height HEIGHT]
                       [--scale SCALE]
                       image

This script resize images

positional arguments:

  image                 Path to file will resize

optional arguments:

  -h, --help            show this help message and exit

  -o OUTPUT, --output OUTPUT
                        Path to output file

  --width WIDTH         width result image

  --height HEIGHT       height result image

  --scale SCALE         scale result image

# Examples

1. Thumbnail image wx1080.jpg to wx1080_540x540.jpg:

```#!bash
$ python image_resize.py wx1080.jpg --scale 0.5
```
2. Thumbnail image wx1080.jpg to wx1080_128x128.jpg (the proportional saved):

```#!bash
$ python image_resize.py wx1080.jpg --width 128
```

or

```#!bash
$ python image_resize.py wx1080.jpg --height 128
```

3. Thumbnail image wx1080.jpg to wx1080_800x600.jpg (the proportional did not save):

```#!bash
$ python image_resize.py wx1080.jpg --width 800 --height 600
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
