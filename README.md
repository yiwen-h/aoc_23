# Advent of code Python template

Python package template demonstrating TDD in Python package format for Advent of Code

## Getting set up

1. Please clone this repo or fork it to your own github account.
2. Install `pytest` with your chosen python package manager.

## How to use this template

### Set up the test

1. Put the test data as a .txt file in the `test_data` folder.
2. Create a `tests/test_day_{day}.py` file and write your test.
3. Create a `day_{day}.py` file and write your function.
4. Run your test by running `pytest tests` in your terminal. It is normal and ok to fail the test at first!

### Work on your solution

5. Work on improving your function and run your test till your functon works.
6. Once it passes the test, create your real data file in the `real_data` folder. Copy and paste your data from the aoc website.
7. Run your function with the full data by uncommenting the lines.
8. Put your answer into the AOC website - hopefully you've got your star! ⭐


## (optional) Fancy API way of getting the real data 

1. Get your Session cookie from the advent of code website! [instructions here](https://mmhaskell.com/blog/2023/1/30/advent-of-code-fetching-puzzle-input-using-the-api)
2. Rename the .envEXAMPLE file to .env
3. Replace the `cookiegoeshere` text from the .env file with your Session cookie! 
4. Now, you should be able to pull the input data file directly from the AOC website without needing to copy and paste it into a .txt file.

## Other optional stretch goals

Implement Continuous Integration using github actions so that your tests automatically run when you push to main!