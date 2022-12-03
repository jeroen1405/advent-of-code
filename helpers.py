import os

def load_txt_file(n_day, suffix=None):
    filepath = load_file_path(n_day, suffix=None)
    with open(filepath, 'r') as f:
        content = f.read().splitlines()
    return content

def load_file_path(n_day, suffix=None):
    filename = 'day' + str(n_day) + '.txt'
    filepath = os.path.join('input', filename)
    return filepath