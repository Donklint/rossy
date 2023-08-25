from userAttributes import addUsername

def classDetail():
    num_units = input('State number of units: ')
    num_students = input('How many students are expected: ')
    teach_name = input('Name of the lec:')
    lesson_dur = input('How long does one lesson take:')

    print(f"Hello {username} thank you for signing up with us. You'll having a total of {num_units} for the first "
          f"semester and {teach_name} will be taking through the sem!")