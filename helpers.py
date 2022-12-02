import os

def load_txt_file(n_day, suffix=None):
    filename = 'day' + str(n_day) + '.txt'
    filepath = os.path.join('input', filename)
    # with open(filepath, 'r') as f:
    #     content = f.readlines()
    # return content
    return filepath