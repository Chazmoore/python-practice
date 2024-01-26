# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician)

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to seeyour next trick, {magician.title()}.\n")

# print("Thank you everyone, that was a great magic show!")
# if this is indented then it will print under each item in the list.

# numercal list:

# for value in range(1,6):
#     print(value)

# numbers = list(range(1,6))
# print(numbers)

# even_numbers = list(range(2,11,2))
# print(even_numbers)

# squares = []
# for value in range(1,11):
#     square = value ** 2
#     squares.append(square)

# print(squares)

# squares = []
# for value in range(1,11):
#     squares.append(value**2)
    
# print(squares)

# digits = [1,2,3,4,5,6,7,8,9,0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))

squares = [value**2 for value in range(1,11)]
print(squares)