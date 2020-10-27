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

    def test_get_value_from_dic(self):
        d = {'hello': 'world'}

        print(d.get('hello', 'default_value'))
        print(d.get('not exist key', 'default_value'))

    def test_filter_array(self):
        a = [3, 4, 5]
        b = [i for i in a if i > 4]
        print(b)

        b = list(filter(lambda x: x > 4, a))
        print(b)

    def test_map_array(self):
        a = [3, 4, 5]
        b = list(map(lambda i: i + 3, a))
        print(b)

    def test_read_file(self):
        with open('file.txt') as fp:
            for line in fp.readlines():
                print(line)

    def test_multiple_lines_format(self):
        long_string = 'For a long time I used to go to bed early. ' \
                      'Sometimes, when I had put out my candle, ' \
                      'my eyes would close so quickly that I had not even time to say “I’m going to sleep.”'
        print(long_string)

        long_string = (
            "For a long time I used to go to bed early. Sometimes, "
            "when I had put out my candle, my eyes would close so quickly "
            "that I had not even time to say “I’m going to sleep.”"
        )
        print(long_string)

    def test_make_complex(self):
        x, y = 1, 2
        print({'x': x, 'y': y})

    def test_placeholder(self):
        file_name = 'foobar.txt'
        basename, _, ext = file_name.rpartition('.')
        assert (f'basename={basename}, _={_}, ext={ext}' == 'basename=foobar, _=., ext=txt')

    def test_map_addition(self):
        def addition(n):
            return n + n

        numbers = (1, 2, 3, 4)
        result = map(addition, numbers)
        assert (list(result) == [2, 4, 6, 8])

    def test_map_lambda(self):
        numbers = (1, 2, 3, 4)
        result = map(lambda x: x + x, numbers)
        assert (list(result) == [2, 4, 6, 8])

    def test_map_add_two_array(self):
        numbers1 = [1, 2, 3]
        numbers2 = [4, 5, 6]

        result = map(lambda x, y: x + y, numbers1, numbers2)
        assert (list(result) == [5, 7, 9])
