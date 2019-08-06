"""
Rename files from a folder
get: http://icarus.cs.weber.edu/~hvalle/hafb/prank.zip
"""
import os



def rename_files():
    """
    Rename files in a folder
    :return: nothing
    """
    folder_dir = r"C:\Users\CCEClass1.AD.000.001\Desktop\hafb\prankOrig" # r is for raw string. Ignores the special characters
    files = os.listdir(folder_dir)
    saved_path = os.getcwd()  # save current directory
    # go to the files' directory
    os.chdir(folder_dir)
    for file in files:
        # Remove digits from name
        new_file = file.lstrip('0123456789')
        os.rename(file,new_file)
        print("old name", file, "new name", new_file)
        # get back home
    os.chdir(saved_path)


def main():
    """
    test function
    :return: nothing
    """
    rename_files()


if __name__ == '__main__':
    main()
    exit(0)