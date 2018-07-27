import sys
from tkinter import filedialog
from tkinter import *

def app_help():
	print("More help is coming. For now, please contact Application Author (Stephan Riley).")

def get_user_input(request):
	return input(request)

def start_program():
	print("Welcome to Folder Finder. (KB 000003727)")
	user_input = get_user_input("Would you like to begin? y/n/help />")
	run_program(user_input)

def run_program(user_input):
	if user_input.lower() == 'y':
		get_files()
	elif user_input.lower() == 'n':
		end_program()
	elif user_input.lower() == 'help':
		app_help()
	else:
		user_input = get_user_input("That is not a valid input. Would you like to try again? y/n/help />")
		run_program(user_input)

def end_program():
	print("Thank you for using Folder Finder. Have a nice day.")
	sys.exit()

def get_files():
	read_file = get_user_input("Path to log file />")
	write_file = get_user_input("Path to file you want to save list to />")
	with open(read_file, 'r', encoding='utf-8') as input_file:
		with open(write_file, 'w') as output_file:
			selection = input_file.readlines()
			count = 0
			for index, line in enumerate(selection):
				if '-W-' in line and '-W-' in selection[index + 1]:
					output_file.write(selection[index + 2])
					count += 1
			print("{} folder paths were writen to the file.".format(count))
			get_user_input("Would you like to run again? y/n/help />")

start_program()