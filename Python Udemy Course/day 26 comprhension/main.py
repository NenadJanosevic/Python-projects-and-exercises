# num = [1,2,3]
# new_numbers = [ n  for n in num]
# print(new_numbers)

# name = "Nenad"
# new_list = [letter for letter in name]
# print(new_list)

# new_range = [num * 2 for num in range(1,5)]
# print(new_range)

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# short_names = [name.upper() for name in names if len(name) > 5]
# print(short_names) 

# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(num) for num in list_of_strings]
# result = [num for num in numbers if num % 2 == 0]
# print(result)

# import random

# names = ["Alex", 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# student_scores = {student:random.randint(1,100) for student in names}
# print(student_scores)
# passed_students = {k:v for k,v in student_scores.items() if v > 60}
# print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words_list = sentence.split()
result = {word: len(word) for word in words_list}
# print(result)

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# weather_f = {k: v * 9/5 +32 for k,v in weather_c.items()}

# print(weather_f)