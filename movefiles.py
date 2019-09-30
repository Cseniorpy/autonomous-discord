import shutil, os

#The destination for the item to move
path = '/root/autonomous/discord/autonomous-discord'


files = []
#Track the .sqlite files specifically
sqliteFiles = []
#r=root, d=directories, f=files

#Get the files in a directory
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

for f in files:
    #Get only '.sqlite' files to sqliteFiles 
    if '.sqlite' in str(f):
        sqliteFiles.append(f)

        #Move the '.sqlite' files to database folder which has not to be in git repository
        for item in sqliteFiles:
            shutil.move(item, '/root/autonomous/discord/autonomous-database')


