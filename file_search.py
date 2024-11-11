import os

dirPath = r"E:\相片\2024"


def list_file(path):
    all_file = []
    set = []
    for f in os.listdir(path):
        all_file.append(f)
        set.append(f.split('.')[0])

    for name in set:
        if (name + '.JPG' in all_file) & ((name + '.CR3' in all_file) or (name + '.CR2' in all_file) or (name + '.RW2' in all_file)):
            delete_file_path = os.path.join(path, name + '.JPG')
            if os.path.exists(delete_file_path):
                # print(delete_file_path)
                os.remove(delete_file_path)


if __name__ == '__main__':
    for folder_name in os.listdir(dirPath):
        print(folder_name)
        list_file(os.path.abspath(os.path.join(dirPath, folder_name)))
        print('\r\n')
