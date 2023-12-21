import os 

path = r"D:\paisa hi paisa\MongoDB Projects\IS601-F23-Milestone1\IS601-F23-006-Improved-List-Pages\IS601-F23-006-Improved-List-Pages\project\brokers"
def print_content(path):
    for root, dirs, files in os.walk(path):    
        for file in files:
            print("Filename: ",file,"\n")
            if file.endswith(".pyc"):
                continue
            with open(os.path.join(root, file), "r") as f:
                print(f.read()) 
                # pass


print_content(path)