def grading(): 
    try:
        # taking marks from users
        sub1 = float(input("Marks of first subject -> "))
        sub3 = float(input("Marks of third subject -> "))
        sub2 = float(input("Marks of second subject -> "))
        if sub1 < 0 or sub1 > 100 or sub2 < 0 or sub2 > 100 or sub3 < 0 or sub3 > 100:
            print("\n[Enter Valid marks! (0-100)]\n")
        else:
        # calculating total and avg
            total = sub1 + sub2 + sub3
            avg = total/3
            avg = round(avg, 2)
            # calculating grade
            if avg >=90:
                grade = "A"
            elif avg >= 75:
                grade = "B"
            elif avg >= 60:
                grade = "C"
            elif avg >= 33:
                grade = "D"
            else:
                grade = "E"
            result = f"Total marks : {total}\nAverage Marks : {avg}\nGrade : {grade}"
            print(result)
    # preventing str input
    except ValueError as v:
        return print(f"\n[Invalid Input ({v})]\n")

grading()