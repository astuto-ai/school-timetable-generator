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


    
    # TODO: Implement the timetable generation algorithm
    # 1. Check if a valid timetable is possible with the given constraints
    

    # cheack total hrs for a class
    for each_class in class_subject_periods.keys():
        total_hr = 0 ;
        for  hr in class_subject_periods[each_class].keys():
            total_hr += class_subject_periods[each_class][hr]

        if(total_hr>30):
            print("can't design time table because hrs are  total hrs are more than 30")
            return timetable


    # check that  with give nuber of teachers is it possible to  design schedule without collision.
    # to check this  there is sufficient number of teacher  to cover  time that required by a subject in  all classes
    # like maths require 24 hrs per week for all classees ,   a teacher  can Do 30 hrs work per week , so a single teacher is enogh.
    # if hrs crosses the limit then  there should be more number of teachers per subject
    # IF FAIL TO DO SO THEN  DESIGN NOT POSSIBLE   

   
    # 2. Assign subjects and teachers to periods for each class

    
    # do with recursive call starting with diff subject  for each call 
        # case case: if no subject left in all classes call validate( ) and return accotrdingly
        # if hrs all slots for teacher is booked and for that subject still hrs are remaning then just return  flase;

    # start one  traversing day wise and start assigning subject in each class 
        # mean time keep track that total no of hrs do not cross  per subject
        # also there should only one class at that particular hr for a teacher keep in account
        # if fail to above 2 steps then move  to the next subject



    # to avoid collision--
    # make a 2d array  for each teacher  of boolean type and mark true or false for  there particular slot  . noofdays*hrs_perday

    # after all call processed  call   isvlaid fn and  if passes then just return

    # 3. Ensure all constraints are satisfied
    
    return timetable


def display_timetable(timetable):
    """
    Display the generated timetable in a readable format.
    
    Args:
        timetable (dict): The generated timetable
    """
    # TODO: Implement timetable display logic


    
    # Display the timetable for each class traverse and display it takes nested loops
    # 

    for uc in class_subject_periods.keys():  # to make sure it will print all  classes
        for day in timetable.keys():        
            for period in timetable[day]:
                for classs in timetable[day][period].keys():
                    if(uc==classs):
                        print(timetable[day][period][uc])

    # Display the timetable for each teacher

    # to display it for teacher wise
    # traverse the time table dict with 3 nested loops  and in last step
    # instead of comparing with  class , compare with teacher name ( after comparing show necessary details for them)

    pass


def validate_timetable(timetable):
    """
    Validate that the generated timetable meets all constraints.
    
    Args:
        timetable (dict): The generated timetable
        
    Returns:
        bool: True if timetable is valid, False otherwise
        str: Error message if timetable is invalid
    """
    # TODO: Implement validation logic


    #Thoughts------
    
    # Check if all classes have their required number of periods for each subject 

    # to check traverse the dict and  keep count in dict for each subject number of classes  scheduled to varigy the  hrs per subject satisfy or not 
    # now valid with requirments 


    # Check if teachers are not double-booked

    # traverse through the dict and   make sure that on a particular hr  there should be only one class for that teacher (among all the classes)
    # if more than 1 return false



    # Check if teachers are only teaching subjects they can teach
    
    #  cross check with given teachers dict


    
    return False, "To be implemented"


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
