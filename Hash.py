#! python3

import os.path
import hashlib
import zlib
import getpass


# pause, press ENTER to continue
def pause():
    print()
    getpass.getpass("Press Enter to continue...")


# hash for md5
def md5hash(inputfile):
    md5 = hashlib.md5()
    with open(inputfile, 'rb') as fin:
        for chunk in iter(lambda: fin.read(4096 * md5.block_size), b''):
            md5.update(chunk)
        print("   md5: " + md5.hexdigest())


# hash for sha1
def sha1hash(inputfile):
    sha1 = hashlib.sha1()
    with open(inputfile, 'rb') as fin:
        for chunk in iter(lambda: fin.read(4096 * sha1.block_size), b''):
            sha1.update(chunk)
        print("  sha1: " + sha1.hexdigest())


# hash for sha256
def sha256hash(inputfile):
    sha256 = hashlib.sha256()
    with open(inputfile, 'rb') as fin:
        for chunk in iter(lambda: fin.read(4096 * sha256.block_size), b''):
            sha256.update(chunk)
        print("sha256: " + sha256.hexdigest())


# hash for crc32
def crc32hash(inputfile):
    with open(inputfile, 'rb') as fin:
        csum = 0
        for chunk in iter(lambda: fin.read(4096), b''):
            csum = zlib.crc32(chunk, csum)
        print(" crc32: " + hex(csum & 0xFFFFFFFF))


# main program
print("Current Working Directory: " + os.getcwd())
filename = str(input('Enter [path]filename: '))
hashMode = str(input('Enter Hash Mode (all/md5/sha1/sha256/crc32): '))
print()

if not os.path.isfile(filename):
    print("Error: File \"" + filename + "\" not exists")
    exit()

if hashMode == "all":
    md5hash(filename)
    sha1hash(filename)
    sha256hash(filename)
elif hashMode == "md5":
    md5hash(filename)
elif hashMode == "sha1":
    sha1hash(filename)
elif hashMode == "sha256":
    sha256hash(filename)
elif hashMode == "crc32":
    crc32hash(filename)
else:
    print("Error: Hash Mode \"" + hashMode + "\" is not defined. Note: It's case sensitive.")
pause()
