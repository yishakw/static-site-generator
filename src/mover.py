import os
import shutil
src_dir = "/mnt/c/Users/DELL/workspace/github.com/yishakw/static_site_generator/static"
dest_dir = "/mnt/c/Users/DELL/workspace/github.com/yishakw/static_site_generator"
def copy_files(src_dir, dest_dir):
    if not os.path.exists(src_dir):
        raise FileNotFoundError(f"Source directory '{src_dir}' does not exist.")
    shutil.copytree(src_dir, dest_dir, dirs_exist_ok=True)
def remove_tree(path):
    if not path:
        raise ValueError("Path cannot be empty")
    path = os.listdir(path)
    for pat in path:
        if os.path.isdir(pat):
            shutil.rmtree(f"{path}/{pat}")
        else:
            os.remove(f"{path}/{pat}")
 
# copy_files(src_dir, dest_dir)

# remove_tree(f"{dest_dir}/index.css")
# remove_tree(f"{dest_dir}/images")