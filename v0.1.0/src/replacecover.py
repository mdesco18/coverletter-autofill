"""
co-op cover letter
"""

import os
import sys
import re
from datetime import date

def main():

	#the cover letter txt
	ifile = sys.argv[1]
	infile = os.path.abspath(ifile)
	#the job descriptors
	dfile = sys.argv[2]
	descfile = os.path.abspath(dfile)	

	#get 
	#date
	#company
	#address
	#job
	#length
	
	d = date.today().strftime("%B %d, %Y")
	with open(descfile) as f:
		lines = f.read().splitlines()
		company = lines[0]
		address = lines[1]
		job = lines[2]
		length = lines[3]
	
	descreplace = {"#Date#":d, "#Company#":company, "#Address#":address, "#Job#": job, "#length#": length}
	
	with open(infile) as f:
		cover = f.read()
		for key, value in descreplace.items():
			cover = re.sub(key, value, cover)
		
	outfile = 'cover.txt'
	outfile = open(outfile, 'w')
	outfile.write(cover)
		
	outfile.close()
	
	
if __name__ == '__main__':
	main()
