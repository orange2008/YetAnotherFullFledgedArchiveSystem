#!/usr/bin/env python3

# Note that this function is strictly operating system-sensitive. Only GNU/Linux with GNU TAR, ZSTD, and GNU Privacy Guard installed is accepted.

import os
import ffas_database as db
import hashlib

def calc_sha256sum(filename: str, BUF_SIZE=262144): # Read data as 256 kilobytes blocks, to avoid too much RAM consumption.
    sha256 = hashlib.sha256()
    with open(filename,  'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()


def archive(barcode: str):
    print("Archving and Compressing...")
    os.system("tar c ./{} | zstd -T0 -1 > {}.tar.zst".format(str(barcode), str(barcode)))
    print("Calculating Hashes...")
    digest = calc_sha256sum("./{}.tar.zst".format(barcode))
    print("SHA256SUM HexDigest: ", digest)
    print("Archived and Compressed to {}.tar.zst\nPlease manually delete the original directory.".format(barcode))
    return digest

def encrypt(barcode: str):
    """Needs to be archived earlier."""
    symmetric_key = db.random_generator(256)
    os.system("gpg --batch --yes --symmetric --cipher-algo AES256 --passphrase {} {}".format(symmetric_key, str(barcode) + ".tar.zst"))
    # print(symmetric_key)
    print("Deleting original archive...")
    os.remove(str(barcode) + ".tar.zst")
    return symmetric_key

def post_process(barcode: str, pagecount: int):
    print("-"*20)
    print("We need more information about your scanned documents.")
    name = input("Name of your document: ")
    description = input("Describe your document.\n>> ")
    original = input("Will you keep your original paper document?(y/n) ")
    if str(original).strip() != "n":
        print("Alright, you will.")
        original = 1
    else:
        print("Alright, you won't")
        original = 0
    algorithm = "aes256"
    hashalgorithm = "sha256"
    api = "gpg"
    barcode = str(barcode)
    print("Postprocessing is started for job with barcode {}".format(str(barcode)))
    sha256dgst = archive(barcode)
    aes256key = encrypt(barcode)
    print("Updating database entries...")
    # Update database
    keyUUID = db.crypto_store(aes256key, algorithm, api)
    db.paper_store(str(barcode), str(name), str(description), int(pagecount), int(original), str(keyUUID), str(sha256dgst), str(hashalgorithm))
    print("Completed.")
    