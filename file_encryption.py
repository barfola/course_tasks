def file_encryption(file_path, encryption_key=5):
    with open(file_path, 'rb') as file:
        binary_data = bytearray(file.read())

    encrypted_binary_data = bytearray(byte ^ encryption_key for byte in binary_data)

    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_binary_data)


def file_decryption(file_path, decryption_key=5):
    with open(file_path, 'rb') as encrypted_file:
        encrypted_binary_data = bytearray(encrypted_file.read())

    decrypted_binary_data = bytearray(byte ^ decryption_key for byte in encrypted_binary_data)

    with open(file_path, 'wb') as file:
        file.write(decrypted_binary_data)



