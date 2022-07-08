
def start_test():
    print("-----list test-----")

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # read from the list
    print(nums[0])
    print(nums[1])

    # add elements to the list
    nums.append(10)

    # for loop
    for n in nums:
        print(n)

    # for loop from 0 to 20
    for number in range(0, 21):
        print(number)


def test1():
    print("test 1")

    prices = [123, 3, 23, 6475, 58, 89, 45, 34, 87, 34, -12, 23, 123, -23, -123, 0, 123, 0, -29, 10
              ]

# 1- print the numbers lower than 50 from test1 prices
# 2- display a count of numbers lower than 50
# 3- sum of all numbers
# 4- sum of all numbers greater than 0
# 5- count how many zeroes there is
    count = 0
    sum = 0
    zeros = 0
    sum_non_zero = 0

    for n in prices:
        sum += n

        if n > 0:
            sum_non_zero += n

        if n == 0:
            zeros += 1

        if n < 50:
            print(n)
            count += 1

    print(f"there are {count} prices lower than $50")


def test2():
    print("-------test2-------")

    users = [
        {
            "gender": "F",
            "name": "Louis",
            "color": "Green"
        },
        {
            "gender": "M",
            "name": "Manuel",
            "color": "Gray"
        },
        {
            "gender": "F",
            "name": "Rossy",
            "color": "Pink"
        },
        {
            "gender": "F",
            "name": "Renny",
            "color": "pink"
        },
        {
            "gender": "M",
            "name": "Roman",
            "color": "Purple"
        },
        {
            "gender": "m",
            "name": "John",
            "color": "Pink"
        },
        {
            "gender": "F",
            "name": "Susan",
            "color": "Black"
        },
    ]

    # 1- print all the names of users
    # 2- print how many users there are in the list
    # 3- print the name of users that like pink or PINK or PiNk

    print(len(users))

    for user in users:
        print(user["name"])

    print("Users that like pink")

    for user in users:
        if(user["color"].lower() == "pink"):
            print(user["name"])


def test3():
    print("-----test 3-----")

    prices = [123, 3, 23, 6475, 58, 89, 45, 34, 87, 34, -12, 23, 123, -23, -123, 0, 123, 0, -29, 10
              ]

# find the most expensive product price
# solution = prices[0]
# for price in prices
# if price is greater than your solution
# your solution = price
# outside the for loop print the result

    solution = prices[0]
    for num in prices:
        if num > solution:
            solution = num

    print("the greatest number is " + str(solution))


start_test()
test1()
test2()
test3()
