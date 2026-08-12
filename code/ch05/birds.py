# This program demonstrates two functions that
# have local variables with the same name.
def main():
    birds = 1

    # Call the texas function.
    texas()
    print(f'main has {birds} birds.')

    # Call the california function.
    california()
    print(f'main still has {birds} birds.')


# Definition of the texas function. It creates
# a local variable named birds.
def texas():
    birds = 5000
    print(f'texas has {birds} birds.')


# Definition of the california function. It also
# creates a local variable named birds.
def california():
    birds = 8000
    print(f'california has {birds} birds.')


# Call the main function.
main()
