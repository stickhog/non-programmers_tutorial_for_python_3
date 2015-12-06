__author__ = 'howardau'


# This program runs a test of knowledge
# First get the test questions
# Later this will be modified to use file io.”

# Exercise version: Expand the test.py program so it has a menu giving the option of taking the test, viewing
# the list of questions and answers, and an option to quit. Also, add a new question to ask, "What noise does a
# truly advanced machine make?" with the answer of "ping".

def get_questions():
    # a list of lists
    return [["What color is the daytime sky on a clear day? ", "blue"], ["What is the answer to life, the \
    universe, and everything? ", "42"], ["What is a three letter word for mouse trap? ", "cat"]]

# Test a single question. It takes a single question in. It returns True if the user typed the correct answer,
# otherwise returns False.

def check_question(question_and_answer):
    # Extract the question and the answer from the list. This function takes a list with two elements, a question
    # and an answer.
    question = question_and_answer[0]
    answer = question_and_answer[1]
    # give the question to the user
    given_answer = input(question)
    # compare the user's answer to the tester's answer
    if answer == given_answer:
        print("Correct")
        return True
    else:
        print("Incorrect, correct answer is: ", answer)
        return False

# this runs through all the questions
def run_test(questions):
    if len(questions) == 0:
        print("No questions were given.")
        # return exits the function
        return
    index = 0
    right = 0
    while index < len(questions):
        #check the question
        #note that this is extracting a question and answer list from the list of lists
        if check_question(questions[index]):
            right = right + 1
        #go to the next question
        index = index + 1
    # notice the order of the computation, first multiply, then divide
    print("you got", right * 100 / len(questions), \
          "% right out of", len(questions))

# now let's get the questions from the get_questions function, and
# send the returned list of lists as an argument to the run_test function
question_list = get_questions()
user_input = 0

while user_input != 9:
    print("^^^^^^^^^^^^^^^^^^")
    print("1. Run test")
    print("2. Show question list")
    user_input = int(input("Select an option: "))

    if user_input == 1:
        run_test(get_questions())

    elif user_input == 2:
        print(question_list)

    else:
        print("Invalid option.")

print("Quit")