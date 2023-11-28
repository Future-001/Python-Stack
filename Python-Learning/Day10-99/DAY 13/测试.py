def make_average():
    li = [1,2,3,4]
    def average(new_values):
        print(locals())
        return new_values
    return average
avg = make_average()
print(avg(11))
print(globals())
print(avg(12))
print(avg(13))

def make_average():
    li = [1,2,3,4]
    def average(new_values):
        print(locals())
        return new_values
    average(18)
    return 'nice'
print(make_average())
print(globals())