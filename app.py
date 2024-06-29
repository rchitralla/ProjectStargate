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

def philosophical_puzzle_solver():
    st.title("Philosophical Puzzle Solver")
    st.write("Solve the following philosophical puzzle to proceed:")

    puzzle = "I think, therefore I am. Who said this famous quote?"
    options = ["Plato", "Aristotle", "Descartes", "Socrates"]
    correct_answer = "Descartes"
    
    user_answer = st.radio(puzzle, options)  # Remove index=-1 to avoid pre-selection error
    
    if st.button("Submit Puzzle Answer"):
        if user_answer:
            if user_answer == correct_answer:
                st.success("Correct! Here is a clip from behind the scenes.")
                st.video("https://www.youtube.com/watch?v=rG5iCV4xza4&t=46s&ab_channel=ReelStreamVenture")  # Replace with actual clip
            else:
                st.error("Incorrect! Try again.")

def philosopher_or_psychic():
    # Quotes or scenarios with their correct answers
    quiz_data = [
        {"quote": "The only true wisdom is in knowing you know nothing.", "answer": "Philosopher", "source": "Socrates"},
        {"quote": "I see a great fortune in your future.", "answer": "Psychic", "source": "Generic Psychic"},
        {"quote": "To be is to do.", "answer": "Philosopher", "source": "Socrates"},
        {"quote": "I sense a strong aura around you.", "answer": "Psychic", "source": "Generic Psychic"},
        {"quote": "The unexamined life is not worth living.", "answer": "Philosopher", "source": "Socrates"},
        {"quote": "You will find love soon.", "answer": "Psychic", "source": "Generic Psychic"},
        {"quote": "Happiness is not an ideal of reason but of imagination.", "answer": "Philosopher", "source": "Immanuel Kant"},
        {"quote": "You have a very strong energy field.", "answer": "Psychic", "source": "Generic Psychic"},
    ]

    st.title("Philosopher or Psychic?")

    st.write("Decide if the following quotes are from a famous philosopher or a psychic.")

    score = 0
    total_questions = len(quiz_data)

    for i, item in enumerate(quiz_data):
        st.write(f"Quote {i + 1}: {item['quote']}")
        user_answer = st.radio("Is this quote from a Philosopher or a Psychic?", ("Philosopher", "Psychic"), key=f"quiz_{i}")

        if st.button(f"Submit Answer {i + 1}"):
            if user_answer:
                if user_answer == item["answer"]:
                    st.success(f"Correct! This quote is from {item['source']}.")
                    score += 1
                else:
                    st.error(f"Incorrect. This quote is from {item['source']}.")

    st.write(f"Your final score is {score} out of {total_questions}")

def main():
    st.title("Decrypt the Code to Access a Special Message")

    # First encrypted message and the shift value
    encrypted_message1 = "Vohdcb Vwhyh"
    shift1 = 3
    youtube_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with your actual "Sleazy Steve" YouTube link

    st.write("Decrypt the following message to get a special YouTube link:")
    st.write(f"Encrypted message: **{encrypted_message1}**")

    user_input1 = st.text_input("Enter the decrypted message here:", key="input1")

    if user_input1:
        decrypted_message1 = decrypt_message(encrypted_message1, shift1)
        if user_input1 == decrypted_message1:
            st.success("Congratulations! You've cracked the first code. Sleazy Steve is the sleaziest of Sleazes.")
            st.write("Here is your special YouTube link:")
            st.write(f"[Your YouTube Video]({youtube_link})")

            # Second challenge
            st.title("Super Secret Password Hacker")
            st.write("Now, crack John's computer password:")
            st.write("Hint: John only remembers up to three numbers at a time.")
            user_input2 = st.text_input("Enter John's password here:", key="input2")

            if user_input2:
                if user_input2 == "123":
                    st.success("Congratulations! You've cracked John's password.")
                    philosophical_puzzle_solver()
                    philosopher_or_psychic()
                else:
                    st.error("Incorrect password. Try again!")

if __name__ == "__main__":
    main()
