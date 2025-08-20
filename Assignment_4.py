# Task 1: Read a File and Handle Errors

try:
    with open("sample.txt", "r") as file:
        print("File content:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")

# Task 2: Write and Append Data to a File

# Step 1: Write user input to a file
user_input = input("Enter some text to write into the file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

# Step 2: Append additional data
with open("output.txt", "a") as file:
    file.write("This line was appended.\n")

# Step 3: Read and display final content
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    print(file.read())
