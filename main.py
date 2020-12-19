# This is a sample Python script.

import subprocess as sp
from create_container import create_container

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    opt = int(input('    ~~~~~~  MAIN MENÚ  ~~~~~~\n\n'
                 'Choose a function to aply to the BBB video:'
                 '\n 1. Encapsulate the given tracks.'
                 '\n 2. Encapsulate 2 tracks at will.'
                 '\n \nChoose a number between 1 and 2: '))
    if opt == 1:
        line = 'ffmpeg -i cut_video.m4v -i cut_mono.m4v -i cut_lowbitrate.m4v -map 0:0 -map 1 -map 2 -map -vf 1min_of_bbb.mp4'

    elif opt == 2:
        line = create_container()

    else:
        print('Try again with another number')
        exit()

    sp.run(line, shell=True)

