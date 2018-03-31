d = [{"o1":1, "o2":2}, {"o3":3}]

# print([True if "o1" in x else False for x in d])


# print(1 if "o1" in d[0] else 0)

# dd = d[0]
# for i in dd:
#     print(i)

# lx = [((3,2,1,4,5,6), 0.1), ((2,2,2), 0.6), ((4,4,4), 0.3)]
#
# ll = [1, 2, 3, 4, 5]
#
# lt = {"o2":2, "o1":3, "o3":1 }
#
# # print(sorted(lx, key=lambda x: x[0], reverse=True))
# print(sorted(lt.items(), key=lambda x:x[1], reverse=True))

s1 = {('1111','2222'), ('3333', '4444')}
s2 = {('1111','2222'), ('3333', '2222')}

# print(s1 & s2)

# print(s1)
# s1.add(('1qqq', 'dada'))
# print(s1)


ss = set()
ss.add("aaa")
ss.add("bb")
print(ss)