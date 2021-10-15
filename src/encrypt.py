import os
import base64
import json
import struct

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad, unpad

from .utils import add_to_16


class EncryptData(object):

    @staticmethod
    def encrypt_string(data, key="G+b8u9XWZljDTy7Lbp/eqdKeAhvC46gl"):
        if isinstance(data, str):
            pass
        elif isinstance(data, dict):
            data = json.dumps(data)
        else:
            raise Exception("Only str or dict support")
        key = add_to_16(key).encode()
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        data = cipher.encrypt(pad(data.encode(), AES.block_size))
        data = iv + data
        return base64.b64encode(data)

    @staticmethod
    def encrypt_file(in_filename, out_filename=None, chunksize=64*1024, key="G+b8u9XWZljDTy7Lbp/eqdKeAhvC46gl"):
        if not out_filename:
            out_filename = in_filename + '.enc'
        iv = os.urandom(16)
        key = add_to_16(key).encode()
        encryptor = AES.new(key, AES.MODE_CBC, iv)
        filesize = os.path.getsize(in_filename)
        with open(in_filename, 'rb') as infile:
            with open(out_filename, 'wb') as outfile:
                outfile.write(struct.pack('<Q', filesize))
                outfile.write(iv)
                pos = 0
                while pos < filesize:
                    chunk = infile.read(chunksize)
                    pos += len(chunk)
                    if pos == filesize:
                        chunk = pad(chunk, AES.block_size)
                    outfile.write(encryptor.encrypt(chunk))
