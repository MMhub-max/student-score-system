def show_student():
    score = float(input("请输入学生成绩："))
    print(f"学生成绩：{score}")
    name = input("请输入学生姓名：")
    print(f"学生姓名：{name}")
    student_id = input("请输入学生学号：")
    print(f"学生学号：{student_id}")
    major = input("请输入学生专业：")
    print(f"学生专业：{major}")

if __name__ == "__main__":
    show_student() 