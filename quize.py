import json
import time
import sys

def load_questions(file_path):
    # Load questions from JSON file
    with open(file_path, 'r') as file:
        questions = json.load(file)
        #print(questions)
    return questions

def run_quiz(questions, time_limit_per_question=10):
    score = 0
    
    print("Welcome to the Timed Quiz Game!")
    print(f"You have {time_limit_per_question} seconds to answer each question.\n")
    
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for option, text in q['options'].items():
            print(f" {option}) {text}")

        start_time = time.time()
        answer = None
        while True:
            if time.time() - start_time > time_limit_per_question:
                print("\nTime's up! Moving to the next question.\n")
                break
            if answer is None:
                answer = input("Your answer (a/b/c/d): ").lower()
                
            if answer in q['options']:
                if answer == q['answer']:
                    print("Correct!\n")
                    score += 1
                else:
                    print(f"Wrong! The correct answer was {q['answer']}.\n")
                break
            
    print(f"Quiz Over! Your final score is {score} out of {len(questions)}.")
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python quize.py <questions_file.json>")
        return
        
if __name__ == '__main__':
    main()
    questions = load_questions('question.json')
    run_quiz(questions)
    