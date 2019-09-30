import shutil, os

path = '/root/autonomous/discord/autonomous-discord'

files = []
sqliteFiles = []
#r=root, d=directories, f=files

for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

for f in files:
    if '.sqlite' in str(f):
        sqliteFiles.append(f)

        for item in sqliteFiles:
            shutil.move(item, '/root/autonomous/discord/autonomous-database')
            

