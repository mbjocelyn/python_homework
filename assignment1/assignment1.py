# Write your code here.
#Task 1 - have to create a function named hello that returns out "hello!"
def hello():
    return("Hello!")

print(hello())

#Task 2 - write a greet function that takes one argument, a name, and returns hello, name!
def greet(name):
    return("Hello, " + name + "!")

print(greet("Jocelyn"))

#Task 3 
def calc(value1,value2,operation="multiply"):
    try: 
     if operation == "add":              # we're not using just = because that means were giving operation the value of "add", but we dont want that, when using == it says that when the operation is addition to add the numbers 
        return value1 + value2
     elif operation == "subtract":
        return value1 - value2
     elif operation == "multiply":
        return value1 * value2
     elif operation == "divide":
        return value1 / value2
     elif operation == "modulo": 
        return value1 % value2
     elif operation == "int_divide":
        return value1 // value2
     elif operation == "power":
        return value1 ** value2

    except ZeroDivisionError: 
        return "You can't divide by 0!"
    except TypeError: 
        return "You can't multiply those values!"
    
#Task 4 
def data_type_conversion(value, type):
    try: 
      if type == "int":
         return int(value)
      elif type == "float":
         return float(value)
      elif type == "str":
         return str(value)
      
    except ValueError: 
        return f"You can't convert {value} into a {type}."
    
#Task 5 
def grade(*args):
    try:
        average = sum(args) / len(args)

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

    except TypeError:
        return "Invalid data was provided."

#Task 6 
def repeat(string, count):
    result = ""

    for i in range(count):
        result += string

    return result

#Task 7 
def student_scores(type, **kwargs):
    if type == "best":
        best_student = ""
        best_score = 0

        for student, score in kwargs.items():
            if score > best_score:
                best_score = score
                best_student = student

        return best_student

    elif type == "mean":
        total = sum(kwargs.values())
        average = total / len(kwargs)

        return average

#Task 8
def titleize(string):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]

    words = string.split()

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            words[i] = word.capitalize()
        elif word.lower() in little_words:
            words[i] = word.lower()
        else:
            words[i] = word.capitalize()

    return " ".join(words)

#Task 9 
def hangman(secret, guess):
    result = ""

    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"

    return result

#Task 10 
def pig_latin(string):
    vowels = "aeiou"
    words = string.split()
    result = []

    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")

        else:
            i = 0

            while i < len(word):
                if word[i:i + 2] == "qu":
                    i += 2
                elif word[i] in vowels:
                    break
                else:
                    i += 1

            result.append(word[i:] + word[:i] + "ay")

    return " ".join(result)