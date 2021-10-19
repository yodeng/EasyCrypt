### simple encrypt and decrypt for file, strings and json-object.

##### Install

```
git clone https://github.com/yodeng/EasyCrypt.git
pip install ./EasyCrypt
```


+ `python2 and python3 compatible`

+ `'pycryptodome' and 'Cython' are installed requires, will be installed automaticly`

  

##### Usage

```
$ EasyCrypt -h 
usage: EasyCrypt [-h] [-i <file>] [-d <file>] [-e <file>]

simple encrypt and decrypt for files

optional arguments:
  -h, --help            show this help message and exit
  -i <file>, --input <file>
                        input file for encrypt/decrypt
  -d <file>, --dec <file>
                        output decrypt file
  -e <file>, --enc <file>
                        output encrypt file
```



##### Interface

```
from EasyCrypt import DecryptData, EncryptData
crypter = DecryptData.decrypt_file_readline("./EasyCrypt/example/a.enc")
for line in crypter:
    print line.strip()


## decrypt file line by line, return a generator.	
# DecryptData.decrypt_file_readline("encrypt_file")     

## decrypt file and output to new file
# DecryptData.decrypt_file("encrypt_file", "decrypt_file")    

## decrypt string or python-object 
# DecryptData.decrypt_string(strings)    

## encrypt string or python-object
# EncryptData.encrypt_string(strings)   

## encrypt string or python-object
# EncryptData.encrypt_file("infile", "encrypt_file")   

```

