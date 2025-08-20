import os
import shutil



def copy_files(current_path, desination_dir):

    if not os.path.exists(desination_dir):
        os.mkdir(desination_dir)


    for filename in os.listdir(current_path):

        from_path = os.path.join(current_path, filename)
        dest_path = os.path.join(desination_dir, filename)

        print(f" * {from_path} -> {dest_path}")


        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files(from_path, dest_path)
