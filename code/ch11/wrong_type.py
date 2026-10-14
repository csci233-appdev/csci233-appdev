def main():
    # Pass a string to show_mammal_info
    not_a_mammal = 'I am a mammal'
    show_mammal_info(not_a_mammal)


# The show_mammal_info function accepts an object
# as an argument, and calls its show_species
# and make_sound methods.
def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()


# Call the main function.
if __name__ == '__main__':
    main()
