import sys          # program variables 
import os
import subprocess

project_directory= r'C:\Users\manib\Documents'

# print(os.getcwd())
os.chdir(project_directory)
# print(os.getcwd())

# print(sys.argv)

# print(project_name)
# print(project_type)

type_={
    'python':'.py',
    'py': '.py',
    'java': '.java',
    'c++' : '.cpp',
}

def create_folder(project_name):
    files_folders= os.listdir()

    if project_name in files_folders:
        print(f"folder {project_name} already exists!")         # f --> formatted string
    else:
        # os.mkdir(folder name ) creates a folder
        os.mkdir(project_name)
        

def create_file(project_type,program_name):
    filename = f'{program_name}{type_[project_type]}'

    files_folders= os.listdir()
    if filename in files_folders:
        print(f"file {program_name} already exists!")         # f --> formatted string
    
    else:
        # a --> append demo.txt  
        # r --> demo.txt        # read 
        # w- -> demo.txt --->   # write 
        f = open(filename , 'a') 
        print(f"{filename} created!")
        f.close()           
        
# --- main program starts here------------------------------------------ !

if len(sys.argv) == 4:
    project_name = sys.argv[1]
    project_type = sys.argv[2]
    program_name = sys.argv[3]

    create_folder(project_name)

    os.chdir(f'{project_name}')

    create_file(project_type,program_name)

    # os.system(' command' )
    os.system('code .')

elif len(sys.argv) == 2:
    project_name = sys.argv[1]
    create_folder(project_name)
    os.chdir(f'{project_name}')
    os.system('code .')

else:
    print("Error : not enough details !")   


