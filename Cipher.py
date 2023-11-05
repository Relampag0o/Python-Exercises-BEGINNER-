import random

swaps = [-1] * 256


def shuffle(password):
    random.seed(password)
    for i in range(len(swaps)):
        rand = random.randint(0, 255)
        while find(rand):
            rand = random.randint(0, 255)
        swaps[i] = rand


def find(value):
    return value in swaps


def showSwaps():
    for i in range(len(swaps)):
        print(f"[{i}] {swaps[i]} char: {chr(swaps[i])}")


def encrypt(src_file, dst_file):
    try:
        with open(src_file, 'r') as src:
            with open(dst_file, 'w') as dst:
                for line in src:
                    for char in line:
                        if swaps[ord(char)] != -1:
                            dst.write(chr(swaps[ord(char)]))
                        else:
                            dst.write(char)
                    dst.write('\n')
    except Exception as e:
        print(f"There was an error with the file: {e}")


def decrypt(src_file, dst_file):
    try:
        with open(src_file, 'r') as src:
            with open(dst_file, 'w') as dst:
                for line in src:
                    for char in line:
                        if char != '\n':
                            for j in range(len(swaps)):
                                if swaps[j] == ord(char):
                                    dst.write(chr(j))
                                    break
                        else:
                            dst.write('\n')
    except Exception as e:
        print(f"There was an error with the file: {e}")


# copied this line from somewhere. it looks like it makes the python run as main when i click on "play".
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 5:
        password = int(sys.argv[2])
        shuffle(password)
        showSwaps()
        if sys.argv[1] == "-c":
            print(f"Encrypting file: '{sys.argv[3]}' with password: {sys.argv[2]}")
            encrypt(sys.argv[3], sys.argv[4])
            print(f"Encrypted file: {sys.argv[4]}")
        elif sys.argv[1] == "-d":
            print(f"Decrypting file: '{sys.argv[3]}' with password: {sys.argv[2]}")
            decrypt(sys.argv[3], sys.argv[4])
            print(f"Decrypted file: {sys.argv[4]}")
        else:
            print("Not supported operation.")
    else:
        print("You can only use 4 arguments.")
        print("Encrypting: -c password srcFile secretFile")
        print("Decrypting: -d password secretFile dstFile")



