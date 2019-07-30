#!/usr/bin/env python3

import shutil

import os

os.chdir("/home/student/mycode/")

shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy") # This makes a copy of the original file and names it the sencond name in the string

shutil.copytree("5g_research/", "5g_research_backup/") # This creates a new directory and copies all of the contents of the original directory


