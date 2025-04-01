📂 Sortify - Advanced File Sorting Tool 🧹

Sortify is a command-line tool designed to help you organize files into appropriate categories and subcategories with ease. It supports multiple sorting options, including sorting by file types, managing subcategories, and removing empty folders. It's built to make your file management more efficient!
________________________________________
🚀 Features

•	Sort files by type (e.g., .jpg, .pdf, .cpp, etc.) into predefined categories.
•	Subcategory sorting: Move files into subfolders based on their types (e.g., Java and C++ files in the "Code" category).
•	Empty folder removal: Delete empty folders after sorting files.
•	Flexible depth sorting: Sort files in specified directory depths.
•	File conflict resolution: Automatically rename duplicate files (e.g., file.txt becomes file1.txt).
•	Move files to the main directory: Move all files from subdirectories to the main directory and remove empty directories.
________________________________________
🛠️ Installation

You can easily use this tool by cloning the repository and running the script in your terminal.
1.	Clone the repository:
2.	git clone https://github.com/M-INDN-SEDTA/Sortify.git
3.	Navigate to the project directory:
4.	cd Sortify
5.	Run the script using Python:
6.	python sort.py [options]
________________________________________
📑 Usage

Here’s how you can use Sortify to keep your files well-organized:
1. Sort files by type into category folders
Sorts all files into their appropriate categories like Documents, Images, Videos, etc.
python sort.py
This will move all files in the current directory and subdirectories into their respective category folders.
________________________________________
2. Sort files in specific directories by depth
Use the -d flag to define the depth range. For example, -d 01 will sort files from the current directory and 1 level of subdirectories.
python sort.py -d 01
Use Case: If you only want to sort files in the current folder and its immediate subdirectories.
________________________________________
3. Sort files and create subfolders for specific file types
Use the -sb flag to sort files into subfolders based on file extensions within the categories.
python sort.py -sb
This will create subfolders inside each category folder for specific file types. For example, .cpp and .java files will be moved into Code/Java or Code/C++ subfolders.
________________________________________
4. Move files from subfolders to the main directory and remove empty directories
Use the -sr flag to move all files from subdirectories to the main directory and then delete the empty subdirectories. Combine with -srm to remove all empty folders in the main directory.
python sort.py -sr -srm
Use Case: This will sort all files into category folders and then delete any empty folders in the main directory.
________________________________________
5. Include or exclude specific folders/files
You can specify which folders or files to include or exclude from the sorting process.
python sort.py -i folder1 file.txt -e folder2
•	-i includes specific folders or files for sorting.
•	-e excludes specific folders or files from sorting.
________________________________________
6. Remove empty folders after sorting
Use the -em flag to delete empty folders that are left behind after the files are moved.
python sort.py -em
This will remove any empty folders from the directory, helping you keep your file structure clean.
________________________________________
7. Save removed folders to a log file
Whenever a folder or file is deleted, the tool will log the names of those folders into a text file called SortTool_removedFolders.txt.
________________________________________
⚙️ Arguments/Flags

Flag	Description	Example
-d <depth>	Set the depth range for sorting	-d 01 (Sort from current directory and 1 level subdirectory)
-sr	Move files from subdirectories to the main directory	-sr
-sc	Sort files within their respective subdirectories	-sc
-sb	Sort files into subfolders based on their file extensions	-sb
-srm	Remove empty subfolders when moving files to the main directory	-srm
-em	Remove empty folders after sorting	-em
-i <folders/files>	Include specific folders/files to be sorted	-i folder1 file.txt
-e <folders/files>	Exclude specific folders/files from sorting	-e folder2
-ic	Include the current directory in sorting	-ic
-ec	Exclude the current directory from sorting	-ec
________________________________________
🌍 Use Case Examples

Example 1: Sort files by category in the current directory
Sort all files in the current directory into category folders like Documents, Images, etc.
python sort.py
Example 2: Sort files within a subdirectory up to 2 levels
Sort files in the current directory and 2 levels of subdirectories, creating category folders.
python sort.py -d 02
Example 3: Move files from subdirectories to the main directory and delete empty folders
Move all files from subdirectories to the main directory and delete any empty folders afterward.
python sort.py -sr -srm
________________________________________
📝 Important Notes

•	The script does not overwrite existing files unless specified, and duplicate files will be renamed (e.g., file.txt becomes file1.txt).
•	If you want to sort only certain files or directories, you can use the -i flag to include them and the -e flag to exclude them.
•	Always double-check before using the -srm or -em flags, as they will delete folders from your file system.
________________________________________
🎉 Contributing

Feel free to contribute to Sortify by forking the repository, making improvements, and submitting pull requests. Any help to improve the functionality or add more sorting features is greatly appreciated!
________________________________________
📄 License

This tool is licensed under the MIT License. See the LICENSE file for more details.
________________________________________
🌟 Acknowledgments
Special thanks to all contributors for their support and feedback. Thanks for using Sortify to organize your files efficiently! 🙌
________________________________________
✨ Happy Sorting! ✨

