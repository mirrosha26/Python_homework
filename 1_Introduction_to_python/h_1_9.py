'''
Функция возвращающее втрое по величине число в списке
'''

def postmax(nums):
    nums = sorted(nums)
    return (nums[-2])
'''
Тест
print(postmax([1,32,13,14,5,6,7,8,9]))
>> 14
'''
