import random

import streamlit as st

trivia_data = [

    {

        "question": "What is the capital of France?",

        "answer": "Paris"

    },

    {

        "question": "Who painted the Mona Lisa?",

        "answer": "Leonardo da Vinci"

    },

]

def get_random_question():

    return random.choice(trivia_data)

def display_question(question):

    st.subheader("Question:")

    st.write(question["question"])

def check_answer(question, selected_answer):

    return selected_answer.lower() == question["answer"].lower()

# Streamlit app

st.title("🦉Trivia App ")

question = get_random_question()

display_question(question)

selected_answer = st.text_input("Your Answer")

timer = st.empty()

correct_answers = 0

total_questions = 0

if st.button("Check Answer"):

    total_questions += 1

    if check_answer(question, selected_answer):

        st.write("Correct!")

        correct_answers += 1

    else:

        st.write("Incorrect. The correct answer is:", question["answer"])

st.subheader("Score")

st.write(f"Correct Answers: {correct_answers}/{total_questions}")

seconds = 30

while seconds >= 0:

    timer.write(f"Time Remaining: {seconds} seconds")

    seconds -= 1

    time.sleep(1)

    if seconds < 0:

        st.write("Time's up!")

        question 

 
