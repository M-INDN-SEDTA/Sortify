import os
import shutil
import argparse

# Define file categories and extensions
CATEGORIES = {
    "Documents": [".doc", ".docx", ".pdf", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".cs", ".php"],
    "Executables": [".exe", ".msi", ".sh", ".bat", ".apk"],
    "Data": [".csv", ".json", ".xml", ".sql", ".db"],
    "Fonts": [".ttf", ".otf", ".woff"],
    "System": [".dll", ".sys", ".bak", ".tmp", ".log"],
    "Others": [".dat", ".bin", ".cfg"]
}

def get_category(file_ext):
    """Get category for a given file extension."""
    for category, extensions in CATEGORIES.items():
        if file_ext in extensions:
            return category
    return "Others"

def log_removed_item(item_name):
    """Log deleted folder/file to 'SortTool_removedFolders.txt'."""
    with open("SortTool_removedFolders.txt", "a") as log_file:
        log_file.write(f"{item_name}\n")

def should_sort_folder(path, include_list, exclude_list, exclude_current):
    """Determine if a folder should be sorted based on include/exclude rules."""
    base_name = os.path.basename(path)
    if exclude_current and path == os.getcwd():
        return False
    if include_list and base_name not in include_list:
        return False
    if exclude_list and base_name in exclude_list:
        return False
    return True

def move_files_to_category(folder, sort_more, subcategory):
    """Move files into category folder or subcategory folder."""
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1]
            category = get_category(file_ext)
            
            # Main directory and category folder
            category_folder = os.path.join(os.getcwd(), category)
            os.makedirs(category_folder, exist_ok=True)

            if subcategory:
                # Create subcategory folder within the category
                subcategory_folder = os.path.join(category_folder, file_ext[1:].upper())
                os.makedirs(subcategory_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(subcategory_folder, file))
                print(f"Moved {file} → {subcategory_folder}")
            else:
                shutil.move(file_path, os.path.join(category_folder, file))
                print(f"Moved {file} → {category_folder}")

def move_files_from_subcategory_to_parent(folder, category_folder):
    """Move files from subcategory folders to the main category folder."""
    for subfolder in os.listdir(category_folder):
        subfolder_path = os.path.join(category_folder, subfolder)
        if os.path.isdir(subfolder_path):
            for file in os.listdir(subfolder_path):
                file_path = os.path.join(subfolder_path, file)
                if os.path.isfile(file_path):
                    shutil.move(file_path, os.path.join(category_folder, file))
                    print(f"Moved {file} → {category_folder}")
            # After moving all files, remove the empty subcategory folder
            os.rmdir(subfolder_path)
            print(f"Removed empty subcategory folder: {subfolder_path}")

def remove_empty_folders_in_range(base_folder, depth_range):
    """Remove empty folders within the specified depth range."""
    for root, dirs, files in os.walk(base_folder, topdown=False):
        depth = root.count(os.sep) - base_folder.count(os.sep)

        # If depth is within the specified range
        if depth_range[0] <= depth <= depth_range[1]:
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                if dir_path != os.getcwd() and not os.listdir(dir_path):  # If it's empty and not the main folder
                    os.rmdir(dir_path)
                    log_removed_item(dir_path)
                    print(f"Removed empty directory: {dir_path}")

def remove_all_empty_folders(folder):
    """Remove all empty folders, including subfolders."""
    for root, dirs, files in os.walk(folder, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):  # If it's empty
                os.rmdir(dir_path)
                log_removed_item(dir_path)
                print(f"Removed empty directory: {dir_path}")

def scan_and_sort(base_folder, depth_range, sort_to_main, sort_more, remove_empty_dirs, remove_all_empty, subcategory, move_back_to_parent, include_list, exclude_list, exclude_current):
    """Scan folders based on depth and sort files accordingly."""
    for root, dirs, files in os.walk(base_folder):
        depth = root.count(os.sep) - base_folder.count(os.sep)
        
        if depth_range[0] <= depth <= depth_range[1]:
            if should_sort_folder(root, include_list, exclude_list, exclude_current):
                if sort_to_main:
                    move_files_to_category(root, sort_more, subcategory)
                elif move_back_to_parent:
                    category_folder = os.path.join(os.getcwd(), get_category(os.path.splitext(files[0])[1]))  # Assume files are in the same category
                    move_files_from_subcategory_to_parent(root, category_folder)
                
                # If sorting to main directory and remove empty folders flag is set, remove empty dirs
                if remove_empty_dirs and sort_to_main and depth == 1:
                    remove_empty_folders_in_range(root, depth_range)

    # Remove all empty folders after sorting if -em flag is set
    if remove_all_empty:
        remove_all_empty_folders(base_folder)

def main():
    parser = argparse.ArgumentParser(description="File Sorting Script")
    parser.add_argument("-d", type=str, default="0", help="Depth range (e.g., '01' for 0 to 1 depth)")
    parser.add_argument("-sr", action="store_true", help="Sort to main directory (move files from subdirectories to main)")
    parser.add_argument("-sc", action="store_true", help="Sort within each directory")
    parser.add_argument("-sm", action="store_true", help="Sort more into subfolders within categories")
    parser.add_argument("-srm", action="store_true", help="Remove empty directories when sorting to main directory")
    parser.add_argument("-em", action="store_true", help="Remove empty folders after sorting within the specified depth range")
    parser.add_argument("-sb", action="store_true", help="Sort files into subcategories")
    parser.add_argument("-sbr", action="store_true", help="Move all files from subcategories back to parent category")
    parser.add_argument("-i", nargs="*", help="Include specific folders/files")
    parser.add_argument("-ic", action="store_true", help="Include current directory")
    parser.add_argument("-e", nargs="*", help="Exclude specific folders/files")
    parser.add_argument("-ec", action="store_true", help="Exclude current directory")
    
    args = parser.parse_args()
    
    # Parse depth range
    depth_range = (int(args.d[0]), int(args.d[1]) if len(args.d) > 1 else int(args.d[0]))
    
    # Sorting destination
    sort_to_main = args.sr
    sort_more = args.sm
    remove_empty_dirs = args.srm and sort_to_main and args.d == "0"
    remove_all_empty = args.em
    subcategory = args.sb
    move_back_to_parent = args.sbr
    
    # Include/exclude handling
    include_list = args.i if args.i else []
    exclude_list = args.e if args.e else []
    exclude_current = args.ec
    include_current = args.ic
    
    # Default to sorting current directory if no include/exclude flags are provided
    if not include_list and not exclude_list:
        include_current = True
    
    # Start sorting
    base_folder = os.getcwd()
    scan_and_sort(base_folder, depth_range, sort_to_main, sort_more, remove_empty_dirs, remove_all_empty, subcategory, move_back_to_parent, include_list, exclude_list, exclude_current)
    
    print("✅ Sorting completed!")
    
if __name__ == "__main__":
    main()
