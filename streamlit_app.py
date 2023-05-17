import random

import streamlit as st

# Trivia dataset

trivia_data = [

    {

        "question": "What is the capital of France?",

        "options": ["Paris", "London", "Berlin", "Madrid"],

        "answer": "Paris"

    },

    {

        "question": "Who painted the Mona Lisa?",

        "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],

        "answer": "Leonardo da Vinci"

    },

    # Add more trivia questions here

]

def get_random_question():

    return random.choice(trivia_data)

def display_question(question):

    st.subheader("Question:")

    st.write(question["question"])

    st.subheader("Options:")

    for option in question["options"]:

        st.write(option)

def check_answer(question, selected_option):

    return selected_option == question["answer"]

# Streamlit app

st.title("Trivia App")

# Get a random question

question = get_random_question()

# Display the question and options

display_question(question)

# User's answer

selected_option = st.radio("Select your answer:", question["options"])

# Check the answer

if st.button("Check Answer"):

    if check_answer(question, selected_option):

        st.write("Correct!")

    else:

        st.write("Incorrect. The correct answer is:", question["answer"])

