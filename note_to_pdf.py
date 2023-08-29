import os
import subprocess

def convert_note_to_pdf(directory):
    # Iterate over all items in the given directory
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # Check if the file has the .note extension
            if filename.endswith(".note"):
                # Derive the output filename
                output_pdf = os.path.join(root, filename.replace(".note", ".pdf"))
                # Create the command
                command = ["supernote-tool", "convert", "-t", "pdf", "-a", os.path.join(root, filename), output_pdf]
                # Run the command
                subprocess.run(command)

if __name__ == "__main__":
    # Converts all .note files in the current directory and its subdirectories
    convert_note_to_pdf(os.getcwd())
    print("Conversion completed!")