import classes
# "Invalid Input: Please input a number between 0 and 255. "


# Verifies the user has entered a valid RGB color value
def data_entry_checker(color_value, warning_text):
    invalid_user_input = True
    while invalid_user_input:
        try:
            user_input = int(color_value)
            if user_input >= 0 and user_input <= 255:
                return user_input
            else:
                color_value = input(warning_text)
        except ValueError:
            color_value = input(warning_text)


# Prompts the user to enter the RGB values of their colors and adds the entries into a dictionary.
def ask_for_color_rgbs(number_of_colors):
    dict_of_colors = {}
    warning_text = "Invalid Input: Please input a number between 0 and 255. "
    for i in range(0, number_of_colors):
        print("\nRGB values are denoted between 0 and 255.\n")
        red_value = data_entry_checker(input(f"What is the value of red in the color number {i+1}? ")
                                       , warning_text)
        green_value = data_entry_checker(input(f"What is the value of green in the color number {i+1}? ")
                                         , warning_text)
        blue_value = data_entry_checker(input(f"What is the value of blue in the color number {i+1}? ")
                                        , warning_text)

        dict_of_colors[f"color_{i+1}"] = (red_value, green_value, blue_value)

    return dict_of_colors


# Constructs objects of class Color out of all the dictionary elements.
def color_object_creator(dict_of_colors):
    list_of_color_objects = []
    for i in dict_of_colors:
        color_inputted = classes.Color(dict_of_colors[i][0], dict_of_colors[i][1], dict_of_colors[i][2])
        list_of_color_objects.append(color_inputted)

    return list_of_color_objects


# Mixes the given colors and returns a Color object using a simple average.
def color_mixer(list_of_color_objects):
    reds = 0
    greens = 0
    blues = 0
    counter = 0
    for color in list_of_color_objects:
        reds += color.return_red_value()
        greens += color.return_green_value()
        blues += color.return_blue_value()
        counter += 1

    new_red = round(reds / counter)
    new_green = round(greens / counter)
    new_blue = round(blues / counter)

    mixed_color = classes.Color(new_red, new_green, new_blue)

    return mixed_color
