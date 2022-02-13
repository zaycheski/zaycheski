import os
import shutil
import glob
import subprocess


COMMAND_NAME = "zaycheski"
USERNAME = "varvarasafonova"
PREFIX = f"/Users/username/"
zaycheski_directory = ""
local_commands_file = ""
local_storage_folder = ""
local_executable_file = ""

def set_main_variables():
	global PREFIX
	global zaycheski_directory
	global local_commands_file
	global local_storage_folder
	global local_executable_file

	PREFIX = f"/Users/{USERNAME}/"
	zaycheski_directory = PREFIX + ".zaycheski"
	local_commands_file = zaycheski_directory + "/" + "custom_bash_commands"
	local_storage_folder = zaycheski_directory + "/" + "stored_cute_images"
	local_executable_file = zaycheski_directory + "/" + "main.py"

def clear_folder(path):
	if path != local_storage_folder:
		return
	for subdir, dirs, files in os.walk(local_storage_folder):
		for file in files:
			filepath = subdir + os.sep + file
			os.system(f"rm {filepath}")

def copy_to_local_storage_folder():
	clear_folder(local_storage_folder)
	for subdir, dirs, files in os.walk("./ascii_images"):
		for file in files:
			filepath = subdir + os.sep + file
			print("filepath = ", filepath, " local_storage_folder = ", local_storage_folder)
			os.system(f"cp {filepath} {local_storage_folder}")

def set_commands_file():
	with open(local_commands_file, mode = "w") as f:
		print("#!/bin/bash", file = f)
		print(f"function {COMMAND_NAME}()", " {", file = f)
		print(f"\tpython3 {local_executable_file}", file = f)
		print("}", file = f)

def set_executable_file():
	with open(local_executable_file, mode = "w") as f:
		print("from random import randint", file = f)
		print("import os", file = f)
		print(f'files = os.listdir("{local_storage_folder}")', file = f)
		print("r = randint(0, len(files) - 1)", file = f)
		print(f'print(open("{local_storage_folder}/" + files[r]).read())', file = f)

def create_zaycheski_environment():
	set_main_variables()

	os.system(f"mkdir {zaycheski_directory}")
	os.system(f"mkdir {local_storage_folder}")
	os.system(f"touch {local_commands_file}")
	os.system(f"touch {local_executable_file}")

	clear_folder(local_storage_folder)

	copy_to_local_storage_folder();
	set_commands_file()
	set_executable_file()

	os.system(f'echo ". {local_commands_file}" > {PREFIX}.zshrc')
	os.system(f". {local_commands_file}")
	os.system("zsh")



def main():
	global COMMAND_NAME
	global USERNAME
	
	command_name = input("Do you want zaycheski or zaycheskaya (zaycheski default): ")
	entered_username = input("Enter username (varvarasafonova default): ")

	if command_name != "zaycheskaya":
		command_name = "zaycheski"
	COMMAND_NAME = command_name

	if len(entered_username) < 1:
		USERNAME = "varvarasafonova"
	else:
		USERNAME = entered_username

	create_zaycheski_environment()

main()
