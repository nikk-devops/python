List = ["Hannu", "Akshu", 7, 42.5, True]  
print(List[0])  

List[0] = "Apple"
print(List[0])  #Here we have changed the first element of the list
print(List)  # Output: ['Apple', 'Akshu', 7, 42.5, True]
print(List[1:4])  # Output: ['Akshu', 7, 42.5]
print(List[-1])  # Output: True
print(List[:3])  # Output: ['Apple', 'Akshu', 7]
print(List[::2])  # Output: ['Apple', 7, True]  