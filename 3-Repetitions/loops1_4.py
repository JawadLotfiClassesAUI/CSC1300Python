# The use of the range function is controlled by the following 3 parameters:
# start gives the initial value of the counter. If not specified, it defaults to 0.
# stop gives the value at which the counter stops. This value is not included and the loop stops before it
# step gives the increment, or decrement of the counter. If not specified, it defaults to 1.
for count in range(5, -1, -1):
    print(count)