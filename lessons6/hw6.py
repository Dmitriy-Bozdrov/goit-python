import sys
import pathlib
import shutil
import os
import re


def recursive_print(path):
    
    if path.is_dir():
        for el in path.iterdir():             
            recursive_print(el)
    else:
        normalize(path) #translate

       
def normalize(path):
    d = os.path.split(path)
    a = str(d[0])
    s = ''.join((d[1].split('.'))[:-1])
    
    my_set = s.maketrans("абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
                         "abvgdeëžzijklmnoprstufhcčššъyьèûâ")
    my_list = []
    for el in s:           
        if el == el.lower():
            d = el.translate(my_set)
        elif el == el.upper():
            d = el.lower().translate(my_set).upper()
        my_list.append(d)

    k = re.sub(r'(\W)', '_', ''.join(my_list))
    z = k + path.suffix
    q = pathlib.Path(a).joinpath(z)
    o = os.rename(path, q)
    
    try:
        sorting(q)# sort
    except:
        pass

def sorting(path):

    audio_file_format = ['mp3', 'ogg', 'wav', 'amr']
    image_file_format = ['jpeg', 'png', 'jpg', 'svg']
    video_file_format = ['avi', 'mp4', 'mov', 'mkv']
    documents_file_format = ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx']
    archive_file_format = ['zip', 'gz', 'tar']

    if (path.name.split('.'))[-1] in audio_file_format:
        shutil.move(path, 'C:\\test\\music')
    elif (path.name.split('.'))[-1] in image_file_format:
        shutil.move(path, 'C:\\test\\images')
    elif (path.name.split('.'))[-1] in video_file_format:
        shutil.move(path, 'C:\\test\\video')
    elif (path.name.split('.'))[-1] in documents_file_format:
        shutil.move(path, 'C:\\test\\documents')
    elif (path.name.split('.'))[-1] in archive_file_format:
        creating_folders = "C:\\test\\archive\\{}".format(*(path.name.split('.')[:-1]))
        shutil.unpack_archive(path, creating_folders)


def drop_empty_folders(directory):

    for dirpath, dirnames, filenames in os.walk(directory, topdown=False):
        if not dirnames and not filenames:
            os.rmdir(dirpath)            

def main():
    path = sys.argv[1]
    path_1 = pathlib.Path(path)
    recursive_print(path_1)
    drop_empty_folders(path) #del


if __name__ == '__main__':
    main()

