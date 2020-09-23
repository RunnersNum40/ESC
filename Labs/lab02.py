def initialize():
    global current_value
    global stored_number
    global previous_value
    current_value = 0.0
    stored_number = 0.0
    previous_value = 0.0

def get_current_value():
    global current_value
    return current_value

def save():
    global previous_value
    global current_value
    previous_value = current_value

def display_current_value():
    global previous_value
    print("Current value:", current_value)

def add(to_add):
    save()
    global current_value
    current_value += to_add

def subtract(to_subtract):
    save()
    global current_value
    current_value -= to_subtract

def mult(multiplicand):
    save()
    global current_value
    current_value *= multiplicand

def divide(divisor):
    save()
    global current_value
    current_value /= divisor

def memory():
    save()
    global stored_number
    global current_value
    stored_number = current_value

def recall():
    save()
    global stored_number
    global current_value
    current_value = stored_number

def undo():
    global previous_value
    global current_value
    current_value, previous_value = previous_value, current_value

if __name__ == '__main__':
    initialize()
    print("Welcome to the calculator program.")
    display_current_value() # 0
    add(5) # 5
    subtract(2)
    display_current_value() # 3
    undo()
    display_current_value() # 5
    undo()
    display_current_value() # 3
    mult(10)
    display_current_value() # 30
    undo()
    undo()
    display_current_value() # 30
    undo()
    undo()
    undo()
    display_current_value() # 3