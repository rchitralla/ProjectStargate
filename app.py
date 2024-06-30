def main():
    st.title("Project Stargate - an unscientific comedy")

    # Display an image at the start
    st.markdown(
        """
        <div style='text-align: center;'>
            <img src='Title.jpeg' width='300'>
        </div>
        """,
        unsafe_allow_html=True
    )

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

    if st.session_state.get("riddle_solved"):
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

    if st.session_state.get("password_solved"):
        philosophical_puzzle_solver()

    if st.session_state.get("puzzle_solved"):
        philosopher_or_psychic()

    if st.session_state.get("quiz_solved"):
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
    if "riddle_solved" not in st.session_state:
        st.session_state.riddle_solved = False
    if "password_solved" not in st.session_state:
        st.session_state.password_solved = False
    if "puzzle_solved" not in st.session_state:
        st.session_state.puzzle_solved = False
    if "quiz_solved" not in st.session_state:
        st.session_state.quiz_solved = False
    
    main()
