Steganography project
Steganography is the art of hiding data in plain sight. This Python project aims to hide a message within an image using techniques that ensure that the image remains intact. The objective of this project is to embed the message within the image and then decode it.
Features
The objective of this Python project is to hide a message within an image and then decode the image using techniques that ensure the image doesn't get corrupted. The project uses the openCV module for encoding and decoding the image and is based on the Least Significant Bit (LSB) image steganography technique.
Tools Used
openCV: Used for encoding and decoding the image
Least Significant Bit (LSB) image steganography: The technique used in this project to embed the secret message into the image by modifying the last bit of each pixel.
Methodology
The project uses LSB based image steganography to embed the secret message into the image. In this technique, the last bit of each pixel is replaced with the data bit of the secret message. This results in minimal differences in the image after embedding the secret message, making it difficult to detect.
screenshot 
![17409056449998988421451409988578](https://github.com/user-attachments/assets/2dae5019-1291-46e6-98ee-5d3832ac7fb1)
![17409056936972077701279058873344](https://github.com/user-attachments/assets/ab5e2eb0-31cb-4e01-89a4-edf430c47d0a)
![17409057177031075455489570864680](https://github.com/user-attachments/assets/51a2103a-ae37-4715-b691-f479a8b3c8bd)
