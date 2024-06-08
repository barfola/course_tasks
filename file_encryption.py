def get_encrypted_file(file_path, encryption_key=5):
    with open(file_path, 'rb') as file:
        binary_data = bytearray(file.read())

    encrypted_binary_data = bytearray(byte ^ encryption_key for byte in binary_data)

    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_binary_data)


get_encrypted_file('pic.jpg', 5)
