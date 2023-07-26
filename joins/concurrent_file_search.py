import os
from os.path import isdir, join

matches = []


def file_search(root, filename):
    print("Searching in:", root)
    try:
        for file in os.listdir(root):
            full_path = join(root, file)
            if filename in file:
                matches.append(full_path)
            if isdir(full_path):
                file_search(full_path, filename)
    except PermissionError as e:
        print(f"Unable to search {root} : {e}")
        pass


# Take the Secret_File.txt in the joins directory
    # hide it in your root directory on the C:\ drive
def main():
    file_search("C:\\Users\\", "Secret_File.txt")
    for m in matches:
        print("Matched:", m)


main()
