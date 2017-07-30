from colorama import Fore
import os

all_paths=[]
dir_name = input( 'Enter the name of directory you want to clear: ')
extension = set()


def source_path(dir_name):
	for root in os.walk("/home"):
		if dir_name == root[0].split('/')[-1]: 
			all_paths.append(root[0])

	for i in range(len(all_paths)):
		print()
		print("{}. {}".format(i+1,all_paths[i]))

	if len(all_paths) == 0:
		print(Fore.LIGHTRED_EX + 'No directory found')
		exit()

	choice = int(input('\nEnter the option number: '))

	if choice < 1 or choice > len(all_paths):
		print(Fore.LIGHTRED_EX +'Wrong choice entered')
		exit()

	else:
		path = all_paths[choice-1]

	return path


def print_before(path):
	print("Cleaning {} located at {}\n".format(path.split('/')[-1],path))

	print(Fore.LIGHTBLUE_EX  + "Before cleaning\n" + Fore.RESET)

	for files in os.listdir(path):
		print(files,end='\t')
	print()


def destination_path(path): 
	os.chdir(path)

	for f in os.listdir():
		name = (os.path.splitext(f))[0]
		ext = (os.path.splitext(f))[1]

		extension.add(ext[1:])

	new_dir = "New" + path.split('/')[-1]
	new_dir_path = os.path.join(path,new_dir)

	if not os.path.exists(new_dir_path):
		os.mkdir(new_dir_path)

	return new_dir_path,new_dir


def organise(new_dir_path,new_dir,path):
	for ext in extension:
		folder = os.path.join(new_dir_path,ext) 
		
		if not os.path.exists(folder):
			os.mkdir(folder)

		if ext !='':
			for f in os.listdir():
				if os.path.splitext(f)[1].strip('.') == ext:
					os.rename(f,os.path.join(folder,f))

		else:
			for f in os.listdir():
				if f!=new_dir and os.path.splitext(f)[1].strip('.') == ext:
					print(f)
					inner_folder = os.path.join(new_dir_path,f)
					
					if os.path.exists(inner_folder):
						os.chdir(os.path.join(path,f))
						for file in os.listdir():
							new_path = os.path.join(inner_folder,file)
							os.rename(file,new_path)
						os.rmdir(os.path.join(path,f))	

					else:
						os.rename(f,inner_folder)


def print_after(path):

	print(Fore.LIGHTBLUE_EX  + "\nAfter cleaning\n" + Fore.RESET)

	for files in os.listdir(path):
		print(files,end='\t')

	print(Fore.LIGHTMAGENTA_EX  + "\n\nCLEANED\n" + Fore.RESET)


def file_manage():
	path = source_path(dir_name)
	print_before(path)
	new_dir_path, new_dir = destination_path(path)
	organise(new_dir_path, new_dir,path)
	print_after(path)


file_manage()
