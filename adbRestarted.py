import os 

os.chdir("C:\\Users\\Jose\\AppData\\Local\\Android\\Sdk\\platform-tools")
os.system("adb devices")
os.system("adb tcpip 5555")

print("Insert the ip: ")
ip = input()

os.system("adb connect " + ip)
