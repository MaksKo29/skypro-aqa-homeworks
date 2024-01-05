results = []   
def my_function():
    return input()
 
for _ in range(11):
    result = my_function()
    results.append(result)

print(*results, sep='') 