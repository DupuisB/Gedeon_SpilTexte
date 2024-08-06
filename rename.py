import os

directory = 'data/raw'

for filename in os.listdir(directory):
    if filename.endswith('.txt'):  # Change the file extension if needed
        new_filename = filename.replace(' ', '_')
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))