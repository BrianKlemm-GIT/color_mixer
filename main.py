import functions

print("""
---------------------------------------------------------
---------Welcome to Brian's Mediocre Color Mixer---------
---------------------------------------------------------

***This script does not consider the volume of color mixed.
Thus, if you are mixing paints you should use equal volumes of paint.***\n""")

mix_colors = True
while mix_colors:  # This loop prompts the user if they want to mix additional sets of colors at the end of execution.

    number_of_colors = int(input("How many colors would you like to mix? "))
    dict_of_colors = (functions.ask_for_color_rgbs(number_of_colors))  # Collects and stores user
    # inputted colors as tuples in a dictionary.
    list_of_color_objects = functions.color_object_creator(dict_of_colors)  # Uses the dictionary of colors to construct
    #  objects of class color.
    mixed_color = functions.color_mixer(list_of_color_objects)  # Mixes the user colors and constructs a color object.
    print(f"\n***************************************\n"
          f"Your new color is R:{mixed_color.return_red_value()}, G:{mixed_color.return_green_value()}, "
          f"B:{mixed_color.return_blue_value()}\n***************************************\n")  # prints the mixed_color
    # object's RGB using Class methods.

    keep_mixing = input("Would you like to mix more colors? y/n\n").lower()
    if keep_mixing != 'y' and keep_mixing != "yes":
        mix_colors = False
