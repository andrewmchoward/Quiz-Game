print("Welcome to the Cartoon Character Quiz. Enjoy!")

play_state = input("Enter 'Ready' when you would like to begin. ")

if play_state.upper() != "READY":
    print("Well, come back when you are ready then...")
    quit()

questions = ["What gem color corresponds to Marcy in the show \"Amphibia\"? ", "In \"Arcane,\" what is the name of the mad scientist that works with Silco to produce Shimmer? ", "In \"Teen Titans,\" what race is Starfire? ", "In \"Gravity Falls,\" what is the nickname of Wendy's dad? ", "In \"The Owl House,\" who did Luz get stuck in the Emperor's mind with? ", "In \"Steven Universe,\" what name did Steven give the Ruby that tricked Steven into thinking she wanted to stay on Earth, only to betray him? ", "Final Question: In \"Adventure Time,\" what is the full name of Finn's biological mother? "]
answers = ["green", "singed", "tamaranian", "manly dan", "hunter", "navy", "minerva campbell"]
counter = 0

for x in range(len(questions)):
    answer = input(questions[x])
    if answer.upper() == answers[x].upper():
        counter += 1
        if x != len(questions) - 1:
            print(f"Nice job! Your score is currently {counter}!")
        else:
            print(f"Strong finish! Your final score is {counter}!")
    else:
        if x != len(questions) - 1:
            print(f"Incorrect, your score is still {counter}!")
        else:
            print(f"Incorrect, but nice try! With that, your final score is {counter}!")

if counter == 7:
    print(f"CONGRATULATIONS, you got every question correct!")

