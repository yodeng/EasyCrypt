import os
import re
import base64
import struct

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad, unpad

from .utils import add_to_16


class DecryptData(object):
    @staticmethod
    def decrypt_string(data, key="G+b8u9XWZljDTy7Lbp/eqdKeAhvC46gl"):
        '''
        data must be base64.b64encode()
        '''
        key = add_to_16(key).encode()
        data = base64.b64decode(data)
        iv = data[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        data = unpad(cipher.decrypt(data[AES.block_size:]), AES.block_size)
        return data

    @staticmethod
    def decrypt_file_iter(in_filename, chunksize=64*1024, key="G+b8u9XWZljDTy7Lbp/eqdKeAhvC46gl"):
        with open(in_filename, 'rb') as infile:
            filesize = struct.unpack('<Q', infile.read(8))[0]
            iv = infile.read(16)
            key = add_to_16(key).encode()
            encryptor = AES.new(key, AES.MODE_CBC, iv)
            encrypted_filesize = os.path.getsize(in_filename)
            pos = 8 + 16  # the filesize and IV.
            while pos < encrypted_filesize:
                chunk = infile.read(chunksize)
                pos += len(chunk)
                chunk = encryptor.decrypt(chunk)
                if pos == encrypted_filesize:
                    chunk = unpad(chunk, AES.block_size)
                yield chunk

    @staticmethod
    def decrypt_file(in_filename, out_file=None, chunksize=64*1024, key="G+b8u9XWZljDTy7Lbp/eqdKeAhvC46gl"):
        if out_file is None:
            out_file = in_filename + ".enc"
        with open(out_file, "wb") as fo:
            for line in DecryptData.decrypt_file_iter(in_filename=in_filename, chunksize=chunksize, key=key):
                fo.write(line)

    @staticmethod
    def decrypt_file_readline(in_filename, key="G+b8u9XWZljDTy7Lbp/eqdKeAhvC46gl"):
        line = ""
        for src in DecryptData.decrypt_file_iter(in_filename, chunksize=64*1024, key=key):
            res = re.split("\n", src)
            res[0] = line + res[0]
            yield res[0] + "\n"
            if len(res) == 1:
                line = ""
            else:
                for i in res[1:-1]:
                    yield i + "\n"
                line = res[-1]
        if line:
            yield line
