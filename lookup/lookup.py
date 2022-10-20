import sys
import os

PATH = os.path.expanduser('~')

def main():
    if len(sys.argv) > 1:
        search_text = sys.argv[1]
        found = False

        for root, dirs, files in os.walk(PATH):
            for file in files:
                if file.find(search_text) != -1 or file.capitalize().find(search_text) != -1 or \
                    file.lower().find(search_text) != -1 or file.upper().find(search_text) != -1:
                    name = os.path.join(root, file)
                    print(f'File found: {name}')
                    found = True
            for folder in dirs:
                if folder.find(search_text) != -1 or folder.capitalize().find(search_text) != -1 or \
                    folder.lower().find(search_text) != -1 or folder.upper().find(search_text) != -1:
                    name = os.path.join(root, folder)
                    print(f'Folder found: {name}')
                    found = True

        if not found:
            print('File or folder not found')

    else:
        print('Usage: lookup [search text]')


if __name__ == '__main__':
    main()

    