def modify_file(input_filename, output_filename):
    """
    Reads a file, modifies its content, and writes it to a new file.

    Args:
        input_filename (str): The name of the file to read.
        output_filename (str): The name of the file to write.
    """
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
            modified_content = content.upper()  # Example modification: convert to uppercase

        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"Successfully modified '{input_filename}' and saved to '{output_filename}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Get filenames from the user
input_file = input("Enter the input filename: ")
output_file = input("Enter the output filename: ")

modify_file(input_file, output_file)
