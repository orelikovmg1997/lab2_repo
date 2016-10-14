arr = [1, 5, 9, 8, 7]

def find_min(arr): #Нахождение минимума в массиве
    min = arr[0]
    for i in arr:
        if min > i:
            min = i
    return min

def find_avg(arr): #Нахождение среднего прифметического в массиве
    avg=0
    for i in arr:
        avg = avg + i
        avg = avg / len(arr)
        return avg

print(arr)
print("Mинимум в массиве:",(find_min(arr)))
print("Среднее арифметическое с массиве:",(find_avg(arr)))