import subprocess as sp

def create_container():
    print("Fill the following questions including the file format, please:")
    video = str(input("Whats your input video name?"))
    audio = str(input("Whats your input audio name?"))

    line = "ffmpeg -i " + video + " -i " + audio + " -map 0 -map 1 encapsuledFile.mp4"

    return line