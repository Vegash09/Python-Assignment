from src.floor_ceil_rint.util import process_array

arr_input = input("Enter array elements separated by space: ")

'''
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
'''

floor, ceil, rint = process_array(arr_input)

# Display results
print(floor)
print(ceil)
print(rint)
