def calculate_average(m1, m2, m3):
    return (m1 + m2 + m3) / 3

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def call():
     
    m1 = int(input("Enter mark 1 : "))
    m2 = int(input("Enter mark 2 : "))
    m3 = int(input("Enter mark 3 : "))

    average = calculate_average(m1, m2, m3)

    grade = get_grade(average)

    print (f"Marks = ", m1 , m2 , m3)
    print (f"Average = ", average)
    print (f"Grade = ", grade)

call()