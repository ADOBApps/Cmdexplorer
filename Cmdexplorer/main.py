#Author: ADOB
#Date: 09/07/2021
#Version: 1.0

import os, sys, pathlib, shutil, time

from my_io.hcolors import Hcolors
from my_io.zip import AsyncZip


class Cmdexplorer():
	"""
	Cmdexplorer class a terminal simple explorer
	"""
	def __init__(self, *args, **kwargs):
	#code
		#using our module Hcolors
		self.hcolors = Hcolors()
		#self.bg_zip = AsyncZip()
		#Set self.full_path with current path, avoid return path error at t_select function
		self.full_path=os.getcwd()
		self.r_text=""
		print(self.hcolors.CITALIC + "Simple File Explorer \n" + self.hcolors.CEND)


	def t_write(self, path, name, sl):
		"""
		Write file
		"""
		#file = open("file.txt", "w+")file.seek(0,2)file.write("Simple File Explorer Test")file.seek(0,0)print(file.read())file.close()
		os.chdir(path)
		try:
			file = os.open(name, os.O_RDWR|os.O_CREAT)
			b=str.encode(sl)
			#Write one string
			os.write(file,b)
			#Infact here you wouls not be able ro see its effect
			os.fsync(file)
			#now read this file from the beginning
			os.lseek(file,0,0)
			line = os.read(file, 10000000).decode()
			#print(line)
			os.close(file)
			print(self.hcolors.CITALIC + self.hcolors.OKGREEN + "Success" + self.hcolors.CEND + self.hcolors.CEND +"\n")
		except OSError as e:
					print(self.hcoloras.WARNING + f"Error:{e.strerror}" + self.hcolors.CEND +"\n")
		return


	def t_read(self):
		"""
		read file function
		Function to select folder o file
		"""
		#Clean screen
		#os.system("cls") #for DOS/Windows
		#os.system("clear") #for unix
		print(self.hcolors.BOLD + "What do you want to do?" + self.hcolors.CEND)
		print(self.hcolors.BOLD + "Enter O to [O]pen, S to [S]elect, U to [U]p go to parent directory, M to [M]ake folder, F to create [F]ile, D to [D]elete file or folder, B to [B]ack return main menu" + self.hcolors.CEND + "\n")
		print(self.hcolors.CITALIC + os.getcwd() + self.hcolors.CEND + "\n")
		f1=input("Insert function: ")
		if( (f1=="O") or (f1=="o") ):
			print("\n")
			os.system("clear") #for unix
			self.t_getdirs(os.getcwd(), "r")
		elif( (f1=="S") or (f1=="s") ):
			print("\n")
			#os.system("clear") #for unix
			self.t_select()
		elif( (f1=="M") or (f1=="m") ):
			r_name=input("Type folder name: ")
			self.t_mkdir(os.getcwd(), r_name)
			print("\n")
			time.sleep(2)
			os.system("clear") #for unix
			self.t_getdirs(os.getcwd(), "r")
		elif( (f1=="F") or (f1=="f") ):
			r_name=input("Type file name: ")
			r_sl=input("Type string: ")
			self.t_write(os.getcwd(), r_name, r_sl)
			print("\n")
			time.sleep(2)
			os.system("clear") #for unix
			self.t_getdirs(os.getcwd(), "r")
		elif( (f1=="D") or (f1=="d") ):
			r_name=input("Type file or folder name: ")
			self.t_delete(os.getcwd(), r_name)
			print("\n")
			time.sleep(2)
			os.system("clear") #for unix
			self.t_getdirs(os.getcwd(), "r")
		elif( (f1=="U") or (f1=="u") ):
			os.chdir("..")
			self.r_text =os.getcwd()
			os.system("clear") #for unix
			self.t_getdirs(os.getcwd(), "r")
		elif( (f1=="B") or (f1=="b") ):
			self.main()
		else:
			self.t_read()
		return

	def t_getdirs(self, path, r_stat):
		"""
		Get and list file and folders
		"""
		print(self.hcolors.CITALIC + path + self.hcolors.CEND)
		with os.scandir(path) as p_files:
			for p_file in p_files:
				if( (os.path.isfile(p_file)) ):
					#Using os.path.splitext("path"). r_root: file name, r_ext: Extension
					#r_root, r_ext=os.path.splitext(p_file)
					#using module pathlib
					r_path=pathlib.Path(p_file)
					#print("Parent: ", r_path.parent)
					#print("Name: ", r_path.name)
					#print("Extension: ", r_path.suffix)
					r_ext=r_path.suffix
					if( (r_ext== ".py") or (r_ext== ".sh") or (r_ext== ".php") or (r_ext== ".js") ):
						print(self.hcolors.OKGREEN + p_file.name + self.hcolors.CEND)
					elif( (r_ext== ".c") or (r_ext== ".cpp") or (r_ext== ".java") or (r_ext== ".html") or (r_ext== ".css") ):
						print(self.hcolors.CVIOLET + p_file.name + self.hcolors.CEND)
					elif( r_ext== "" ):
						print(self.hcolors.WARNING + p_file.name + self.hcolors.CEND)
					elif( (r_ext== ".txt") ):
						print(self.hcolors.BOLD + p_file.name + self.hcolors.CEND)
					elif( (r_ext== ".zip") or (r_ext== ".rar") or (r_ext== ".jar") ):
						print(self.hcolors.UNDERLINE + p_file.name + self.hcolors.CEND)
					elif( (r_ext== ".tar") or (r_ext== ".pyc") ):
						print(self.hcolors.FAIL + p_file.name + self.hcolors.CEND)
					else:
						print(self.hcolors.FAIL + p_file.name + self.hcolors.CEND)
				elif( (os.path.isdir(p_file)) ):
					print(self.hcolors.OKBLUE + p_file.name + self.hcolors.CEND)
				else:
					print(p_file.name)
		print("\n")
		if(r_stat=="r"):
			self.t_read()
		else:
			self.t_read()
		return

	def t_select(self):
		"""
		Function to select folder o file
		"""
		print("'^B'' to [B]ack read menu, '^Q' to [Q]uit")
		f2=input("type dir or file name or default options: ")
		d_file = os.getcwd()
		r_path=pathlib.Path(d_file)
		if( (f2=="^B") or (f2=="^b") ):
			self.t_read()
		elif( (f2=="^Q") or (f2=="^q") ):
			quit()
		else:
			s_path=d_file +"/"+ f2
			if( os.path.isdir(s_path) ):
				print("\n")
				os.chdir(f2)
				os.system("clear") #for unix
				self.t_getdirs(s_path, "s")
			elif(os.path.isfile(s_path)):
				s_file=os.open(s_path, os.O_RDWR)
				os.lseek(s_file,0,0)
				s_line=os.read(s_file, 10000000).decode()
				print(self.hcolors.CITALIC + s_path + self.hcolors.CEND +"\n")
				print("#---------------------------------------------------->>")
				print(s_line)
				print("#<<----------------------------------------------------")
				print("\n")
				os.close(s_file)
				self.t_read()
			else:
				self.t_select()
		return


	def t_mkdir(self, path, name):
		"""
		Create folders
		"""
		os.chdir(path)
		try:
			os.mkdir(name, 755)
			print(self.hcolors.CITALIC + self.hcolors.OKGREEN + "Success" + self.hcolors.CEND + self.hcolors.CEND +"\n")
		except OSError as e:
					print(self.hcolors.CITALIC + self.hcolors.WARNING + f"Error:{e.strerror}" + self.hcolors.CEND + self.hcolors.CEND +"\n")
		return

	def t_delete(self, path, name):
		"""
		delete files or directory
		"""
		print("Delete?")
		d_path=path + "/" + name
		d_d=input("[Y]es or [N]o?: ")
		if( (d_d=="Y") or (d_d=="y")):
			if(os.path.isdir(d_path)):
				try:
					shutil.rmtree(d_path)
					print(self.hcolors.CITALIC + self.hcolors.OKGREEN + "Success" + self.hcolors.CEND + self.hcolors.CEND +"\n")
				except OSError as e:
					print(self.hcolors.CITALIC + self.hcolors.WARNING + f"Error:{e.strerror}" + self.hcolors.CEND + self.hcolors.CEND +"\n")
			elif( (os.path.isfile(d_path)) ):
				try:
					os.remove(d_path)
					print(self.hcolors.CITALIC + self.hcolors.OKGREEN + "Success" + self.hcolors.CEND + self.hcolors.CEND +"\n")
				except OSError as e:
					print(self.hcolors.CITALIC + self.hcolors.WARNING + f"Error:{e.strerror}" + self.hcolors.CEND + self.hcolors.CEND +"\n")
			else:
				print(self.hcolors.FAIL + f"Error:{OSError.strerror}" + self.hcolors.CEND +"\n")
				self.t_delete(path, name)
		elif( (d_d=="N") or (d_d=="n")):
			self.t_read()
		else:
			self.t_delete(path, name)
		return

	def main (self):
		"""
		Main function, can call all function
		"""
		print ("Function [R]ead file")
		print("Function [Q]uit")
		print ("\n")
		f=input("Insert function: ")
		print("\n")
		if ((f == "R") or (f=="r")):
			self.t_read()
		elif ((f=="Q") or (f=="q")):
			quit()
		else:
			print("Try again")
			self.main()
		
cmd = Cmdexplorer()
cmd.main()
