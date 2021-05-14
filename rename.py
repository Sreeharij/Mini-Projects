import os,shutil,stat,sys
extension_arr = []
count = 1

print("[WARNING]The folder you provide must not have a subfolder named 'temp'.")
try:
        root = sys.argv[1]
except:
        root = input('Enter folder to bulk renmae its contents:(press enter to use current folder) ')
if root == '':
        root = os.getcwd() + '\\'
else:
        if root[-1]!='\\':
                root = root + '\\'
try:
	os.mkdir(f'{root}temp')
except:
        if input("Temp folder already exists.\nProceed to delete it?('y' to proceed)") == 'y':
                shutil.rmtree(f'{root}temp')
                os.mkdir(f'{root}temp')
        else:
                print('cant proceed as temp folder already exists')


all_items = os.scandir(root)
all_files = []
for item in all_items:
        if item.is_file():
                all_files.append(item.name)
                
for file in all_files:
        if file=='rename.py' or file=='temp':
                continue
        os.chmod(root+file,stat.S_IWUSR)
        extension_arr.append((file,file.split('.')[-1]))
print(len(extension_arr))

for item in extension_arr:
	old_name = root+item[0]
	shutil.copy(old_name,root+f'temp\\{count}.'+item[1])
	count += 1

for file in all_files:
	if file=='rename.py' or file=='temp':
		continue
	os.remove(root+file)

for file in os.listdir(root+'temp\\'):
	shutil.copy(root+'temp\\'+file,root)	

shutil.rmtree(f'{root}temp')
