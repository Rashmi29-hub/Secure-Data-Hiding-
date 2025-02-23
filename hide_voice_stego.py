import wave
import numpy as np
from cryptography.fernet import Fernet

# Generate encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_message(message):
    """Encrypt the message before hiding."""
    return cipher.encrypt(message.encode())

def hide_message(audio_file, message, output_file):
    """Hide the encrypted message inside the least significant bits of the audio file."""
    # Open the WAV file
    audio = wave.open(audio_file, 'rb')
    frame_bytes = bytearray(audio.readframes(audio.getnframes()))

    # Encrypt the message and convert to binary
    encrypted_msg = encrypt_message(message)
    binary_message = ''.join(format(byte, '08b') for byte in encrypted_msg) + '1111111111111110'  # End marker

    # Hide binary message in silent parts
    index = 0
    for i in range(0, len(frame_bytes), 2):  # Modify every second frame
        if index < len(binary_message):
            frame_bytes[i] = (frame_bytes[i] & 254) | int(binary_message[index])
            index += 1

    # Save the stego-audio file
    with wave.open(output_file, 'wb') as stego_audio:
        stego_audio.setparams(audio.getparams())
        stego_audio.writeframes(bytes(frame_bytes))
    
    audio.close()
    return key  # Return encryption key for decryption

# Run the function to hide the message
audio_file = "input_voice.wav"  # Make sure this file exists in your directory
output_file = "stego_voice.wav"
hidden_message = "This is a hidden secret message!"
encryption_key = hide_message(audio_file, hidden_message, output_file)

print("Hidden message stored successfully!")
print("Encryption Key (Save this to decrypt):", encryption_key.decode())
