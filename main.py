import os

# Root directory containing all the folders to be renamed
root_dir = 'PATH\TO\FILES'

# Iterate over all the folder names in the root directory
for dir_name in os.listdir(root_dir):

    # Checks if returned path name refers to a directory
    if os.path.isdir(os.path.join(root_dir, dir_name)):

        # Split the folder name into parts separated by dashes (list)
        parts = dir_name.split('-')
        
        # Get the last part of the folder name (item level ref no)
        last_part = parts[-1]

        # Check if the last part is a zero-padded number with three digits
        if last_part.isdigit() and last_part.zfill(3) == last_part:

            # Convert the zero-padded number to an integer and remove the padding
            parts[-1] = str(int(last_part))

            # Join the parts back together to form the new folder name
            new_dir_name = '-'.join(parts)

            # Construct the old and new paths for the folder
            old_path = os.path.join(root_dir, dir_name)
            new_path = os.path.join(root_dir, new_dir_name)

            # Rename the folder
            os.rename(old_path, new_path)
