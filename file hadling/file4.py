with open("file4.txt","w+") as file:
    file.write("Hello Happy Birthday")
    file.seek(0)
    file.writelines(["Ramu","shyamu\n"])
with open("file4.txt","r") as file:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())