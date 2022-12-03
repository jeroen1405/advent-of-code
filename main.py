import helpers
DAY = 3
testing = False
day_module = __import__('day' + str(DAY))
input_content = helpers.load_txt_file(DAY)

if testing:
    # Sample data #
    input_content = [
        'vJrwpWtwJgWrhcsFMMfFFhFp',
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
        'PmmdzqPrVvPwwTWBwg',
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
        'ttgJtRGJQctTZtZT',
        'CrZsJsPPZsGzwwsLwLmpwMDw',
    ]
    # Sample data #

    print(input_content)

answer_pt1 = day_module.pt1(input_content)
print('Answer part 1: ', answer_pt1)
print('###########')

answer_pt2 = day_module.pt2(input_content)
print('Answer part 2: ', answer_pt2)


