import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

PAYPAL_BUTTON_ID = os.getenv("PAYPAL_BUTTON_ID")

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
        if os.path.exists
