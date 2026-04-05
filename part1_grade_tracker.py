### --- Task 1: Data Parsing & Profile Cleaning --- ###

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

print("--- Task 1: Student Profiles ---")

for student in raw_students:
    # 1. Clean the name: strip whitespace and convert to Title Case
    clean_name = student["name"].strip().title()
    
    # 2. Convert roll to integer
    clean_roll = int(student["roll"])
    
    # 3. Convert marks_str to a list of integers
    # We split by ", " then use a list comprehension to convert each string to int
    clean_marks = [int(m) for m in student["marks_str"].split(", ")]
    
    # 4. Verify name validity (only alphabetic characters)
    # join then check isalpha handles multiple words
    is_valid = all(word.isalpha() for word in clean_name.split())
    valid_status = "✓ Valid name" if is_valid else "✗ Invalid name"
    
    # Store cleaned data
    cleaned_info = {"name": clean_name, "roll": clean_roll, "marks": clean_marks}
    cleaned_students.append(cleaned_info)
    
    # 5. Print Profile Card
    print(f"{valid_status}")
    print("================================")
    print(f"Student : {clean_name}")
    print(f"Roll No : {clean_roll}")
    print(f"Marks   : {clean_marks}")
    print("================================")

# 6. Specific operation for roll 103
for s in cleaned_students:
    if s["roll"] == 103:
        print(f"\nRoll 103 - Uppercase: {s['name'].upper()}")
        print(f"Roll 103 - Lowercase: {s['name'].lower()}\n")


### --- Task 2: Marks Analysis --- ###

print("\n--- Task 2: Marks Analysis ---")
student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

# 1. Print subject grades
for i in range(len(subjects)):
    m = marks[i]
    if m >= 90: grade = "A+"
    elif m >= 80: grade = "A"
    elif m >= 70: grade = "B"
    elif m >= 60: grade = "C"
    else: grade = "F"
    print(f"{subjects[i]}: {m} ({grade})")

# 2. Calculations
total_marks = sum(marks)
avg_marks = total_marks / len(marks)
high_idx = marks.index(max(marks))
low_idx = marks.index(min(marks))

print(f"\nTotal Marks: {total_marks}")
print(f"Average Marks: {avg_marks:.2f}")
print(f"Highest: {subjects[high_idx]} ({marks[high_idx]})")
print(f"Lowest: {subjects[low_idx]} ({marks[low_idx]})")

# 3. While Loop for User Input
print("\n--- New Subject Entry (Type 'done' to stop) ---")
new_subjects_count = 0
while True:
    sub_input = input("Enter subject name: ").strip()
    if sub_input.lower() == 'done':
        break
    
    marks_input = input(f"Enter marks for {sub_input}: ")
    
    # Validation logic
    if marks_input.isdigit():
        m_val = int(marks_input)
        if 0 <= m_val <= 100:
            subjects.append(sub_input)
            marks.append(m_val)
            new_subjects_count += 1
        else:
            print("Warning: Marks must be between 0 and 100.")
    else:
        print("Warning: Please enter a valid numeric value.")

updated_avg = sum(marks) / len(marks)
print(f"\nNew subjects added: {new_subjects_count}")
print(f"Updated overall average: {updated_avg:.2f}\n")


### --- Task 3: Class Performance Summary --- ###

print("--- Task 3: Class Report ---")
class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

pass_count = 0
fail_count = 0
student_averages = []
topper_name = ""
max_avg = -1

print(f"{'Name':<18} | {'Average':<7} | {'Status'}")
print("-" * 40)

for name, m_list in class_data:
    avg = sum(m_list) / len(m_list)
    student_averages.append(avg)
    status = "Pass" if avg >= 60 else "Fail"
    
    if status == "Pass": pass_count += 1
    else: fail_count += 1
    
    if avg > max_avg:
        max_avg = avg
        topper_name = name
        
    print(f"{name:<18} |  {avg:>5.2f}  | {status}")

class_avg = sum(student_averages) / len(student_averages)

print("-" * 40)
print(f"Passed: {pass_count}, Failed: {fail_count}")
print(f"Class Topper: {topper_name} ({max_avg:.2f})")
print(f"Class Average: {class_avg:.2f}\n")


### --- Task 4: String Manipulation Utility --- ###

print("--- Task 4: Essay Utility ---")
essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# 1. Strip
clean_essay = essay.strip()
print(f"1. Clean Essay: {clean_essay}")

# 2. Title Case
print(f"2. Title Case: {clean_essay.title()}")

# 3. Count Python (Case-insensitive)
# Note: Since the prompt says clean_essay is already lowercase from step 1
print(f"3. 'python' count: {clean_essay.count('python')}")

# 4. Replace
replaced_essay = clean_essay.replace("python", "Python 🐍")
print(f"4. Replaced: {replaced_essay}")

# 5. Split into sentences
sentences = clean_essay.split(". ")
print(f"5. Sentences List: {sentences}")

# 6. Numbered sentences
print("6. Numbered Sentences:")
for i, sentence in enumerate(sentences, 1):
    # Ensure it ends with a period
    final_sentence = sentence.strip()
    if not final_sentence.endswith("."):
        final_sentence += "."
    print(f"{i}. {final_sentence}")
