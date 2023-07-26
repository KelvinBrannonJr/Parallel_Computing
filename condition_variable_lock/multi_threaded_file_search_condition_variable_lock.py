import os
from os.path import isdir, join
from threading import Lock, Thread
from wait_group import WaitGroup

mutex = Lock()
matches = []


def file_search(root, filename, wait_group):
    print("Searching in:", root)
    try:
        for file in os.listdir(root):
            full_path = join(root, file)
            if filename in file:
                mutex.acquire()
                matches.append(full_path)
                mutex.release()
            if isdir(full_path):
                wait_group.add(1)
                t = Thread(target=file_search, args=([full_path, filename, wait_group]))
                t.start()
        wait_group.done()

    except PermissionError as e:
        print(f"Unable to search {root} : {e}")
        pass


# Take the Secret_File.txt in the joins directory
    # hide it in your root directory on the hard-drive
def main():
    wait_group = WaitGroup()
    wait_group.add(1)
    t = Thread(target=file_search, args=([r"D:\\Python\\", "Secret_File.txt", wait_group]))
    t.start()
    wait_group.wait()
    for m in matches:
        print("Matched:", m)


main()
