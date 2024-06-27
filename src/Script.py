import os

from FindMatch import find_top_matches

def main():
  """
  Main script function that takes a reference text file and finds top matching files.
  """

  # Get user input for file paths
  reference_file_path = "textFile1.txt"
  folder_path = "C:/Users/apeks/Downloads/DataFiles"
  num_top_files = 5

  # Find top matching files
  top_matches = find_top_matches(reference_file_path, folder_path, num_top_files)

  # Print results (if any)
  if top_matches:
    print(f"The top {len(top_matches)} files with the most matched words from '{reference_file_path}' are:")
    for file in top_matches:
      print(f"- {file}")
  else:
    print(f"No files found with matching words in '{folder_path}'.")

# Run the main script
if __name__ == "__main__":
  main()