from itertools import chain
listing = [1,2]
listing.append(3)
listing.append(4)

print(listing)

listing.extend([5,6,7])
listing.extend([8,9,10])
print(listing)

#or use itertools.chain
test1 = [1,2,3,4]
test2 = [5,3,4,6]
test3 = [7,8,9,3]

lst = list(chain(test1,test2,test3))
print(lst)
