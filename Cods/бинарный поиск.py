def binary_search(value, arr):
    left = 0
    right = len(arr) - 1
#Цикл продолжается, пока диапазон поиска не пуст.
#Когда у нас left = right, то мы заходим в последний раз и выводен результат
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > value:
            right = mid - 1

        elif arr[mid] < value:
            left = mid + 1
        
        elif arr[mid] == value:
            return mid
        
    return None
    



array = [2,4,6,8,16,32,64,128]
item = int(input("Введите искомое число из массива [2,4,6,8,16,32,64,128]: "))
print(binary_search(item,array))

print(9//2)