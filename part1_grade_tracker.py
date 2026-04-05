# =========================================================
# Student Grade Tracker
# Assignment Part 1 - Python Basics & Control Flow
# =========================================================

# -----------------------------
# Task 1 — Data Parsing & Profile Cleaning
# -----------------------------

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

print("\n--- Student Profile Cards ---\n")

for student in raw_students:

    # Clean the name (remove spaces and convert to title case)
    clean_name = student["name"].strip().title()

    # Convert roll number to integer
    roll = int(student["roll"])
    

    # Convert marks string to list of integers
    marks_split = student["marks_str"].split(",")
    marks = []

    for m in marks_split:
        marks.append(int(m.strip()))

    # Validate name (check each word contains only letters)
    valid_name = True
    for word in clean_name.split():
        if not word.isalpha():
            valid_name = False

    if valid_name:
        validation = "✓ Valid name"
    else:
        validation = "✗ Invalid name"

    # Print student profile
    print("================================")
    print(f"Student : {clean_name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print(validation)
    print("================================")

    # If roll number is 103 print uppercase and lowercase name
    if roll == 103:
        print("\nSpecial Output for Roll 103")
        print(clean_name.upper())
        print(clean_name.lower())
        print()

# -----------------------------
# Task 2 — Marks Analysis
# -----------------------------

print("\n--- Marks Analysis ---\n")

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

# Loop through subjects and assign grade
for i in range(len(subjects)):

    score = marks[i]

    # Grade logic
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "F"

    print(f"{subjects[i]} : {score} Grade {grade}")

# Total and average
total = sum(marks)
average = round(total / len(marks), 2)

print("\nTotal Marks:", total)
print("Average:", average)

# Highest and lowest subjects
highest = max(marks)
lowest = min(marks)

high_index = marks.index(highest)
low_index = marks.index(lowest)

print("Highest:", subjects[high_index], highest)
print("Lowest:", subjects[low_index], lowest)

# While loop to add subjects
print("\n--- Add New Subjects ---")

new_count = 0

while True:

    subject = input("Enter subject name (or 'done'): ")

    if subject.lower() == "done":
        break

    mark_input = input("Enter marks (0-100): ")

    if not mark_input.isdigit():
        print("Invalid marks. Please enter a number.")
        continue

    mark = int(mark_input)

    if mark < 0 or mark > 100:
        print("Marks must be between 0 and 100.")
        continue

    subjects.append(subject)
    marks.append(mark)
    new_count += 1

print("\nNew subjects added:", new_count)

new_average = round(sum(marks) / len(marks), 2)
print("Updated Average:", new_average)

# -----------------------------
# Task 3 — Class Performance Summary
# -----------------------------

print("\n--- Class Performance ---\n")

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print("Name              | Average | Status")
print("----------------------------------------")

pass_count = 0
fail_count = 0

topper_name = ""
topper_avg = 0

total_avg_sum = 0

for name, marks in class_data:

    avg = round(sum(marks) / len(marks), 2)
    total_avg_sum += avg

    if avg >= 60:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1

    if avg > topper_avg:
        topper_avg = avg
        topper_name = name

    print(f"{name:<18} | {avg:6} | {status}")

class_average = round(total_avg_sum / len(class_data), 2)

print("\nStudents Passed:", pass_count)
print("Students Failed:", fail_count)
print("Class Topper:", topper_name, topper_avg)
print("Class Average:", class_average)

# -----------------------------
# Task 4 — String Manipulation
# -----------------------------

print("\n--- Essay Processing ---\n")

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# Step 1: Strip whitespace
clean_essay = essay.strip()
print("Stripped Essay:\n", clean_essay)

# Step 2: Title case
print("\nTitle Case:\n", clean_essay.title())

# Step 3: Count python
count_python = clean_essay.count("python")
print("\n'python' count:", count_python)

# Step 4: Replace python
replaced = clean_essay.replace("python", "Python 🐍")
print("\nReplaced Text:\n", replaced)

# Step 5: Split sentences
sentences = clean_essay.split(". ")
print("\nSentence List:", sentences)

# Step 6: Print numbered sentences
print("\nNumbered Sentences:")

for i, sentence in enumerate(sentences, start=1):

    if not sentence.endswith("."):
        sentence += "."

    print(f"{i}. {sentence}")
