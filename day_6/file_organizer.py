#map the categories
#loop through a messy directory
#check if the destinatio folder exists if not create it
#move the file
#keep the count of how many files were moved to reach category and print a final report
import os
import shutil
storage = {
    "Images": [".jpg", ".png", 'jpeg', 'gif'],
    "Docs": [".pdf", '.docx', '.txt', '.xlsx'],
    "Archives": ['.zip', '.tar.gz', '.rar'],
    'Scripts': ['.py', '.sh', '.cpp', '.c', '.js']
}

def get_directory():
    path1 = input("Enter the path you want to organize: ")

    if os.path.exists(path1):
        return path1
    print("Path doesn't exist, Please try agian")

def move_to_category(category, org_path, base_path):
    mv_path = os.path.join(base_path, category)
    if not os.path.exists(mv_path):
        os.makedirs(mv_path)

    filename  = os.path.basename(org_path)
    dest_path = os.path.join(mv_path, filename)

    shutil.move(org_path, dest_path)


def search_dir(storage_map, path1): 
    report = {key: 0 for key in storage_map.keys()}
    report["Others"] = 0
    for file in os.listdir(path1):
        full_path = os.path.join(path1, file)   

        if os.path.isdir(full_path):
            continue

        root, ext = os.path.splitext(file)
        ext = ext.lower()

        found_category = "Others"
        for category, extention in storage_map.items():
            if ext in extention:
                found_category = category
                break
        move_to_category(found_category, full_path, path1)
        report[found_category] +=1
    
    for cat, count in report.items():
        if count > 0:
            print(f"{cat} : {count} files moved \n")
    
    
if __name__ == "__main__":
    get_path = get_directory()
    search_dir(storage, get_path)
