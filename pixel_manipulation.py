from PIL import Image 
import numpy as np

def load_image(image_path):
    return Image.open(image_path)

def save_image(image, path):
    image.save(path)

def encrypt_image(image):
    image_data = np.array(image)
    encrypted_data = image_data.copy()
    height, width, channels = encrypted_data.shape
    for i in range(height):
        for j in range(0, width, 2):
            if j + 1 < width:
                encrypted_data[i, j], encrypted_data[i, j + 1] = encrypted_data[i, j + 1], encrypted_data[i, j]
    encrypted_data = (encrypted_data + 50) % 256
    encrypted_image = Image.fromarray(encrypted_data.astype('uint8'))
    return encrypted_image

def decrypt_image(image):
    image_data = np.array(image)
    decrypted_data = (image_data - 50) % 256
    height, width, channels = decrypted_data.shape
    for i in range(height):
        for j in range(0, width, 2):
            if j + 1 < width:
                decrypted_data[i, j], decrypted_data[i, j + 1] = decrypted_data[i, j + 1], decrypted_data[i, j]

    decrypted_image = Image.fromarray(decrypted_data.astype('uint8'))
    return decrypted_image

def main():
    operation = input("Enter encrypt or decrypt for image: ").strip().lower()

    if operation not in ['encrypt', 'decrypt']:
        print("Invalid, Please enter 'encrypt' or 'decrypt'.")
        return

    image_path = input("Enter the Path: ").strip()

    try:
        image = load_image(image_path)
    except Exception as e:
        print(f"Error in loading: {e}")
        return

    if operation == 'encrypt':
        result_image = encrypt_image(image)
        result_image_path = 'encrypted_image.png'
    else:
        result_image = decrypt_image(image)
        result_image_path = 'decrypted_image.png'

    save_image(result_image, result_image_path)
    print(f"{operation.capitalize()}ed image saved as {result_image_path}")
    result_image.show(title=f"{operation.capitalize()}ed Image")

if __name__ == "__main__":
    main()