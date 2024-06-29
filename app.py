import streamlit as st
import os

def philosophical_puzzle_solver():
    st.title("Philosophical Puzzle Solver")
    st.write("Solve the following philosophical puzzle to proceed:")

    puzzle = "I think, therefore I am. Who said this famous quote?"
    options = ["Plato", "Aristotle", "Descartes", "Socrates", "John"]
    correct_answer = "Descartes"
    
    user_answer = st.radio(puzzle, options, key="puzzle_radio")  # Use a key to avoid conflict
    
    if st.button("Submit Puzzle Answer", key="puzzle_submit"):
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
        {"quote": "I see a great change coming into your life, possibly involving a new pair of bell-bottoms.", "answer": "Psychic", "source": "Generic Psychic"},
        {"quote": "To be is to do.", "answer": "Philosopher", "source": "Socrates"},
        {"quote": "I sense a strong energy around you, likely from that disco fever.", "answer": "Psychic", "source": "Generic Psychic"},
        {"quote": "The unexamined life is not worth living.", "answer": "Philosopher", "source": "Socrates"},
        {"quote": "You will find love very soon, perhaps at the roller rink.", "answer": "Psychic", "source": "Generic Psychic"},
        {"quote": "Happiness is not an ideal of reason but of imagination.", "answer": "Philosopher", "source": "Immanuel Kant"},
        {"quote": "I see you remote viewing your fridge late at night.", "answer": "Psychic", "source": "Generic Psychic"},
    ]

    st.title("Philosopher or Psychic?")
    st.write("Decide if the following quotes are from a famous philosopher or a psychic.")

    score = 0
    total_questions = len(quiz_data)
    all_answered_correctly = True

    for i, item in enumerate(quiz_data):
        if f"answered_{i}" not in st.session_state:
            st.session_state[f"answered_{i}"] = False

        st.write(f"Quote {i + 1}: {item['quote']}")
        if not st.session_state[f"answered_{i}"]:
            user_answer = st.radio("Is this quote from a Philosopher or a Psychic?", ("Philosopher", "Psychic"), key=f"quiz_{i}")

            if st.button(f"Submit Answer {i + 1}", key=f"submit_{i}"):
                st.session_state[f"user_answer_{i}"] = user_answer
                st.session_state[f"answered_{i}"] = True

        if st.session_state[f"answered_{i}"]:
            user_answer = st.session_state[f"user_answer_{i}"]
            if user_answer == item["answer"]:
                st.success(f"Correct! This quote is from {item['source']}.")
                score += 1
            else:
                st.error(f"Incorrect. This quote is from {item['source']}.")
                all_answered_correctly = False

    st.write(f"Your final score is {score} out of {total_questions}")

    if all_answered_correctly and score == total_questions:
        st.write("Congratulations! You have answered all questions correctly. Download your special image below:")
        if os.path.exists("ProjectStargate_Poster_4K.png"):
            with open("ProjectStargate_Poster_4K.png", "rb") as file:
                btn = st.download_button(
                    label="Download Congratulations Image",
                    data=file,
                    file_name="ProjectStargate_Poster_4K.png",
                    mime="image/png"
                )
        else:
            st.error("The file ProjectStargate_Poster_4K.png was not found.")

def main():
    st.title("Project Stargate - an unscientific comedy")

    # Description of the pilot episode project
    st.write("""
    **PROJECT STARGATE**

    This uproarious comedy follows John, an underemployed philosophy grad, who accidentally infiltrates the Department of Inexplicable Affairs (DIA) after being mistaken for a deceased psychic prodigy.
    Thrust into a world of psychic espionage he's hilariously unprepared for, John relies on his philosophical insights and knack for improvisation.
    His only ally is a cryptic janitor with a thick Russian accent and mysterious proverbs. Together, they navigate absurd bureaucratic challenges and over-the-top missions, with John's pseudo-philosophical babble inadvertently solving real psychic mysteries.
    This series blends bureaucratic absurdity with psychic phenomena, creating a world where the only thing taken seriously is the art of not taking anything seriously.
    """)

    # New riddle and the answer
    riddle = "I am a word often used to describe someone who is disreputable or dishonest. I rhyme with 'breezy' but mean something far from pleasant. What am I?"
    correct_answer = "Sleazy"
    youtube_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with your actual "Sleazy Steve" YouTube link

    st.write("Solve the following riddle to get a special YouTube link:")
    st.write(f"Riddle: **{riddle}**")

    user_input1 = st.text_input("Enter the answer here:", key="input1")

    if user_input1:
        if user_input1.lower() == correct_answer.lower():
            st.success("Congratulations! You've solved the riddle. Sleazy Steve is the sleaziest of Sleazes.")
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
                    st.write("Download your special sticker below:")
                    if os.path.exists("Sure_Drink.pdf"):
                        with open("Sure_Drink.pdf", "rb") as file:
                            btn = st.download_button(
                                label="Download Sticker",
                                data=file,
                                file_name="Sure_Drink.pdf",
                                mime="application/pdf"
                            )
                    else:
                        st.error("The file Sure_Drink.pdf was not found.")
                    philosophical_puzzle_solver()
                    philosopher_or_psychic()
                else:
                    st.error("Incorrect password. Try again!")

    st.write("Created by Regina Chitralla")

    # Add PayPal donation button using HTML form
    st.markdown(
        """
        <form action="https://www.paypal.com/donate" method="post" target="_top">
        <input type="hidden" name="hosted_button_id" value="8TTFV24WNWLS4" />
        <input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
        <img alt="" border="0" src="https://www.paypal.com/en_DE/i/scr/pixel.gif" width="1" height="1" />
        </form>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
