# def test_sum():
#     assert sum([1, 2, 3]) == 6, "Should be 6"
#
#
# def test_sum_tuple():
#     assert sum((2, 2, 2)) == 6, "Should be 6"
#
#
# def test_input_text(expected_result, actual_result):
#     assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"
from _socket import if_nameindex


def substring(full_string, substring):
    return substring in full_string, f"expected \'{substring}\' to be substring of \'{full_string}\'"


print(substring('1', '2'))

if __name__ =='__main__':
    substring('Sey hello me', 'hello')
