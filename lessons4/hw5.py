import sys
import pathlib


def recursive_print(path):
    if path.is_dir():
        for el in path.iterdir():
            recursive_print(el)
    else:
        files.append(path.name)
    sorting()


def sorting():
    
    global music, images, video, documents, other_files, archive
    new_files, archive, music, images, video, documents, other_files = [], [], [], [], [], [], []

    audio_file_format = ['mp3', 'ogg', 'wav', 'amr']
    image_file_format = ['jpeg', 'png', 'jpg', 'svg']
    video_file_format = ['avi', 'mp4', 'mov', 'mkv']
    documents_file_format = ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx']
    archive_file_format = ['zip', 'gz', 'tar']

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
        elif new_files[i].split('.')[-1] in archive_file_format:
            archive.append(files[i])
        else:
            other_files.append(files[i])

         
def main():
    path = sys.argv[1]
    path = pathlib.Path(path)
    recursive_print(path)
    print(f"""Music:       {music}
Images:      {images}
Video:       {video}
Documents:   {documents}
Archive:     {archive}
Other_files: {other_files}""")
    
files = []

if __name__ == '__main__':
    main()

