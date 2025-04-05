#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
School Timetable Generator

This program generates an optimal weekly timetable for a school based on 
classes, subjects, teachers, and period requirements.
"""

### DO NOT MODIFY THE CODE BELOW THIS LINE ###

# Define the input constraints
# Classes
classes = ["Class 6A", "Class 6B", "Class 7A", "Class 7B"]

# Subjects
subjects = ["Mathematics", "Science", "English", "Social Studies", "Computer Science", "Physical Education"]

# Weekly period requirements for each class and subject
# {class_name: {subject_name: number_of_periods_per_week}}
class_subject_periods = {
    "Class 6A": {"Mathematics": 6, "Science": 6, "English": 6, "Social Studies": 6, "Computer Science": 3, "Physical Education": 3},
    "Class 6B": {"Mathematics": 6, "Science": 6, "English": 6, "Social Studies": 6, "Computer Science": 3, "Physical Education": 3},
    "Class 7A": {"Mathematics": 6, "Science": 6, "English": 6, "Social Studies": 6, "Computer Science": 4, "Physical Education": 2},
    "Class 7B": {"Mathematics": 6, "Science": 6, "English": 6, "Social Studies": 6, "Computer Science": 4, "Physical Education": 2}
}

# Teachers and their teaching capabilities
# {teacher_name: [list_of_subjects_they_can_teach]}
teachers = {
    "Mr. Kumar": ["Mathematics"],
    "Mrs. Sharma": ["Mathematics"],
    "Ms. Gupta": ["Science"],
    "Mr. Singh": ["Science", "Social Studies"],
    "Mrs. Patel": ["English"],
    "Mr. Joshi": ["English", "Social Studies"],
    "Mr. Malhotra": ["Computer Science"],
    "Mr. Chauhan": ["Physical Education"]
}

# School timing configuration
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
periods_per_day = 6

### DO NOT MODIFY THE CODE ABOVE THIS LINE ###

def generate_timetable():
    """
    Generate a weekly timetable for the school based on the given constraints.
    
    Returns:
        dict: A data structure representing the complete timetable
               Format: {day: {period: {class: (subject, teacher)}}}
    """
    # Initialize an empty timetable
    timetable = {day: {period: {} for period in range(1, periods_per_day + 1)} for day in days_of_week}
    
    remaining_periods = {class_name: class_subject_periods[class_name].copy() 
                        for class_name in classes}
    
    subject_teachers = {}
    for subject in subjects:
        subject_teachers[subject] = [teacher for teacher, teachable in teachers.items() 
                                   if subject in teachable]
    
    def is_teacher_available(teacher, day, period, current_assignments):
        return not any(teacher == class_assignment[1] 
                      for class_assignment in current_assignments.values())
    
    def is_class_available(class_name, day, period):
        return class_name not in timetable[day][period]
    
    for day in days_of_week:
        for period in range(1, periods_per_day + 1):
            for class_name in classes:
                if not is_class_available(class_name, day, period):
                    continue
                
                for subject, periods_needed in remaining_periods[class_name].items():
                    if periods_needed <= 0:
                        continue
                    
                    for teacher in subject_teachers[subject]:
                        if is_teacher_available(teacher, day, period, timetable[day][period]):
                            timetable[day][period][class_name] = (subject, teacher)
                            remaining_periods[class_name][subject] -= 1
                            break
                    
                    if class_name in timetable[day][period]:
                        break
    
    return timetable


def display_timetable(timetable):
    """
    Display the generated timetable in a readable format.
    
    Args:
        timetable (dict): The generated timetable
    """
    for class_name in classes:
        print(f"\nTimetable for {class_name}:")
        print("-" * 80)
        print(f"{'Day':<12}" + "".join(f"Period {p:<12}" for p in range(1, periods_per_day + 1)))
        print("-" * 80)
        
        for day in days_of_week:
            row = [day.ljust(12)]
            for period in range(1, periods_per_day + 1):
                if class_name in timetable[day][period]:
                    subject, teacher = timetable[day][period][class_name]
                    cell = f"{subject}\n({teacher})"
                else:
                    cell = "Free"
                row.append(cell.ljust(12))
            print("".join(row))
        print("-" * 80)

    print("\nTeacher Schedules:")
    for teacher_name in teachers:
        print(f"\n{teacher_name}'s Schedule:")
        print("-" * 80)
        print(f"{'Day':<12}" + "".join(f"Period {p:<12}" for p in range(1, periods_per_day + 1)))
        print("-" * 80)
        
        for day in days_of_week:
            row = [day.ljust(12)]
            for period in range(1, periods_per_day + 1):
                cell = "Free"
                for class_name, (subject, teacher) in timetable[day][period].items():
                    if teacher == teacher_name:
                        cell = f"{subject}\n({class_name})"
                        break
                row.append(cell.ljust(12))
            print("".join(row))
        print("-" * 80)


def validate_timetable(timetable):
    """
    Validate that the generated timetable meets all constraints.
    
    Args:
        timetable (dict): The generated timetable
        
    Returns:
        bool: True if timetable is valid, False otherwise
        str: Error message if timetable is invalid
    """
    actual_periods = {class_name: {subject: 0 for subject in subjects} 
                     for class_name in classes}
    
    for day in days_of_week:
        for period in range(1, periods_per_day + 1):
            teachers_this_period = set()
            
            for class_name, (subject, teacher) in timetable[day][period].items():
                actual_periods[class_name][subject] += 1
            
                if subject not in teachers[teacher]:
                    return False, f"Teacher {teacher} is not qualified to teach {subject}"
                
                if teacher in teachers_this_period:
                    return False, f"Teacher {teacher} is double-booked on {day}, period {period}"
                teachers_this_period.add(teacher)
    
    for class_name in classes:
        for subject, required_periods in class_subject_periods[class_name].items():
            actual = actual_periods[class_name][subject]
            if actual != required_periods:
                return False, f"{class_name} has {actual} periods of {subject}, but needs {required_periods}"
    
    return True, "Timetable is valid"


def main():
    """
    Main function to generate and display the timetable.
    """
    print("Generating school timetable...")
    
    # Generate the timetable
    timetable = generate_timetable()
    
    # Validate the timetable
    is_valid, message = validate_timetable(timetable)
    
    if is_valid:
        # Display the timetable
        display_timetable(timetable)
    else:
        print(f"Failed to generate valid timetable: {message}")


if __name__ == "__main__":
    main()
