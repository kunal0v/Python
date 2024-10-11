file=open("ramu.txt","w")
file.seek(0)
file.write("aloha")
with open ("ramu.txt","w") as file:
    file.write("hello ")
    file.close()
# with open ("ramu.txt","r+") as file:
#     print(file.read())
#     file.seek(0)
#     file.write("Hello How are You\n")
#     file.seek(0)
#     file.write("huh")
file=open("ramu.txt","w")
file.write("before appends\n")
with open ("ramu.txt","a") as file:
    file.write("yes appends mode is done\n")
with open ("ramu.txt","a+") as file:
    file.write("one more time append and read")
    print(file.read())