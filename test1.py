

def run_test():
    print("Test 1 - dictionaries")

    me = {
        "first": "Derek",
        "last": "Dolan",
        "age": "33",
        "hobbies": [],
        "address": {
            "street": "whatever",
            "number": "123",
            "city": "wherever",
            "state": "CA",
            "zip": "12345",

        }
    }
    print(me)
    print(me["first"])
    print(me["first"] + " " + me["last"])

    # change values
    # me["age"] = me["age"] + 1
    me["age"] = 99

    # add new item to dictionaries
    me["favorite_color"] = "purple"
    print(me)

    # read if exist
    if "middle_name" in me:
        print(me["middle_name"])

    # print full address in a single line
    address = me["address"]
    print("--------address--------")
    print(address)
    print(type(address))

    print(
        f'{address["street"]} #{address["number"]} #{address["city"]} #{address["state"]} #{address["zip"]}')


run_test()
