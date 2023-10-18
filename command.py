import os

os.chdir("C:\\Users\\Jose\\AppData\\Local\\Android\\Sdk\\platform-tools")

print("Insert the ip: ")
ip = input()

os.system("adb connect " + ip)
