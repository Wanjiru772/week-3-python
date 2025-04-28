def read_and_modify_file(input_filename, output_filename):
    try:
        # Attempt to open the input file in read mode
        with open(input_filename, 'r') as infile:
            content = infile.read()  # Read the content of the file

        # Modify the content (example: converting text to uppercase)
        modified_content = content.upper()  # Modify as needed (e.g., convert to uppercase)

        # Write the modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File successfully read and modified. Modified content saved to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: There was an issue reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask the user for the input and output filenames
input_filename = input("Enter the input filename: ")
output_filename = input("Enter the output filename: ")

# Call the function to process the file
read_and_modify_file(input_filename, output_filename)
