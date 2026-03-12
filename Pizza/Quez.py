
score = 0
def ask_question(question, op1, op2, op3, answer):
    print(question)
    print(op1)
    print(op2)
    print(op3)
    choice = input("Enter your choice:")
    answer_ref: str | None =  None
    if choice >= 1 or choice <= 2:
        if choice == 1:
            answer_ref = op1
        elif choice == 2:
            answer_ref = op2
        elif choice == 3:
            answer_ref = op3
    else:
        answer_ref = None

   


