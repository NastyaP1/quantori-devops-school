# Homework 18
#
# https://github.com/CsteerDevops1/lectures_devops2/blob/main/Python/Homework/hw18.txt
#
# ###############################################################################
#
from PIL import Image
import sys, getopt


def main(argv):
    input_file = ''
    output_file = 'new_small_photo.jpg'
    percent = 0
    try:
        opts, args = getopt.getopt(argv, "hi:o:p:", ["ifile=", "ofile=", "percent="])
    except getopt.GetoptError:
        print('hw18.py -i <inputfile> -o <outputfile> -p <percent>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('hw18.py -i <inputfile> -o <outputfile> -p <percent>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
        elif opt in ("-p", "--percent"):
            percent = arg
    if input_file == '' or percent == 0:
        print('Not all mandatory settings are set')
        sys.exit(2)
    else:
        resize_image(input_image_path=input_file,
                     output_image_path=output_file,
                     percent_size=percent)


def resize_image(input_image_path, output_image_path, percent_size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    print('The original image size is {} wide x {} '.format(width, height))

    size = (int(width - width / 100 * int(percent_size)), int(height - height / 100 * int(percent_size)))

    resized_image = original_image.resize(size)
    resized_width, resized_height = resized_image.size
    print('The resized image size is {} wide x {} '.format(resized_width, resized_height))
    resized_image.save(output_image_path)


if __name__ == '__main__':
    main(sys.argv[1:])
