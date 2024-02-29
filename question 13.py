total_users = int(input("Enter the total number of users: "))
staff_users = int(input("Enter the number of staff users: "))
non_teaching_staff_users = staff_users // 3
student_users = total_users - staff_users - non_teaching_staff_users
print(f"Student users: {student_users}")
