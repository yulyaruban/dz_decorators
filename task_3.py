from task_2 import logger

@logger('task_3.log')
def flat_generator(list_of_lists):
    lists = iter(list_of_lists)
    new = []
    for i in lists:
        new += i
    for el in new:
        if new == []:
            exit()
        yield (el)
    
list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
# def test_2():

#     list_of_lists_1 = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
#     ]

#     for flat_iterator_item, check_item in zip(
#             flat_generator(list_of_lists_1),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#     ):

#         assert flat_iterator_item == check_item

#     assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

#     assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    
    flat_generator(list_of_lists_1)