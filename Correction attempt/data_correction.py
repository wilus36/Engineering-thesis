from copy import deepcopy
from cmath import cos, sin, sqrt, tan
from pyexpat.errors import XML_ERROR_UNKNOWN_ENCODING
from matplotlib import pylab
import math
import logging

from numpy import arctan, ndarray

logging.getLogger().setLevel(logging.INFO)

ANGLE = 0.56
ANGLE_RADIANS = math.radians(ANGLE)
COORDINATE_ZERO = 2048

def correct(x_to_correct, y_to_correct, original_x_axis) -> tuple:
    x_points = deepcopy(x_to_correct)
    y_points = deepcopy(y_to_correct)

    all_points = [(x_points[i], y_points[i]) for i in range(x_points.size)]
    all_points_after_correction = perform_correction(all_points, original_x_axis)

    corrected_x = [point[0] for point in all_points_after_correction]
    corrected_y = [point[1] for point in all_points_after_correction]

    return (corrected_x, corrected_y)

def perform_correction(points: list[tuple], original_x_axis) -> None:
    corrected_points = []
    for idx, point in enumerate(points):
        x = point[0]
        y = point[1]
        x_new = 0
        y_new = 0

        # if y > COORDINATE_ZERO and y > original_x_axis[idx]:
            # x_new = x/cos(ANGLE_RADIANS) + (y-x*tan(ANGLE_RADIANS))*sin(ANGLE_RADIANS)
            # y_new = y - x*tan(ANGLE_RADIANS)
        # elif y < COORDINATE_ZERO and y > original_x_axis[idx]:
            # x_new = sqrt(x*x + y*y) * cos(ANGLE_RADIANS - arctan(y/x)) 
            # y_new = sqrt(x*x + y*y) * sin(ANGLE_RADIANS - arctan(y/x))
        # elif y < COORDINATE_ZERO and y < original_x_axis[idx]:
        x_new = sqrt(x*x + y*y) * cos(ANGLE_RADIANS + arctan(y/x)) 
        y_new = sqrt(x*x + y*y) * sin(ANGLE_RADIANS + arctan(y/x))
        # elif y == original_x_axis[idx]:
        #     x_new = x * cos(ANGLE_RADIANS)
        #     y_new = x * sin(ANGLE_RADIANS)
        # elif y == COORDINATE_ZERO:
        #     x_new = x / cos(ANGLE_RADIANS)
        #     y_new = y
        # else:
        #     raise('No condition was evaluated to true')
        logging.info('Point:')
        logging.info(f'\tx: {x}, x_new: {x_new}')
        logging.info(f'\ty: {y}, y_new: {y_new}')
        
        corrected_points.append((x_new, y_new))
    return corrected_points
    

def display_plot(original: tuple, corrected: tuple, original_x_axis: ndarray):
    pylab.title('Original vs. Corrected')
    pylab.grid()
    # draw X axes
    reference_x_axis = [COORDINATE_ZERO for i in range(2000)]
    x_axis = pylab.arange(original_x_axis.size)*(4/original_x_axis.size)*1000
    pylab.plot(x_axis, original_x_axis, color='red', label='original x axis') 
    pylab.plot(x_axis, reference_x_axis, color='green', label='correct x axis')
    # draw plots
    for idx in range(2000):
        if original[0][idx] != corrected[0][idx]:
            logging.info('x of two points is different')
        if original[1][idx] != corrected[1][idx]:
            logging.info('y of two points is different')
    pylab.plot(original[0], original[1], color='blue', label='original')
    pylab.plot(corrected[0], corrected[1], color='orange', label='corrected')
    pylab.legend()
    pylab.show()

def main():
    FILENAME = 'X8-1-2'
    y_to_correct = pylab.loadtxt(f'{FILENAME}.txt')
    points_amount = y_to_correct.size
    x_to_correct = pylab.arange(points_amount)*(4/points_amount)*1000
    original_x_axis = (math.tan(math.radians(360) - math.radians(ANGLE))) * x_to_correct + COORDINATE_ZERO
    
    corrected = correct(x_to_correct, y_to_correct, original_x_axis)

    display_plot((x_to_correct, y_to_correct), corrected, original_x_axis)

if __name__ == "__main__":
    main()
    


