import os

# Get the current working directory
current_directory = os.getcwd()
print(f"Contents of: {current_directory}\n")

# List all files and directories
for item in os.listdir(current_directory):
    full_path = os.path.join(current_directory, item)
    if os.path.isdir(full_path):
        print(f"[DIR]  {item}")
    else:
        print(f"[FILE] {item}")
