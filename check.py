import shutil
import os
dirc = "D:\Semesters\Winter_Semester_2019-2020\OOAD"

desti = "D:\Semesters\Winter_Semester_2019-2020\OOAD\cat-1"
# print(os.getcwd())

os.chdir(dirc)

# print(os.getcwd())

file = os.listdir();
src = file[1]
# print(file) 
# print(src)
shutil.move(src,desti)
