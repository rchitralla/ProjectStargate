import streamlit as st
import os
from dotenv import load_dotenv
from streamlit_cookies_manager import EncryptedCookieManager

# Load environment variables
load_dotenv()

# Initialize cookies manager
cookies = EncryptedCookieManager(prefix="pg_", password="a_secure_password_key")
if not cookies.ready():
    st.stop()

# PayPal button ID
PAYPAL_BUTTON_ID = os.getenv("PAYPAL_BUTTON_ID")

# Initialize the counter in session state
if "unique_visits" not in st.session_state:
    if not cookies.get("visit_count"):
        cookies["visit_count"] = "1"
        st.session_state.unique_visits = 1
    else:
        st.session_state.unique_visits = int(cookies.get("visit_count"))

def increment_unique_visits():
    st.session_state.unique_visits += 1
    cookies["visit_count"] = str(st.session_state.unique_visits)

# Increment the counter if the user is new
if not cookies.get("user_visited"):
    cookies["user_visited"] = "true"
    increment_unique_visits()

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
                st.session_state.puzzle_solved = True
            else:
                st.error("Incorrect! Try again.")

def philosopher_or_psychic():
    # Quotes or scenarios with their correct answers
    quiz_data = [
        {"quote": "The only true wisdom is in knowing you know nothing.", "answer": "Philosopher", "source": "Socrates"},
        {"quote": "I see a great change coming into your life, possibly involving embracing that 70's look!", "answer": "Psychic", "source": "Generic Psychic"},
        {"quote": "To be is to do.", "answer": "Philosopher", "source": "Socrates"},
        {"quote": "I sense a strong energy around you, likely from that disco fever.", "answer": "Psychic", "source": "Generic Psychic"},
        {"quote": "I see you remote viewing your fridge late at night.", "answer": "Psychic", "source": "Generic Psychic"},
        {"quote": "Happiness is not an ideal of reason but of imagination.", "answer": "Philosopher", "source": "Immanuel Kant"},
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
        st.session_state.quiz_solved = True

def main():
    st.title("Project Stargate - an unscientific comedy")

    # Initialize session state variables
    if "riddle_solved" not in st.session_state:
        st.session_state.riddle_solved = False
    if "password_solved" not in st.session_state:
        st.session_state.password_solved = False
    if "puzzle_solved" not in st.session_state:
        st.session_state.puzzle_solved = False
    if "quiz_solved" not in st.session_state:
        st.session_state.quiz_solved = False

    # Display an image at the start using st.image
    st.image('Title.jpeg', caption='Project Stargate', width=300)

    # Description of the pilot episode project
    st.write("""
    **PROJECT STARGATE**

    Congrats, you have been invited to the super secret recruitment program by Project Stargate - an unscientific comedy. 
    The comedy follows John, an underemployed philosophy grad, who infiltrates the Department of Inexplicable Affairs (DIA) because his nemesis ´Sleazy Steve´ leads him there. 
    Being mistaken for a deceased psychic rockstar, he lands a job. 
    Thrust into a world of psychic espionage he's hilariously unprepared for, John relies on his philosophical insights and knack for improvisation.
    His only ally is a cryptic janitor with a thick Russian accent and mysterious proverbs. 

    After solving the riddles, you will be able to watch the trailer and hopefully you like it so much, you want to support us with a donation. 
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
            st.session_state.riddle_solved = True
        elif user_input1.lower() == "sleezy":
            st.warning("Almost correct, try again.")
        else:
            st.error("Incorrect! Try again.")

    if st.session_state.riddle_solved:
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
                st.session_state.password_solved = True
            else:
                st.error("Incorrect password. Try again!")

    if st.session_state.password_solved:
        philosophical_puzzle_solver()

    if st.session_state.puzzle_solved:
        philosopher_or_psychic()

    if st.session_state.quiz_solved:
        # Add the new lottery numbers question at the end
        st.title("Guess the Next Lottery Numbers")
        st.write("Clairvoyance is an important skill, hence you should be able to foresee the lottery numbers.")
        lottery_input = st.text_input("Enter your guess for the next lottery numbers:")

        if lottery_input:
            st.success("Congrats, you passed and are hired!")

    # Add PayPal donation button as a clickable link styled as a button
    st.markdown(
        f"""
        <a href="https://www.paypal.com/donate?hosted_button_id={PAYPAL_BUTTON_ID}" target="_blank">
            <button style="background-color:#4CAF50; border:none; color:white; padding:15px 32px; text-align:center; text-decoration:none; display:inline-block; font-size:16px; margin:4px 2px; cursor:pointer;">
                Donate via PayPal
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

    # Smaller credit text and visitor counter at the bottom
    st.markdown(
        f"""
        <div style='text-align: center; margin-top: 50px; font-size: 12px;'>
            Created by Regina Chitralla
        </div>
        <div style='text-align: center; font-size: 12px;'>
            Unique Page Visits: {st.session_state.unique_visits}
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
