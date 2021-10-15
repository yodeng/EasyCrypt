import sys
import argparse

from EasyCrypt import EncryptData, DecryptData
from EasyCrypt.utils import UsageError


def parseArgs():
    parser = argparse.ArgumentParser(
        description="simple encrypt and decrypt for files")
    parser.add_argument('-i', '--input', required=False,
                        help='input file for encrypt/decrypt', metavar="<file>")
    parser.add_argument(
        '-d', '--dec', help='output decrypt file', metavar="<file>")
    parser.add_argument(
        '-e', '--enc', help='output encrypt file', metavar="<file>")
    return parser.parse_args()


def main():
    args = parseArgs()
    if args.dec and args.enc:
        raise UsageError("conflict args.")
    if (args.dec is None) and (args.enc is None):
        raise UsageError("enc/dec output omit.")
    if args.dec:
        DecryptData.decrypt_file(args.input, args.dec)
    elif args.enc:
        EncryptData.encrypt_file(args.input, args.enc)


if __name__ == "__main__":
    main()
