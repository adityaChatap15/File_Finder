import os

from ReadFile import read_file
from CountMatch import count_matches


def find_top_matches(file1_path, folder_path, num_top_files=5):
  """
  This function finds the top 'num_top_files' with the most words matching file1 in a folder.

  Args:
      file1_path (str): The path to file1.
      folder_path (str): The path to the folder containing other files.
      num_top_files (int, optional): The number of top matching files to find (default: 5).

  Returns:
      list: A list containing paths of the top 'num_top_files' matching files.
  """

  file1_content = read_file(file1_path)
  match_counts = {}  # Dictionary to store file paths and match counts

  # Get all file paths within the folder
  for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Check if readable file format (txt, pdf, docx)
    if filename.endswith(".txt") or filename.endswith(
            ".pdf") or filename.endswith(".docx"):
      file_content = read_file(file_path)
      match_count = count_matches(file1_content,
                                  file_content)
      match_counts[file_path] = match_count

  # Sort the dictionary by match count (descending order)
  sorted_matches = dict(sorted(match_counts.items(), key=lambda item: item[1], reverse=True))

  # Extract top 'num_top_files' paths
  top_files = list(sorted_matches.keys())[:num_top_files]

  return top_files