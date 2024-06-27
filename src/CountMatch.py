def count_matches(file1_content, file2_content):
    """
  This function counts the number of words that match between two files.

  Args:
      file1_content (str): The content of file1 as a string.
      file2_content (str): The content of another file as a string.

  Returns:
      int: The number of words that match between the two files.
  """

    # Split both files into words (optional: remove punctuation)
    file1_words = set(file1_content.split())
    file2_words = set(file2_content.split())

    # Count matches using intersection of sets
    return len(file1_words.intersection(file2_words))