def vote_age_check():
    person_age= input("How old are you")
    if person_age >= 18:
        print("You can vote!")
    else:
         print("Sorry you cannt vote")

def main():
    vote_age_check()
main()
