import functions

print("""
----------------------------------------------------------
--------------Welcome to Brian's Color Mixer--------------
----------------------------------------------------------

***This script does not consider the volume of color mixed.
Thus, if you are mixing paints you should use equal volumes of paint.***\n""")

# This loop prompts the user if they want to mix additional sets of colors at the end of execution.
mix_colors = True
while mix_colors:

    # Function prompts user for number of colors they would like to mix. Also, validates the user input.
    number_of_colors = functions.data_entry_checker(input("How many colors would you like to mix? ")
                                                    , "Invalid Input: Please enter a whole number greater than 1. ")

    # Collects and stores user inputted colors as tuples in a dictionary.
    dict_of_colors = (functions.ask_for_color_rgbs(number_of_colors))

    # Uses the dictionary of colors to construct objects of class Color.
    list_of_color_objects = functions.color_object_creator(dict_of_colors)

    # Mixes the user colors and constructs a Color object.
    mixed_color = functions.color_mixer(list_of_color_objects)

    # Prints the mixed_color object's RGB using Class methods.
    print(f"\n***************************************\n"
          f"Your new color is R:{mixed_color.return_red_value()}, G:{mixed_color.return_green_value()}, "
          f"B:{mixed_color.return_blue_value()}\n***************************************\n")

    # End of while loop controling the run state of the script
    keep_mixing = input("Would you like to mix more colors? y/n\n").lower()
    if keep_mixing != 'y' and keep_mixing != "yes":
        mix_colors = False
