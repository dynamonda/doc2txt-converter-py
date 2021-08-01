import sys
import os
import docx2txt

path: str = ""
output_dir: str = "./word2txt/"


def get_file_name(path: str) -> str:
    return os.path.splitext(os.path.basename(path))[0]


def convert2txt(path: str) -> str:
    return docx2txt.process(path)


def write_txt(text: str, filename: str):
    if os.path.exists(output_dir):
        fullpath = os.path.join(output_dir, filename+'.novel')
        print(fullpath)
        with open(fullpath, "w", encoding="utf-8") as f:
            f.write(text)


def main():
    print("Start docx2txt")
    file_name = get_file_name(path)
    if os.path.exists(path):
        doctxt = convert2txt(path)
        write_txt(doctxt, file_name)


if __name__ == '__main__':
    args = sys.argv

    if len(args) == 2:
        path = args[1]
        main()
    else:
        print('Error, docxのパスを付けてください。')
