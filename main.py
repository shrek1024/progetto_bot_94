#/*--
#
# Copyright (c) 2025  Frêney Studios
#
# Module Name:
#
#	 main.py
#
# Abstract:
#
#	 Safe Aero Core
#	 (COMMAND LINE)
#
# Author:
#
#	 Marco Panseri (Marx) 18-04-2025
#    Piergiorgio (Shrek1024) 18-04-2025
#    Pradee 18-04-2025
#    Tommaso 18-04-2025
#
# Revision History:
#
#--*/

################### IMPORTS #############################
try:
	import tensorflow as tf
	import numpy as np
	import requests 
	import keras
	import discord
	import yolov
	import imageai
	import bot
	import os
except Exception as e:
	print("Error: " + e.message)

################### CFG VARIABLES #######################
show_module_ver   : bool = True
version 		  : str  = "v.0.0.3"
legalcaption 	  : str  = "Copyright (c) Frêney Studios Holdings and affiliates"

################### MODULE VERSIONS #######################
if show_module_ver:
	print("Module information")
	print(" - Tensorflow: " + tf.__version__)
	print(" - NumPy:		  " + np.__version__)
	print(" - requests: 	" + requests.__version__)
	print(" - keras: 			" + keras.__version__)
	print(" - discord:		" + discord.__version__)
	print(" - YOLOv:			" + yolov.__version__)
	print(" - ImageAI:		" + imageai.__version__)

################# FUNCTIONS ###############################
def show_license() -> None:
	print("License: GNU GENERAL PUBLIC LICENSE v.3")

	try:
		with open("LICENSE.md") as f:
			print(f)
	except FileNotFoundError:
		print("Cannot found license file!")

def show_caption() -> None:
	print(f""" 	
	   			    Safe Aero {legalcaption}
					This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
					This is free software, and you are welcome to redistribute it
					under certain conditions; type `show c' for details.
	""")

def yn(message: str) -> bool:
	if message.lower() in [ "yes", "y", "ok" ]:
		return True 
	else:
		return False

def cli_loop():
	while 1:
		cmd : str = str(input("> ")).lower()

		if cmd == "exit":
			break 
		elif cmd == "show c" or \
		 	 cmd == "show w" or \
			 cmd == "legal"  or \
			 cmd == "show legal":
			show_license()
		elif cmd == "test yn":
			while 1:
				inp : str = str(input(">>> "))

				if inp != "exit":
					yn(inp)
				else:
					break
		else:
			print(f"Error: unknow command \"{cmd}\"!")

####################### ENTRY POINT #########################
if __name__ == "__main__":
	show_caption()

	if yn(input("Would you like to start the CLI?")):
		os.system("clear") # Linux
		# os.system("cls") # Windows NT
		show_caption()
		print()

		cli_loop()
	else:
		bot.bot_interface()
		
