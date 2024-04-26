def score_grade(score,best_score): #this function calcs a letter grade for current score and best score.
    if score >= best_score - 10:
        return 'A'
    if score >= best_score - 20:
        return 'B'
    if score >= best_score - 30:
        return 'C'
    if score >= best_score - 40:
        return 'D'
    else:
        return 'F'
def main():
    students = int(input("Enter the total number of students: "))
    scores_ints = []
    scores_entered_str = []

    while len(scores_entered_str) < students:
        scores_entered_str = input(f'Enter {students} score(s): ').split()

    i = 0
    while len(scores_ints) < len(scores_entered_str):
        scores_ints.append(int(scores_entered_str[i]))
        i += 1

    best_score = max(scores_ints)

    for i in range(len(scores_ints)):
        print(f'Student {i + 1} score is {scores_ints[i]}, and grade is, {score_grade(scores_ints[i], best_score)}')

    avg_score = sum(scores_ints) / len(scores_ints)
    print(f'The average score is {avg_score:.2f}, a grade of {score_grade(avg_score, best_score)}')


if __name__=="__main__":
    main()

