import os,math
from cryptooperations import gen_random_key

# def showfilename(param1, param2, param3):
#     print(param1, param2, param3)

def encryptfile():
    """Function for encrypt file"""
    print("Encryption............")
    print("Write the filename to encrypt with extension")
    file_to_encrypt = input()
    print("Write the filename for OTP")
    otp_file_name = input()
    print("Write the filename for encrypted file")
    encrypted_file_name = input()
    filesize = getfilesizeinbytes(file_to_encrypt)
    keytxt = gen_random_key(filesize)
    createotpfile(keytxt, otp_file_name)
    sourceinbinary = toBinary(gettxtfromsourcefile(file_to_encrypt))
    #test code
    print(sourceinbinary)


def decryptfile():
    """Function for dencrypt file"""
    print("Decryption............")
    print("Enter the filename to decrypt with extension")
    decrypted_file = input()
    print("OTP file")
    otp_file_name = input()
    print("Write the filename for encrypted file")
    encrypted_file_name = input()


def find(name, path):
    """ find file name through particular path """
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def getfilesizeinbytes(filename):
    """Get size of file"""
    # only hardcode on this case
    app_path = "D:\CyberSecurityEngineerViA\ActiveCryptography\PythonProgram\CryptoMaker"
    file_stats = os.stat(find(filename, app_path))
    print(f'File Size in Bytes is {file_stats.st_size}')
    return file_stats.st_size

def createotpfile(key,filename):
    """Create OTP file"""
    file = open(filename,"w")
    file.write(listtostr(str(key)))
    file.close()

def listtostr(list):
    """Convert list to string"""
    str = " "
    return (str.join(list))

def gettxtfromsourcefile(filename):
    file = open(filename,"r")
    #file.close()
    return file

def toBinary(text):
    """Convert txt to binary"""
    l,m=[],[]
    #TODO: remove spaces,comas,and [] in text
    for i in text:
       l.append(ord(i))
    for i in l:
       m.append(int(bin(i)[2:]))
    return m