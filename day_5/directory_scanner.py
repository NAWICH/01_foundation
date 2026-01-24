#ask user for a directory path
#loop through every file in that folder
#get the size of each file in bytes
#convert bytes to MB
#print summary : total number of files, total size of the directory, list of the top 3 largest files found

import os

def get_dir():
    path1 = input("Enter the directory path you want to scan: ")
    if not os.path.exists(path1):
        print("Directory doesn't exist")
        return None
    return path1

def get_summary(path1):
    total = 0
    file_num = 0
    list_dir = {}
    for file in os.listdir(path1):
        full_path = os.path.join(path1, file)

        if os.path.isfile(full_path):
            size = os.path.getsize(full_path)
            total += size
            file_num += 1
            list_dir[file] = size

    total_mb = total / (1024 * 1024)

    print(f"Total number of file is {file_num}\nTotal size of directory is {total_mb:.4f}MB")

    sorted_files = sorted(list_dir.items(), key = lambda x:x[1], reverse=True)

    print("\n Top 3 Largest Files:")
    for name,size in sorted_files[:3]:
        print(f"{name}: {size / (1024 * 1024):.4f}MB")


def main():
    path1 = get_dir()
    get_summary(path1)
if __name__ == "__main__":
    main()


    