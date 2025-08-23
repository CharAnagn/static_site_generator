import os
import shutil
from copy_dir_contents import copy_files
from markdown_blocks import generate_pages_recursive
import sys

dir_path_static = "./static"
dir_path_public = "./public"

def main():

    if (len(sys.argv) > 1):
        basepath = sys.argv[1]
    else:
        basepath = "/"

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files(dir_path_static, dir_path_public)

    generate_pages_recursive("content","template.html","docs", basepath)
main()
