from textnode import TextNode, TextType
import os
import shutil

def main():
    static_to_public()

def copy_files(src, dst):
    for entry in os.listdir(src):
        entry_path = os.path.join(src, entry)
        dst_path = os.path.join(dst, entry)
        if os.path.isdir(entry_path):
            if not os.path.exists(dst_path):
                os.makedirs(dst_path)
                print(f"Created directory {dst_path}.")
            copy_files(entry_path, dst_path)
        else:
            print(f"Copying {entry} to {dst_path}.")
            shutil.copy(entry_path, dst_path)

def static_to_public():
    print(os.listdir("static"))
    
    if os.path.exists("public"):
        print("public directory already exists. Checking if it is empty...")
        
        if os.listdir("public") == []:
            print("public directory is empty and ready for file transfer.")
        
        else:
            print("public directory is not empty. Deleting and recreating it...")
            shutil.rmtree("public")
            os.makedirs("public")
            print("public directory deleted and recreated.")
    
    else:
        print("public directory does not exist. Creating it...")
        os.makedirs("public")
        print("public directory created.")
    
    
    print("Copying from static to public directory...")
    copy_files("static", "public")
    print("File transfer complete.")
    
    
           
main()
