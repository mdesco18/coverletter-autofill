"""
co-op cover letter job description replacement
"""

import os
import sys
import re
from datetime import date

def replace(jobdetail, samplecover):
	print("Replacing job details...")
	print("Input parameters: "+jobdetail)
	#get
	#date
	#company
	#address
	#job
	#employment type
	#hiring manager

	d = date.today().strftime("%B %d, %Y")
	lines = jobdetail.split(',')
	company = lines[0]
	address = lines[1]
	job = lines[2]
	employtype = lines[3]
	hiringmgr = lines[4]

	descreplace = {"#Date#":d, "#Company#":company, "#Address#":address, "#Job#": job, "#employ-type#": employtype, '#hiring-manager#': hiringmgr}
	sampleTitle = samplecover.split('/')[-1]
	print("\tReading sample cover letter "+samplecover)
	with open(samplecover) as f:
		covercontent = f.read()
		for key, value in descreplace.items():
			print("\t\tReplacing "+key+" with "+value)
			cover = re.sub(key, value, cover)

	covertitle = job+'_'+company+'.txt'
	print("...cover letter "+covertitle+" ready to save.")

	outfile = '../output/'+covertitle
	outfile = open(outfile, 'w')
	outfile.write(covercontent)

	outfile.close()

	return covertitle, covercontent;
