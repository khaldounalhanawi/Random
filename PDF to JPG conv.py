# import subprocess
# subprocess.call("mogrify -resize 150 home/ankip/sisend/image.jpg", shell=True)

import os
path=os.getcwd()


def findjpgs (mypath):
	alljpgs=[]

	try:
		folders=os.listdir(mypath)
	except:
		return(alljpgs)

	mappedcontents=map(lambda x:mypath+'\\'+x,folders)

	for content in mappedcontents:
		if content[-4:]=='.pdf':
			alljpgs.append(content)
		else:
			alljpgs+=findjpgs(content)
	
	return(alljpgs)

# print(*findjpgs(path),sep='\n')

allll=findjpgs(path)
import subprocess
import os

for i in allll:
	# Path to the PDF file (use a raw string to handle backslashes and spaces)
	pdf_file = i
	# Change directory to where the file is located (optional but recommended)
	pdf_directory = os.path.dirname(pdf_file)
	os.chdir(pdf_directory)

	# ImageMagick command: mogrify the PDF to JPG
	command = ['magick', 'mogrify', '-density', '200', '-background', 'white', '-alpha', 'remove', '-format', 'jpg', pdf_file]

	# Run the command
	print(f'processing {i}')
	try:
		subprocess.run(command, shell=True)
		print(f'Done')
	except:
		print(f'Could NOT convert {i}')
		continue