import os
from cryptooperations import gen_random_key
from cryptooperations import xoroperationencrypt

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
    sourcetxtbytearray = getbytearrayfromsourcefile(file_to_encrypt)
    keybytearray = getbytearrayfromtxt(keytxt)
    encryptedsource=xoroperationencrypt(sourcetxtbytearray,keybytearray)
    createencfile(encrypted_file_name, encryptedsource)

def decryptfile():
    """Function for dencrypt file"""
    #TODO:function is not finished yet
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
    return file_stats.st_size

def createotpfile(key,filename):
    """Create OTP file"""
    file = open(filename,"w")
    file.write(listtostr(str(key)))
    file.close()

def createencfile(filename,data):
    """Create OTP file"""
    file = open(filename, "w")
    file.write(str(data))
    file.close()

def listtostr(list):
    """Convert list to string"""
    str = " "
    return (str.join(list))

def getbytearrayfromsourcefile(filename):
    file = open(filename,"r")
    file_char_array = []
    for x in file:
        file_char_array.extend(x)
    b = bytearray()
    b.extend(map(ord,file_char_array))
    return b

def getbytearrayfromtxt(txt):
    """Get bytearray from key file"""
    txt_in_char_arr = []
    for x in str(txt):
        txt_in_char_arr.extend(x)
    b = bytearray()
    b.extend(map(ord, txt_in_char_arr))
    return b

