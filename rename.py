import os


with open("names.txt","r") as filename:
    datalist = filename.readlines()
    new_names=[]
    for items in range (0 , len(datalist),3):
        new_names.append( datalist[items+1])

    print(f" lenth of new names: {len(new_names)}")    

path = os.path.curdir
old_names = os.listdir(path)
print(f" lenth of new names: {len(old_names)}")

for root,dirs,files in os.walk(path):
    print(type(files))
    print(f" lenth of new names: {len(files)}")

i=0
for item in files:
    if item.split(".")[1] == "mp4":
        os.rename(files[i], str(i+1) +"-" + new_names[i].strip()+".mp4")
        print("not a mp4 file")
    print(item.split("."))
    i+=1
    