try:
    question_bank = open("questions.txt", "w")
    answer_bank = open("quiz_answers.txt", "w")

    questions = ["Who is the greatest person on Earth? (a)Udbhav (b)Nasser (c)Yourself (d)Khalil ",
                 "Name the disease which ruined your summer. (a)Malaria (b)Typhoid (c)COVID-19 (d)Jaundice",
                 "Which programming language is this quiz written in? (a)C++ (b)Java (c)R (d)Python",
                 "Which is the best kind of food? (a)Healthy (b)Junk (c)Diet (d)Fibrous "]

    for stuff in questions:
        question_bank.write("%s\n" % stuff)

    answers = ["a", "c", "d", "b"]
    for items in answers:
        answer_bank.write("%s\n" % items)

    options = ['a', 'b', 'c', 'd']

    question_bank = open("questions.txt", "r")
    answer_bank = open("quiz_answers.txt", "r")


    def remove_questions():
        global answers, questions
        question_bank = open("questions.txt", "r")

        for each in question_bank.readlines():
            print(each)
        print("")
        print("These are the questions now.")

        remove_index = int(input("Enter the index of the question you want to remove: "))
        index_choices = []
        for i in range(0, len(questions)):
            index_choices.append(i)
        print(index_choices)

        while remove_index not in index_choices:
            remove_index = int(input("Enter the index of the question you want to remove: "))

        else:
            sure = input("Are you sure you want to delete the question: " + questions[remove_index] + " : ")

            while sure.lower() == 'no':
                retry_index = int(input("Enter the index of the question you want to remove: "))
                retry_sure = input("Are you sure you want to delete the question: " + questions[retry_index] + " : ")
                if str(retry_sure.lower()) == 'yes':
                    remove_index = retry_index
                    sure = 'yes'

            if str(sure.lower()) == 'yes':
                question_bank = open("questions.txt", "w")
                answer_bank = open("quiz_answers.txt", "w")
                del questions[remove_index]
                del answers[remove_index]
                for new in questions:
                    question_bank.write("%s\n" % new)
                for new_ans in answers:
                    answer_bank.write("%s\n" % new_ans)
                question_bank.close()
                answer_bank.close()

                question_bank = open('questions.txt', 'r')
                answer_bank = open('quiz_answers.txt', 'r')
                print("")
                for i in question_bank.readlines():
                    print(i)
                print("")
                for a in answer_bank.readlines():
                    print(a)
                print("")
                print("are the questions and answers now.")


    def run_quiz():
        num = 1
        score = 0
        wrong = []
        correct = []
        with open('questions.txt', 'r') as f:
            lines = f.read().splitlines()
            question_bank = open('questions.txt', 'r')
            answer_bank = open('quiz_answers.txt', 'r')
        while num <= len(lines):
            # print(len(lines))
            question = question_bank.readline()
            print("")
            print(question)
            g = open("quiz_given.txt", "w")
            player_answer = [input("Your answer: ")]

            for given in player_answer:
                g.write("%s\n" % given)

            g = open("quiz_given.txt", "r")
            move = g.readline()
            answer = answer_bank.readline()

            if str(move.lower()[0]) not in options:
                print("I don't understand. Please type the letter which corresponds to your answer from next time.")
                again = input("Try again: ")
                while again.lower() not in options:
                    again = input("Try again: ")
                else:
                    print("You can carry on now.")
                    g = open("quiz_given.txt", "w")
                    g.write("%s\n" % again)
                    g = open("quiz_given.txt", "r")
                    move = g.readline()
                    g.close()

            if str(move.lower()) == str(answer):
                correct.append(question)
                score += 1

            elif str(move.lower()) != str(answer):
                wrong.append(str(question))

                score += 0
            num += 1
        print("")
        print("Your score is", score, "out of", len(lines))
        # c = open("rectified.txt", "r")
        print("")
        for wrong_question in wrong:
            print(wrong_question, "was answered incorrectly by you.")
        print("")

        for correct_answer in correct:
            print(correct_answer, "was answered correctly by you.")
        print("")
        answer_bank = open('quiz_answers.txt', 'r')
        for one in answer_bank.readlines():
            print(one)
        print("are the answers to the questions respectively.")


    def login():
        global question_bank, answer_bank
        password_tries = 2
        password_count = 0
        commands = ['add', 'remove', 'exit']
        while True:
            login_mode = input("You are logging in as (player/admin): ")
            password = "1234"
            login_options = ['player', 'admin']

            if login_mode.lower() == "admin":
                while password_count <= password_tries:
                    password_given = input("Password: ")
                    if str(password_given) == password:
                        password_count = password_tries
                        print("Hello now you can add or remove questions.")
                        command_given = input('''
    Type 'add','remove' or 'exit' to add or remove  questions or exit respectively: ''')
                        if str(command_given.lower()) not in commands:
                            print("I don't understand. Please type 'add' or 'remove'.")
                            retry = input("Enter yor command again: ")
                            while retry.lower() not in commands:
                                retry = input("Try again: ")
                            else:
                                print("You can carry on now.")
                                command_given = retry
                        while str(command_given.lower()) != 'exit':
                            if str(command_given.lower()) == 'add':
                                add_question = input('''Please enter your question in the format-
    Whatever your question is? (a)option1 (b)option2 (c)option3 (d)option4: ''')
                                add_answer = input('''Enter the answer to your new question(enter only the letter which
    corresponds to your answer: ''')
                                question_bank = open("questions.txt", "a")
                                question_bank.write("%s\n" % str(add_question))
                                question_bank.close()
                                answer_bank = open("quiz_answers.txt", "a")
                                answer_bank.write("%s\n" % add_answer)
                                answer_bank.close()

                                command_given = input('''
    Type 'add','remove' or 'exit' to add or remove  questions or exit respectively: ''')

                            if command_given == 'remove':
                                remove_questions()
                                break
                        if command_given == 'exit':
                            question_bank = open("questions.txt", "r")
                            answer_bank = open("quiz_answers.txt", "r")
                            print("")
                            for new_question_set in question_bank.readlines():
                                print(new_question_set)
                            for new_answers_set in answer_bank.readlines():
                                print(new_answers_set)
                            print("The above mentioned are the questions and answers now.")
                            question_bank.close()
                            answer_bank.close()
                            break
                    else:
                        password_count += 1
                    if password_count >= password_tries:
                        print("")
                        break
            elif login_mode.lower() == "player":
                run_quiz()
            elif login_mode.lower() not in login_options:
                print("Type 'player' to play the quiz or type 'admin' if you are an administrator.")
                break


    login()

except ValueError:
    print("Hey you got a ValueError.")
except SyntaxError:
    print("Hey you got a SyntaxError")
except:
    print("Hey you got an error. Its not a ValueError or a SyntaxError. Check your program.")
