
def func(arr, max_=None):
    if(max_ is None):
        max_ = arr.pop()
        current =  arr.pop()
        if (current> max_):
            max_ = current
            if (arr):
                return func(arr, max_)
    return max_
list1=[1,2,3,4,2]
result = func(list1)
print(result)
