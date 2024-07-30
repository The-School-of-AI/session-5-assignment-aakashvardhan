"""WRITE PROPER ASSINGMENT DESCIPTION HERE AND DELETE THIS MESSAGE"""

import time
import math

def time_it(fn, *args, repetitions=1, **kwargs):
    """This is a genralized function to call any function
    user specified number of times and return the average
    time taken for calls"""

    # Repetition should be positive number
    if repetitions < 0:
        raise ValueError("Repetitions should be positive number")
    if not isinstance(repetitions, int):
        raise ValueError("Repetitions should be integer")
    if repetitions == 0:
        return 0
    if fn is None:
        raise ValueError("Error: Function is not provided")
    if not callable(fn):
        raise ValueError("Error: Function is not callable")
    if args is None:
        raise ValueError("Error: Arguments are not provided")
    if kwargs is None:
        raise ValueError("Error: Keyword arguments are not provided")

    # Calculate the time taken for the function to execute
    exec_lst = []

    for i in range(repetitions):
        start = time.time()
        fn(*args, **kwargs)
        end = time.time()
        exec_lst.append(end - start)

    return sum(exec_lst) / len(exec_lst)


def squared_power_list(number, *args, start=0, end=5, **kwargs):
    """Retruns list by raising number to power from start to end
    -> number**start to number**end. Default start is 0 and end is 5"""

    # Validations "if" block
    if not isinstance(number, int):
        raise TypeError("Only integer type arguments are allowed")
    if start < 0:
        raise ValueError("Value of start or end can't be negative")
    if end < 0:
        raise ValueError("Value of start or end can't be negative")
    if start > end:
        raise ValueError("Value of start should be less than end")
    if not isinstance(start, int):
        raise ValueError("Error: Start should be integer")
    if not isinstance(end, int):
        raise ValueError("Error: End should be integer")
    if number > 10:
        raise ValueError("Value of number should be less than 10")
    if len(args) > 0:
        raise TypeError("takes maximum 1 positional arguments")
    if len(kwargs) > 0:
        raise TypeError("maximum 2 keyword/named arguments")

    # Return the list of number to the power of numbers from start to end
    return [number**i for i in range(start, end)]


def polygon_area(length, *args, sides=3, **kwargs):
    """Retruns area of a regular polygon with number of sides between
    3 to 6 bith inclusive"""

    # Validations
    if not isinstance(length, int):
        raise ValueError("Error: Length should be integer")
    if sides < 3 or sides > 6:
        raise ValueError("Error: Sides should be between 3 to 6")
    if not isinstance(sides, int):
        raise ValueError("Error: Sides should be integer")
    if length <= 0:
        raise ValueError("Error: Length should be positive number")
    if len(args) > 0:
        raise TypeError("polygon_area function takes maximum 1 positional arguments, more provided")
    if len(kwargs) > 0:
        raise TypeError("polygon_area function take maximum 1 keyword/named arguments, more provided")

    
    if sides == 3:
        area = (math.sqrt(3) / 4) * length ** 2
    elif sides == 4:
        area = length ** 2
    elif sides == 5:
        area = (1 / 4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * length ** 2
    elif sides == 6:
        area = (3 * math.sqrt(3) / 2) * length ** 2

    return area


def temp_converter(temp, *args, temp_given_in="f", **kwargs):
    """Converts temprature from celsius 'c' to fahrenheit 'f' or
    fahrenheit to celsius"""

    # Validations
    if type(temp_given_in) != str:
        raise TypeError("Character string expected")
    if temp_given_in.lower() not in ['c', 'f']:
        raise ValueError("Only f or c is allowed")
    if type(temp) not in [int, float]:
        raise TypeError("Only integer or float type values are allowed")
    if temp_given_in.lower() == 'c' and temp < -273.15:
        raise ValueError("Temperature can't go below -273.15 celsius = 0 Kelvin")
    if temp_given_in.lower() == 'f' and temp < -459.67:
        raise ValueError("Temperature can't go below -459.67 fahrenheit = 0 Kelvin")
    if len(args) > 0:
        raise TypeError("temp_converter function takes maximum 1 positional arguments, more provided")
    if len(kwargs) > 0:
        raise TypeError("temp_converter function take maximum 1 keyword/named arguments, more provided")

    # Return the converted temprature
    if temp_given_in.lower() == 'c':
        return (temp * 9/5) + 32
    else:
        return (temp - 32) * 5/9


def speed_converter(speed, *args, dist="km", time="min", **kwargs):
    """Converts speed from kmph (provided by user as input) to different units
    dist can be km/m/ft/yrd time can be ms/s/min/hr/day"""

    # Validations
    if type(speed) not in [int, float]:
        raise TypeError("Speed can be int or float type only")
    if type(dist) != str:
        raise TypeError("Character string expected for distance unit")
    if type(time) != str:
        raise TypeError("Character string expected")
    
    if speed < 0:
        raise ValueError("Speed can't be negative")
    if speed > 300000:
        raise ValueError("Speed can't be greater than speed of light")
    
    if len(args) > 0:
        raise TypeError("speed_converter function takes maximum 1 positional arguments, more provided")
    if len(kwargs) > 0:
        raise TypeError("speed_converter function take maximum 2 keyword/named arguments, more provided")
    if dist.lower() not in ['km', 'm', 'ft', 'yrd']:
        raise ValueError("Incorrect unit of distance. Only km/m/ft/yrd allowed")
    if time.lower() not in ['ms', 's', 'min', 'hr', 'day']:
        raise ValueError("Incorrect unit of Time. Only ms/s/min/hr/day allowed")
    # Return the converted speed
    km_to_m = 1000
    km_to_ft = 3280.84
    km_to_yrd = 1093.61
    hr_to_ms = 3.6e+6
    hr_to_min = 60.0
    hr_to_sec = 3600.0
    hr_to_day = 24.0

    speed_ = speed
    if dist.lower() == 'km':
        speed_ = speed_
    elif dist.lower() == 'm':
        speed_ = speed_ * km_to_m
    elif dist.lower() == 'ft':
        speed_ = speed_ * km_to_ft
    elif dist.lower() == 'yrd':
        speed_ = speed_ * km_to_yrd
        
    if time.lower() == 'ms':
        speed_ = speed_ / hr_to_ms
    elif time.lower() == 's':
        speed_ = speed_ / hr_to_sec
    elif time.lower() == 'min':
        speed_ = speed_ / hr_to_min
    elif time.lower() == 'hr':
        speed_ = speed_
    elif time.lower() == 'day':
        speed_ = speed_ * hr_to_day
        
    return round(speed_)