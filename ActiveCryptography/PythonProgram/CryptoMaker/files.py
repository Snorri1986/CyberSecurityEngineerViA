import os
from cryptooperations import gen_random_key

# def showfilename(param1, param2, param3):
#     print(param1, param2, param3)

def encryptfile():
    print("Encryption............")
    print("Write the filename to encrypt with extension")
    file_to_encrypt = input()
    print("Write the filename for OTP")
    otp_file_name = input()
    print("Write the filename for encrypted file")
    encrypted_file_name = input()
    filesize = getfilesizeinbytes(file_to_encrypt)
    gen_random_key(filesize)


def decryptfile():
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
    # only hardcode on this case
    app_path = "D:\CyberSecurityEngineerViA\ActiveCryptography\PythonProgram\CryptoMaker"
    file_stats = os.stat(find(filename, app_path))
    print(f'File Size in Bytes is {file_stats.st_size}')
    return file_stats.st_size
