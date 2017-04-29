import unittest

from parse import *

def test_zpicode():
    "Test zipcode function"
    assert(parse_zipcode('12345') == '12345')
    assert(parse_zipcode('1234') == False)
    assert(parse_zipcode('abcde') == False)
    # assert(parse_zipcode('1234') == True)

def test_phone_number():
    "Test phone number"
    assert(parse_phone_number('373 781 7380') == '373-781-7380')
    assert(parse_phone_number('018 154 6474') == '018-154-6474')
    assert(parse_phone_number('018 154 647') == False)
    assert(parse_phone_number('abc def ghi') == False)

def test_color():
    "Test color function"
    assert(parse_color('pink') == 'pink')
    assert(parse_color('pink1') == False)
    assert(parse_color('pi') == False)

def test_parse_words_array():
    "Test array of words"
    words = ['Booker T.', ' Washington', ' 87360', ' 373 781 7380', ' yellow']
    result_expected = {'first_name' : 'Booker T.', 'last_name': 'Washington',
    'zipcode': '87360', 'phone_number': '373-781-7380', 'color': 'yellow'}
    result = parse_words_array(words)
    assert(len(set(result.iteritems()) - set(result_expected.iteritems())) == 0)

    words = ['Chandler', ' Kerri', ' (623)-668-9293', ' pink', ' 123123121']
    result_expected = False
    result = parse_words_array(words)
    assert(result == result_expected)

    words = ['James Murphy', ' yellow', ' 83880', ' 018 154 6474']
    result_expected = {'color': 'yellow', 'phone_number': '018-154-6474',
    'first_name': 'James', 'last_name': 'Murphy', 'zipcode': '83880'}
    result = parse_words_array(words)
    assert(len(set(result.iteritems()) - set(result_expected.iteritems())) == 0)

def test_file_check():
    "test file function"
    file = file_check('test.in')
    check = "<open file 'test.in'" in str(file)
    assert(check == True)

def main():
    test_zpicode()
    test_phone_number()
    test_color()
    test_parse_words_array()
    test_file_check()

if __name__ == "__main__":
    main()
