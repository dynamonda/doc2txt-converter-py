import sys
import docx2txt

path: str = ""

def convert2txt(path: str)->str:
    return docx2txt.process(path)

def main():
    print("Start docx2txt")
    print(path)
    doctxt = convert2txt(path)
    print(doctxt)
    
if __name__ == '__main__':
    args = sys.argv

    if len(args) == 2:
        path = args[1]
        main()
    else:
        print('Error, docxのパスを付けてください。')
