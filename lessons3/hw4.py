import os
import sys

# path содержит первый аргумент, считаем, что это валидный адрес в файловой системе
path = sys.argv[1]
print(f"Start in {path}")
# files - это список имен файлов и папок в path.
files = os.listdir(path)

new_files = []

music = []
images = []
video = []
documents = []
other_files = []

audio_file_format = ['mp3', 'ogg', 'wav', 'amr']
image_file_format = ['jpeg', 'png', 'jpg']
video_file_format = ['avi', 'mp4', 'mov']
documents_file_format = ['doc', 'docx', 'txt']

new_files = files.copy()
new_files = [(z.lower()) for z in new_files]

for i in range(len(new_files)):
    if new_files[i].split('.')[-1] in audio_file_format:
        music.append(files[i])
    elif new_files[i].split('.')[-1] in image_file_format:
        images.append(files[i])
    elif new_files[i].split('.')[-1] in video_file_format:
        video.append(files[i])
    elif new_files[i].split('.')[-1] in documents_file_format:
        documents.append(files[i])
    else:
        other_files.append(files[i])

print(f"music:       {music}")
print(f"images:      {images}")
print(f"video:       {video}")
print(f"documents:   {documents}") 
print(f"other_files: {other_files}")

