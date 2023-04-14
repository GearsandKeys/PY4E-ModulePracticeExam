import fizz_buzz
import unittest.mock as mock

def test_numbers_output(capsys):
    with mock.patch('builtins.input', side_effect=["23", "47", '1']):
        fizz_buzz.fancy_fizzbuzz()
        
        captured = capsys.readouterr()
        outputs = captured.out

        formatted_output = outputs.replace('\n', '')
        formatted_output = formatted_output.replace('\r', '')

        expected_answers = '23FizzBuzz26Fizz2829FizzBuzz3132Fizz34BuzzFizz3738FizzBuzz41Fizz4344FizzBuzz46'

        assert formatted_output == expected_answers


def test_numbers_output_reverse(capsys):
    with mock.patch('builtins.input', side_effect=['25','14','-1']):
        fizz_buzz.fancy_fizzbuzz()
        
        captured = capsys.readouterr()
        outputs = captured.out

        formatted_output = outputs.replace('\n', '')
        formatted_output = formatted_output.replace('\r', '')

        expected_answers = 'BuzzFizz2322FizzBuzz19Fizz1716FizzBuzz'

        assert formatted_output == expected_answers
