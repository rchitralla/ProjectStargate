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
    st.title("Decrypt the Code to Access a Special Message")

    # First encrypted message and the shift value
    encrypted_message1 = "Vohdcb Vwhyh"
    shift1 = 3
    youtube_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with your actual "Sleazy Steve" YouTube link

    st.write("Decrypt the following message to get a special YouTube link:")
    st.write(f"Encrypted message: **{encrypted_message1}**")

    user_input1 = st.text_input("Enter the decrypted message here:")

    if user_input1:
        decrypted_message1 = decrypt_message(encrypted_message1, shift1)
        if user_input1 == decrypted_message1:
            st.success("Congratulations! You've cracked the first code. Sleazy Steve is the sleaziest of Sleazes.")
            st.write("Here is your special YouTube link:")
            st.write(f"[Your YouTube Video]({youtube_link})")

            # Second challenge
            st.write("Now, crack John's password:")
            st.write("Hint: John only remembers up to three numbers at a time.")
            user_input2 = st.text_input("Enter John's password here:")

            if user_input2:
                if user_input2 == "123":
                    st.success("Congratulations! You've cracked John's password.")
                else:
                    st.error("Incorrect password. Try again!")

if __name__ == "__main__":
    main()
