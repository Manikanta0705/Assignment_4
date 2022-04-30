import itertools
x_list = [1,2,3,4,5,6]
y_list = [1,2,3,4,5,6]
cartesian_product = itertools.product(x_list, y_list)


cartesian_list = list(cartesian_product)


print(cartesian_list)
