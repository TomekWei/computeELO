# Extract match_id values to use as filenames for future reference
from contourpy.util import data
import shutil

# Define the path for the zip file
zip_path = '/mnt/data/split_matches.zip'

# Create a zip file containing all the split match CSV files
shutil.make_archive(base_name=zip_path.replace('.zip', ''), format='zip', root_dir=output_dir)

zip_path

match_ids = data['match_id'].unique()

# Create a text file containing all unique match_ids
match_id_file_path = '/mnt/data/match_ids.txt'
with open(match_id_file_path, 'w') as file:
    for match_id in match_ids:
        # Format match_id to match the filenames created
        formatted_match_id = f"match_data_{match_id.replace('-', '_')}.csv\n"
        file.write(formatted_match_id)

match_id_file_path
