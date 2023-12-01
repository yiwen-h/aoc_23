import requests
from dotenv import load_dotenv
import os

# checks if you are using the fancy cookie way of getting data
if os.path.isfile('.env'):
    load_dotenv()
    COOKIE = os.environ.get("SESSION")

def check_file_exists(day):
    # checks that the datafile exists
    filepath = os.path.join('real_data', f'{day}.txt')
    return os.path.isfile(filepath)

def get_data(day):
    # loads the real data from real_data folder
    if check_file_exists(day):
        print('loading existing file')
        with open(f'real_data/{day}.txt') as f:
            raw_data = f.read()
    else: 
        # does the fancy cookie method of getting data if .env file with SESSION cookie is available
        if os.path.isfile('.env'):
            print('getting file')
            response = requests.get(f'https://adventofcode.com/2023/day/{day}/input',
                                cookies={'session': COOKIE})
            raw_data = response.content.decode('UTF-8')
            with open(f'real_data/{day}.txt', 'w') as f:
                f.write(raw_data)
        else:
            print('data file not found')
    return raw_data

def get_test_data(day):
    # loads the test data
    with open(f'test_data/{day}.txt') as f:
        data = f.read()
    return data

if __name__ == '__main__':
    print(get_test_data(1))