'''

@author: redtree

@contact: redtreec@gmail.com

@desc: you can input a picture and the merchine will describes this picture.


'''

import os
import sys

def download_model(path):
    print('download at' + path)

    process = os.popen(
        'cd ' + path)  # return file
    output = process.read()

    if output != None:
        process = os.popen(
            'python classify_image.py  --model_dir ' + path)  # return file
        output = process.read()
        print(output)
    else:
        print('error path , please check if yourpath exist')


def check(model_path, test_pic_path):
    process = os.popen(
        'python classify_image.py --model_dir ' + model_path + ' --image_file ' + test_pic_path)  # return file
    output = process.read()
    print('---------------------')
    print(output)
    print('---------------------')

    process.close()


def main(argv):
    if len(argv) ==1:
        print( 'USE:' + '\n' +
              'python img2txt [mode] [path1] [path2]' + '\n'
              + 'mode : download / check' + '\n' +
              'path' + '\n' +
              '1 when mode is download , ' + '\n' +
              'only take path1 as download_filepath ,' + '\n' +
              '2 when mode is check ' + '\n' +
              'take path1 as model_path and path2 as your test_image_path')

    elif argv[1] == 'download':
        if argv[2] == None:
            print('need write path')
        else:
            print('model downloading')
            download_model(argv[2])
            print('model download finish at' + argv[2])

    elif argv[1] == 'check':
        if argv[2] == None or argv[3] == None:
            print('error command')
        else:
            print('check_start')
            check(argv[2], argv[3])
            print('check_success!')

    else:
        print('error command '+'\n'+'USE:' +'\n' +
              'python img2txt [mode] [path1] [path2]' +'\n'
              + 'mode : download / check' +'\n'+
              'path' +'\n'+
              '1 when mode is download '+'\n'+
              'only take path1 as download_filepath '+'\n'+
              '2 when mode is check '+'\n'+
              'take path1 as model_path and path2 as your test_image_path')


if __name__ == '__main__':
    main(sys.argv)
