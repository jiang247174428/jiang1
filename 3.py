﻿
import os
# root_path = os.getcwd()
# offset = len(root_path.split("\\"))
# for root,dirs,files in os.walk(root_path):
# 	current_dir = root
# 	path_list = current_dir.split("\\")
# 	indent_level = len(path_list) - offset
# 	print("\t"*indent_level,"\\"+path_list[-1])
# 	# print(length,len(length))   #len()显示列表长度
# 	for f in files:
# 		filename = os.path.splitext(f)[0]   #输出文件名取第0个文件赋予filename名字 
# 		file_path =of.path.join(root,f)
# 		print(file_path)   #获取root绝对路径

file_path = r'C:\Users\Administrator\Desktop\root\root\dir1\cp3_data_size.c'

def line_count(file_path):
	code_line,blank_line = 0,0
	
	with open(file_path,'r') as fp:
		while True:
			line = fp.readline()
			if not line:
				break
			code_line+=1
	print(code_line,"line")
line_count(file_path)
	
