class quiz_brain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        
    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        answer=input(f"Q.{self.question_number}: {current_question.text} (True/False)")
        if not answer==self.question_list[self.question_number-1].answer:
            print("Failed!. wrong answer")
            return False
        else:
            print (f"{answer} was the corret answer")
            return True

    def stillhasq(self):
        if self.question_list[self.question_number]:
            return True
        else:
            return False