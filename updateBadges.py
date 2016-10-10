#SCRIPT for updating the badges in github.com/diegopastor/learning for how many problems I've solved on each site
import os
import sys
import fileinput

def dir(path, extension):
    list_dir = []
    list_dir = os.listdir(path)
    count = 0
    for file in list_dir:
        if file.endswith(extension):
            count += 1
    return count

CForces = dir('CForces','.py')
CForces -= 2
PE = dir('PE','.py')
UVa = dir('UVa','.py')
UVa -= 1

for line in fileinput.input(['README.md'], inplace=True):
    if line.strip().startswith('<img src="https://img.shields.io/badge/CodeForces'):
        line = '<img src="https://img.shields.io/badge/CodeForces-'+str(CForces)+'-blue.svg">\n'
        sys.stdout.write(line)
    elif line.strip().startswith('<img src="https://img.shields.io/badge/ProjectEuler'):
        line = '<img src="https://img.shields.io/badge/ProjectEuler-'+str(PE)+'-orange.svg">\n' 
        sys.stdout.write(line)
    elif line.strip().startswith('<img src="https://img.shields.io/badge/UVa'):
        line = '<img src="https://img.shields.io/badge/UVa-'+str(UVa)+'-brightgreen.svg">\n' 
        sys.stdout.write(line)
    else:
        sys.stdout.write(line)
