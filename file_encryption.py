def encrypted_image(file_path):
    with open('try.jpg', 'rb') as file:
        binary_data = bytearray(file.read())
        print(binary_data[0] ^ 1)
        n = binary_data[0] ^ 1
        byte_ob = n.to_bytes(1, byteorder='big')
        print(byte_ob)
    with open('picture_en.jpg', 'wb') as encrypted_pic:
        encrypted_pic.write(byte_ob)


encrypted_image('s')

