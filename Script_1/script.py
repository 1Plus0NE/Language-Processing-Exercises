import math

'''
    Given a number of seconds creates a tuple of days, hours, minutes and seconds
'''
def break_seconds(secs):
    days = secs // 86400
    secs %= 86400 # change secs value after days

    hours = secs // 3600
    secs %= 3600 # change secs value after hours

    minutes = secs // 60 
    seconds = secs % 60 # get secs value after minutes

    return (days, hours, minutes, seconds)

'''
    Reverses a number using arithemtic functions only
'''
def reverse_number(number):
    result = 0
    while number > 0:
        old_number = result * 10
        last_number = number % 10
        result = old_number + last_number
        number //= 10

    return result

'''
    Given a string reverses the string using slicing
'''
def reverse_str(s):
    return s[::-1]
    
'''
    Convert the given string into camel case: remove all non-alphabetic
    characters, and only characters after a non-alphabetic characters are
    ppercase, except the first
'''
def camel_case(s):
    new_str = ""

    for c in s:
        if c.isalpha():
            new_str += c.upper() if last_upper else c.lower()
        last_upper = not c.isalpha()
    
    return new_str

'''
    Shift each character in the given text according to the given value. You can
    assume only lower case characters. Leave other characters unchanged.
'''
def ceasar_cipher(shift, text):
    result = ""
    for c in text:
        if c.islower():
            idx = (ord(c) - ord('a') + shift) & (ord('z') + ord('a'))
            result += chr(idx + ord('a'))
        else:
            result += c

    return result

'''
    Implement the quadratic formula to solve ax² + bx + c = 0. 
    Result should be a tuple with 0, 1 or 2 elements.
'''
def quadritic_formula(a, b, c):
    d = b**2 - 4*a*c

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return (round(x1, 2), round(x2, 2))

    elif d == 0:
        x = -b / (2*a)
        return (round(x, 2),)

    else:
        return ()

'''
    Break down the given amount of cents in the smallest number of 200, 100, 50,
     20, 10, 5, 2, 1 cent coins.  Note: this is not a knapsack problem, you can be
    greedy.
'''
def change(amount):
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    result = []

    for coin in coins:
        if amount >= coin:
            result.append((coin, amount//coin))
            amount %= coin
    
    return result

'''
    You are given a rectangular grid and a set of instructions (U, D, L, R).
    Determine the path traversed when starting at position (0,0) and following the
    instructions. If it goes outside the grid, return None.
'''
def path(grid, instructions):
    x, y = (0,0)
    result = grid[y][x]

    for i in instructions:
        if i == 'U':
            y -= 1
        elif i == 'D':
            y += 1
        elif i == 'L':
            x -= 1
        else:
            x += 1

        if not (0 <= x < len(grid[0]) and 0 <= y < len(grid)):
            return None
        
        else:
            result += grid[y][x]
    
    return result

'''
    Read file "alunos.csv" and count the number of students.
'''
def num_students():
    number_students = 0

    with open("alunos.csv") as alunos:
        lines = alunos.readlines()
        number_students = len(lines[1:])

    return number_students    

'''
    Read file "alunos.csv" and process the data into a dictionary from student
    ids to a tuple contained the rest of the information.
'''
def load_students():
    students = {}

    with open("alunos.csv") as f:
        next(f)  # skip header

        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split(",")

            student_id = parts[0]
            nome = parts[1]
            curso = parts[2]

            tpcs = tuple(int(x) for x in parts[3:7])

            students[student_id] = (nome, curso, tpcs)

    return students

'''
    Finds the students with best average in alunos.csv.
'''
def best_average():

    students = load_students()
    best_average = 0
    best_student = ""

    for student_id, (name, course, grades) in students.items():
        temp_avg = sum(grades) / len(grades)
        if temp_avg > best_average:
            best_average = temp_avg
            best_student = student_id

    return best_student

'''
    Finds all students with average higher than 15 in alunos.csv.
'''
def good_average():

    students = load_students()
    good_students = []

    for student_id, (name, course, grades) in students.items():
        temp_avg = sum(grades) / len(grades)
        if temp_avg > 15:
            good_students.append(student_id)

    return good_students

def main():

    my_tuple = break_seconds(3601)
    print(my_tuple)

    number = reverse_number(12345)
    print(number)

    my_str = reverse_str("numero")
    print(my_str)

    camel_str = camel_case("121sssJJJ877")
    print(camel_str)

    my_ceasar = ceasar_cipher(5, "hello")
    print(my_ceasar)
    
    quadritic = quadritic_formula(1, -2, 3)
    print(quadritic)

    my_change = change(1278)
    print(my_change)

    number_students = num_students()
    print(number_students)

    students = load_students()
    print(students['"a1"'])

    best_student = best_average()
    print(best_student)

    good_students = good_average()
    print(len(good_students))

if __name__ == "__main__":
    main()