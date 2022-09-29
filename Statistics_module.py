import statistics

example_list = [4,6,2,4,7,6,8,9,9,4,5,6,7]

x = statistics.mean(example_list)
y = statistics.median(example_list)
z = statistics.stdev(example_list)
l = statistics.variance(example_list)

print(x,' ',y,' ',z,' ',l)
