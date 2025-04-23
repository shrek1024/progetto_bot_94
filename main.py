x  = 0
print(x)
#ciao
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
#
# Author:
#
#	 Marco Panseri (Marx) 18-04-2025
#  Piergiorgio (Shrek1024) 18-04-2025
#  Pradee 18-04-2025
#  Tommaso 18-04-2025
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
except Exception as e:
	print("Error: " + e.message)

################### CFG VARIABLES #######################
show_module_ver : bool = True
version 			  : str  = "v.0.0.2"
legalcaption 	  : str  = "Copyright (c) Frêney Studios and affiliates"

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
