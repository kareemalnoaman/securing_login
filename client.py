# This is a sample Python script.
import hashlib
import _mysql_connector


def calculate_hash(data):
    # Create a new SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Convert the password to bytes and update the hash object
    sha256_hash.update(data.encode('utf-8'))

    # Get the hexadecimal representation of the hash digest
    hash_value = sha256_hash.hexdigest()

    return hash_value




def main():
    password = "My Very Strong Password"
    hashed_password = calculate_hash(password)
    print(hashed_password)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


