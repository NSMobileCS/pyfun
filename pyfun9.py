from random import randrange

def genTen():
    for _ in range(10):
        grade = 'A'
        score = randrange(60,101)
        if 80 < score <= 90:
            grade = 'B'
        elif 70 < score <= 80:
            grade = 'C'
        elif score <= 70:
            grade = 'D'
        print("Score: {}; Your grade is {}".format(score, grade))
    print("end of the program - bye!")

    
if __name__ == '__main__':
    genTen()