


def hex_to_c_array(hex_data, var_name):
    """
    hex_to_c_array -> a function to convert the TensorFlow Lite file into the C format so that it can be used on Arduino BLE 33 Sense

    ----------------------------------------------------------------------------------------------------------------------------------

    Inputs:

    hex_data -> basically our tf lite model

    var_name -> the name of our model

    ----------------------------------------------------------------------------------------------------------------------------------

    Outputs:

    c_str -> converted string in C format ready to be copied to the Arduino project.


    ----------------------------------------------------------------------------------------------------------------------------------
    
    """

    c_str = ""

    # Create a header guard
    c_str += "#ifndef " + var_name.upper() + "_H\n"
    c_str += "#define " + var_name.upper() + "_`H\n\n"

    # Add array length at top of file
    c_str += "\nunsigned int " + var_name + "_len = " + str(len(hex_data)) + ";\n"

    # Declare C variable
    c_str += "unsigned char " + var_name + "[] = {"
    hex_array = []
    for i, val in enumerate(hex_data):

        # Construct string from hex
        hex_str = format(val, "#04x")

        # Add formatting so each line stays within 80 characters
        if i + 1 < len(hex_data):
            hex_str += ","

        if (i + 1) % 12 == 0:
            hex_str += "\n "
        hex_array.append(hex_str)

    # Add closing brace
    c_str += "\n " + format(" ".join(hex_array)) + "\n}; \n\n"

    c_str += "#endif //" + var_name.upper() + "_H"

    return c_str

