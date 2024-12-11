calls = 0

def count_calls():
    global calls
    calls += 1


def string_info(str_info):
    count_calls()
    str_info = len(str_info), str_info.upper(), str_info.lower()
    return str_info


def is_contains(contains_str, contains_list):
    count_calls()
    if contains_str.lower() in [s.lower() for s in contains_list]:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
