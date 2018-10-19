# tuple
p1 = (1, 2, 3)
p2 = (1, [2, 3])
# dict(key-value存储，key唯一)
d1 = {p1:p2} # no error
d2 = {p2:p1} # error

# set(key的集合，不存储value，key唯一)
d3 = {p1} # no error
d4 = {p2} # error