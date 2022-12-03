import os

INPUT_FOLDER = 'input'

def handle_input_file(filepath):
    not_renamed_path = os.path.join(INPUT_FOLDER, 'input.txt')
    download_path = r'C:\Users\jeroenvanrijn\Downloads\input.txt'
    if os.path.exists(not_renamed_path):
        os.rename(not_renamed_path, filepath)
    elif os.path.exists(download_path):
        # for the truly lazy days
        os.rename(download_path, filepath)
    else:
        raise OSError('Cannot find input file')

def load_txt_file(n_day, suffix=None):
    filepath = load_file_path(n_day, suffix=None)
    if not os.path.exists(filepath):
        # I probably just downloaded input.txt
        # and forgot to rename / put in the right folder
        handle_input_file(filepath)
    with open(filepath, 'r') as f:
        content = f.read().splitlines()
    return content

def load_file_path(n_day, suffix=None):
    filename = 'day' + str(n_day) + '.txt'
    filepath = os.path.join(INPUT_FOLDER, filename)
    return filepath