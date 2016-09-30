import os
import requests
from urllib.parse import urljoin
import sys
# def getAbsPath(name):

def move(src,dest):
	extn='txt'
	# print ('hee')
	# src=os.path.dirname(os.path.abspath(__file__))
	# print (src)
	# dest=os.path.dirname(os.path.abspath(__file__))+'/hello'
	# print (dest)
	all_files=os.listdir(src)
	for i in all_files:
		# print (i)
		path=os.path.join(src,i)
		if os.path.isdir(path):
			move(path,dest)
		else:
			file_extn=i.split('.')[-1]
			if file_extn==extn:
				filename=i.split('/')[-1]
				# print(filename)
				os.rename(path,dest+'/'+filename)		


src=os.path.dirname(os.path.abspath(__file__))
# src='/home/varun/Downloads'
dest=os.path.dirname(os.path.abspath(__file__))+'/hello'
# dest='/home/varun/Downloads/mp4'
move(src,dest)
# print (os.path.abspath(__file__))
# print (os.path.dirname(os.path.abspath(__file__)))


