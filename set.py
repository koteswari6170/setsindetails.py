"""1.difference_update"""
# a={5,12,15,18,20}
# b={15,18,21,25}
# a.difference_update(b)
# b.difference_update(a)
# print(a)#{5,12,20}
# print(b)#{18,15,21,15}
# a.update(b)
# b.update(a)
# print(a)#{5, 12, 15, 18, 20, 21, 25}
# print(b)#{5, 12, 15, 18, 20, 21, 25}
"""2.copy"""
# a={1,2,3,4,5}
# a.copy()
# print(a)#{1,2,3,4,5}
"""3.symmetric_difference_update"""
# a={5,12,15,18,20}
# b={15,18,21,25}
# a.symmetric_difference_update(b)
# print(a)#{20, 5, 21, 25, 12}
# b.symmetric_difference_update(a)
# print(b)#{5, 12, 20, 21, 25}
"""4.intersection_update"""
# s={5,12,15,18,20}
# v={15,18,21,25}
# s.intersection_update(v)
# print(s)#{18,15}
# v.intersection_update(s)
# print(v)#{18,15}
"""5.intersection"""
# a={8,9,10,12,14}
# b={10,14,15}
# print(a.intersection(b))#{10,14}
# print(b.intersection(a))#{10,14}
"""6.remove"""
# a={8,9,10}
# a.remove(140)
# print(a)#KeyError:140
"""7.issuperset"""
# a={8,9,10,12,14}
# b={10,14,15,1}
# print(a.issuperset(b))#False
# print(b.issuperset(a))#False
# c={5,34,12,3}
# k={12,3}
# print(c.issuperset(k))#True
# print(k.issuperset(c))#False



