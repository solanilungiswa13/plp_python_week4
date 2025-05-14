def read_and_modify_file():
# Ask the user for the input file name and output file name
input_file_name = input("Please enter the name of the file to read (with extension): ")
output_file_name = input("Please enter the name of the file to write (with extension): ")

try:
# Attempt to open and read the input file
with open(input_file_name, 'r') as input_file:
content = input_file.read()
# Modify the content (e.g., convert to uppercase)
modified_content = content.upper() # This is an example modification

# Write the modified content to the output file
with open(output_file_name, 'w') as output_file:
output_file.write(modified_content)

print(f"Modified content has been written to {output_file_name}.")

except FileNotFoundError:
print(f"Error: The file '{input_file_name}' does not exist.")
except IOError:
print(f"Error: The file '{input_file_name}' could not be read.")
except Exception as e:
print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
read_and_modify_file()