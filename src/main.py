""" main executable for project """

# Includes and Imports
from feature_practical_calvin import get_time
from feature_practical_amaan import helloWorld
from feature_practical_reza import evaluate_square

# Variables
num = 2
name = "Amaan"
timezone = +2

# Functions


if __name__ == '__main__':
    _, _, time_response = get_time(name, timezone)
    print(time_response)
    output = helloWorld(name)
    print(output)
    square = evaluate_square(num)
    print(square)