#Task 1
#Given Data 
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []
for students in raw_students:
# Cleaning Names 
    name = students["name"].strip().title()
# Convertion roll to int
    roll = int(students["roll"])
 #convertion of marks strings to list
    marks = list(map(int,
students["marks_str"].split(",")))
    
    cleaned_students.append({
        "name":name,
        "roll":roll,
        "marks":marks
    })

#Validating Names 
for students in cleaned_students:
    name = students["name"]

    valid = all(word.isalpha() for word in name.split())
    if valid:
        print(name, "✓ Valid name")
    else:
        print(name, "x Invalid name")

#for Profile Card
for student in cleaned_students:
    print("="*30)
    print(f"Student: {student['name']}")
    print(f"Roll No: {student['roll']}")
    print(f"Marks: {student['marks']}")
    print("="*30)

#finding the roll no 103
for student in cleaned_students:
    if student["roll"] == 103:
        name = student["name"]
        print(name.upper())
        print(name.lower())

#Task 2 
#Given Data
student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

#Grade Logic
for i in range(len(subjects)):
    mark = marks[i]

    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "F"
    
    print(subjects[i],"-",mark,"-",grade)

#finding of total, average, highest, lowest 
total = sum(marks)
average = round(total/len(marks),2)

print("Total:",total)
print("Average:", average)

#highest marks
max_mark = max(marks)
max_index = marks.index(max_mark)
print("Highest:", subjects[max_index],"-",max_mark)

#lowest marks 
min_mark = min(marks)
min_index = marks.index(min_mark)
print("Lowest:", subjects[min_index],"-",min_mark)

#Mark entry system
new_subjects = []
new_marks = []

while True:
    subject = input ("Enter subject (or 'done'):")
    if subject.lower() == "done":
        break
    mark_input = input("Enter Marks:")
    if not mark_input.isdigit():
        print("Invalid Marks! Try Again.")
        continue
    mark = int(mark_input)
    if mark < 0 or mark > 100:
        print("Marks must be between 0-100")
        continue
    new_subjects.append(subject)
    new_marks.append(mark)

print("New Subjects Added:",len (new_subjects))

#updated average 

all_marks = marks + new_marks
new_avg = sum(all_marks)/len(all_marks)

print("Updated average:", round(new_avg,2))

#Task 3
#class data 
class_data = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma", [55, 68, 49, 72, 61]),
    ("Priya Nair", [91, 85, 88, 94, 79]),
    ("Karan Mehta", [40, 55, 38, 62, 50]),
    ("Sneha Pillai", [75, 80, 70, 68, 85])
]

total_avg = 0
pass_count = 0
fail_count = 0
topper_name = ""
topper_avg = 0

print("Name              | Average | Status")
print("--------------------------------------")

for name, marks in class_data:
    avg = round(sum(marks) / len(marks), 2)
    total_avg += avg

    if avg >= 60:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1

# Find topper
    if avg > topper_avg:
        topper_avg = avg
        topper_name = name

    print(f"{name:<18} | {avg:<7} | {status}")

# Class average
class_avg = round(total_avg / len(class_data), 2)

print("\nSummary:")
print(f"Passed: {pass_count}")
print(f"Failed: {fail_count}")
print(f"Topper: {topper_name} ({topper_avg})")
print(f"Class Average: {class_avg}")

#Task 4
essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

#Step 1: Strip spaces 
clean_essay = essay.strip()
print("Step 1:", clean_essay)

#Step 2: Title case
print("Step 2:", clean_essay.title())

#Step 3: Count "pythom"
count = clean_essay.count("python")
print("Step 3 : Count of 'Python' =", count)

#Step 4: Replace 'Python'
replace = clean_essay.replace("python","Python🐍")
print("Step 4:", replace )

#Step 5: Split into Sentences 
sentences = clean_essay.split(".")
print("Step 5:", sentences)

#Step 6: printing of numbereed sentences
print("Step 6:")
for i, sentence in enumerate(sentences,1):
    if not sentence.endswith("."):
        sentence += "."
    print(f"{i}. {sentence}")
    