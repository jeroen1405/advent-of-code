import helpers
import pandas as pd

def determine_outcome_game(opponent, own):
    if own == opponent:
        return 3
    if own == 'r':
        if opponent == 'p':
            return 0
        else:
            return 6
    elif own == 'p':
        if opponent == 's':
            return 0
        else:
            return 6
    elif own == 's':
        if opponent == 'r':
            return 0
        else:
            return 6

filepath = helpers.load_txt_file(2)
df = pd.read_csv(filepath, delimiter=' ', names=['opponent_move', 'suggested_move'])
# df = pd.DataFrame([['A', 'Y'], ['B', 'X'], ['C', 'Z']], columns=['opponent_move', 'suggested_move'])
mapper = {
    'A': 'r',
    'B': 'p',
    'C': 's',
    'X': 'r',
    'Y': 'p',
    'Z': 's',
}

selected_scores = {
    'r': 1,
    'p': 2,
    's': 3,


}
df['opponent_move'] = df['opponent_move'].map(mapper)
df['suggested_move'] = df['suggested_move'].map(mapper)
df['outcome'] = df.apply(lambda row: determine_outcome_game(row['opponent_move'], row['suggested_move']), axis=1)
df['selected_score'] = df['suggested_move'].map(selected_scores)
df['result'] = df['outcome'] + df['selected_score']
print(df['result'].sum())

def pick_move(opponent, suggested):
    if suggested == 's': # win
        if opponent == 'r':
            return 'p'
        elif opponent == 's':
            return 'r'
        else:
            return 's'
    if suggested == 'p': # draw
        return opponent
    if suggested == 'r': # lose
        if opponent == 'r':
            return 's'
        elif opponent == 's':
            return 'p'
        else:
            return 'r'

outcome_mapper = {
    'r': 0,
    'p': 3,
    's': 6
}

df['move_pt2'] = df.apply(lambda row: pick_move(row['opponent_move'], row['suggested_move']), axis=1)
df['selected_score_pt2'] = df['move_pt2'].map(selected_scores)
df['outcome_pt2'] = df['suggested_move'].map(outcome_mapper)
df['result2'] = df['selected_score_pt2'] + df['outcome_pt2']
print(df['result2'].sum())
print(df)