import numpy

def process_array(arr_str):
    numpy.set_printoptions(sign=' ')
    A = numpy.array(arr_str.split(), float)
    return numpy.floor(A), numpy.ceil(A), numpy.rint(A)
