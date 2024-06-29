import streamlit as st

def encrypt_message(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(ord(char) + shift_amount)
            if char.islower() and new_char > 'z' or char.isupper() and new_char > 'Z':
                new_char = chr(ord(new_char) - 26)
            encrypted += new_char
        else:
            encrypted += char
    return encrypted

def decrypt_message(encrypted_message, shift):
    return encrypt_message(encrypted_message, -shift)

def main():
    st.title("Decrypt the Code to Access the YouTube Link")

    # Encrypted message and the shift value
    encrypted_message = "Khoor Zruog"
    shift = 3

    st.write("Decrypt the following message to get the YouTube link:")
    st.write(f"Encrypted message: **{encrypted_message}**")

    user_input = st.text_input("Enter the decrypted message here:")

    if user_input:
        decrypted_message = decrypt_message(encrypted_message, shift)
        if user_input == decrypted_message:
            st.success("Congratulations! You've cracked the code.")
            st.write("Here is your YouTube link:")
            st.write("[Your YouTube Video](https://www.youtube.com/watch?v=dQw4w9WgXcQ)")
        else:
            st.error("Incorrect. Try again!")

if __name__ == "__main__":
    main()
