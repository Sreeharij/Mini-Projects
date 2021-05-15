import os,random,sys,pprint as pp
old_name = {}
temporary_renaming = []
count = 1

try:
        root = sys.argv[sys.argv.index('-file')+1]
except:
        root = input("Enter folder to bulk renmae its contents:(type 'confirm' to use current folder) ")
if root == 'confirm':
        root = os.getcwd() + '\\'
else:
        if root[-1]!='\\':
                root = root + '\\'

all_items = os.scandir(root)
all_files = []
for item in all_items:
        if item.is_file():
                all_files.append(item.name)

for i in range(len(all_files)):
        file = all_files[i]
        if file=='rename.py':
                continue
        extension = file.split('.')[-1]

        if f'{count}.{extension}' == file:          
                pass 

        elif f'{count}.{extension}' not in all_files:
                os.rename(root+file,f'{root}{count}.{extension}')
                all_files[i] = f'{root}{count}.{extension}'
        else:
                dup_idx = all_files.index(f'{count}.{extension}')
                random_number = random.randint(1,100000000)
                while f'{random_number}.{extension}' in all_files:
                        random_number = random.randint(1,100000000)

                os.rename(f'{root}{count}.{extension}',f'{root}{random_number}.{extension}')
                os.rename(root+file,f'{root}{count}.{extension}')

                temporary_renaming.append((all_files[dup_idx],f'{random_number}.{extension}'))

                all_files[dup_idx] = f'{random_number}.{extension}'
                all_files[i] = f'{count}.{extension}'
                
        flag = False
        for a,b in temporary_renaming:
                if file==b:
                        old_name[a] = f'{count}.{extension}'
                        flag=True
        if not flag:
                old_name[file] = f'{count}.{extension}'
        count += 1

def pretty_loggin():
	'''Call This function to for nice formatting.'''
	string = "|" + "-"*80 + "|" + "-"*10 +  "|" + '\n'
	string += "{:<80} {:<10} {:<5}".format("| Old Name","| New Name","|") +'\n'
	string +=  "|" + "-"*80 + "|" + "-"*10 +  "|" + '\n'
	for k,v in old_name.items():
		string += "{:<80} {:<10} {:<5}".format("| "+k,"| "+v,"|") + '\n'
		string += "|" + "-"*80 + "|" + "-"*10 +  "|" + '\n'
	return string

with open(f'{root}renamed_log_file.txt','wt') as f:
	string = "Old Name : New Name\n"
	for k,v in old_name.items():
		string += f"{k} {v}\n"
	f.write(string)

