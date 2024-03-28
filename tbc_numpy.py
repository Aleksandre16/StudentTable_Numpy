import numpy as np
import random


def generate_full_name():
    first_names = ['ვენერა', 'თინა', 'თეა', 'სოსო', 'მირანდა', 'ჟენია', 'ტატიანა', 'ედუარდ', 'კლარა', 'სიმონ', 'ანზორ',
                   'სოფია', 'სოსო', 'ნელი', 'ბონდო', 'ედუარდ', 'სონია', 'არჩილ', 'მარიამ', 'სოფია', 'ემა', 'იზოლდა',
                   'ომარ',
                   'ტატიანა', 'ვიქტორ', 'კარინე', 'გუგული', 'კახა', 'როზა', 'რუსუდან', 'სიმონ', 'ნელი', 'ბადრი',
                   'მადონა',
                   'ირინე', 'მინდია', 'ნათია', 'გულნარა', 'კახა', 'ელზა', 'როინ', 'ნაირა', 'ლიანა', 'ნინელი', 'მაყვალა',
                   'რეზო', 'ჟუჟუნა', 'ზინა', 'გოჩა', 'მურმან']
    last_names = ['ქუთათელაძე', 'მეგრელიშვილი', 'სალუქვაძე', 'ხარაიშვილი', 'შელია', 'კევლიშვილი', 'ბუჩუკური',
                  'ტყებუჩავა',
                  'მიქაბერიძე', 'ურუშაძე', 'ძიძიგური', 'გოგუაძე', 'ანთაძე', 'ვალიევა', 'როგავა', 'ნაკაშიძე', 'ღურწკაია',
                  'გვაზავა', 'გვასალია', 'ზარანდია', 'სხირტლაძე', 'ბერაძე', 'ხვიჩია', 'ბასილაშვილი', 'კაკაბაძე',
                  'მერებაშვილი', 'ნოზაძე', 'ხარაბაძე', 'მუსაევა', 'მამულაშვილი', 'ელიზბარაშვილი', 'მამულაშვილი',
                  'ჯოჯუა',
                  'გულუა', 'ხალვაში', 'ხარატიშვილი', 'დუმბაძე', 'ბერიანიძე', 'ჯოხაძე', 'სამხარაძე', 'ლიპარტელიანი',
                  'იობიძე', 'გაბაიძე', 'ხარაბაძე', 'ინასარიძე', 'ბერაძე', 'შენგელია', 'ქობალია', 'მიქავა',
                  'რევაზიშვილი']

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f"{first_name} {last_name}"


def build_up():
    rows = 100
    columns = 7
    matrix = np.empty((rows, columns), dtype="U50")

    for i in range(100):
        matrix[i, 0] = generate_full_name()

    subjects = ["Math", "Physics", "Chemistry", "Biology", "English"]
    for i, subject in enumerate(subjects, start=1):
        matrix[0, i] = subject

    for row in range(1, 100):
        for column in range(1, 6):
            matrix[row, column] = str(random.randint(1, 100))

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print("\t".join(row))


def highest_average_score(score_board):
    total_scores = score_board[1:, 1:6].astype(int).sum(axis=1)
    avg_scores = total_scores / 5
    highest_avg = np.max(avg_scores)
    top_students = score_board[1:, 0][avg_scores == highest_avg]

    print("Top Student:")
    print(", ".join(top_students))
    print(f"Average Score: {highest_avg}")
    print("___________________________")


def best_and_worst(score_board):
    math_scores = score_board[1:, 2].astype(int)
    highest_math_score = np.max(math_scores)
    lowest_math_score = np.min(math_scores)

    top_math_students = score_board[1:, 0][math_scores == highest_math_score]
    low_math_students = score_board[1:, 0][math_scores == lowest_math_score]

    print("Top Student in Math:")
    print(", ".join(top_math_students))
    print(f"Highest Math Score: {highest_math_score}")
    print("__________________________________")

    print("Lowest Scoring Student in Math:")
    print(", ".join(low_math_students))
    print(f"Lowest Math Score: {lowest_math_score}")


def above_average_english(score_board):
    english_scores = score_board[1:, 5].astype(int)
    avg_score = np.mean(english_scores)
    above_avg_students = score_board[1:, 0][english_scores > avg_score]

    print("Students Above Average in English:")
    print(", ".join(above_avg_students))


score_board = build_up()
print("Generated Scoreboard:")
print_matrix(score_board)
print("\n")
highest_average_score(score_board)
best_and_worst(score_board)
above_average_english(score_board)
