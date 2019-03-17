import os
import shutil as shut

LogFolder = "C:\\Riot Games\\League of Legends\\Logs"	

files = os.listdir(LogFolder)
print(files)     

#size = os.path.getsize(LogFolder)
#length = len(os.listdir(LogFolder))

for n in files:
	file = LogFolder + '\\' + n
	shut.rmtree(file)

	print("Deleted " + n)

print("Cleaned " + LogFolder)


