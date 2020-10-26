from unittest import TestCase


class Practice1Test(TestCase):
    def test_exchange_value(self):
        a, b = 1, 2
        print(f"a={a}, b={b}")
        a, b = b, a
        print(f"a={a}, b={b}")

    def test_for_loop(self):
        my_list = [i * 2 for i in range(10)]
        print(my_list)

    def test_single_line_expression(self):
        print('hello')
        print('world')

        x = 1
        if x == 1:
            print('hello, world')

        cond1 = x == 1
        cond2 = 1 == 1
        if cond1 and cond2:
            print('Great world.')

    def test_iterate_array_with_index(self):
        for i, item in enumerate(range(10)):
            print(f'{i}-->{item}')

    def test_deserialize_array(self):
        a, *rest = [1, 2, 3]
        print(f'a={a}, rest={rest}')

        a, *middle, c = [1, 2, 3, 4]
        print(f'a={a}, middle={middle}, c={c}')

    def test_join_str(self):
        print(''.join(['a', 'b', 'c']))

    def test_true_condition_judgement(self):
        empty_str = ''
        empty_arr = []
        empty_dic = {}

        if not empty_str:
            print(f'empty_str is False.')

        if not empty_arr:
            print(f'empty_arr is False.')

        if not empty_dic:
            print(f'empty_dic is False.')
