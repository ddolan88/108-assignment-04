from unittest import mock
from flask import Flask

from about import me

import json

from data import mock_data


app = Flask('server')


@app.get("/")
def home():
    return "Hello from flask server"


@app.get("/test")
def test():
    return "This is just a simple test"

# get /about


@app.get("/about")
def about_me():
    return "My name is Derek"


########################################################
############ API ENDPOINTS = PRODUCTS ##################
########################################################

# get /api/version
# @app.get("/api/version")

@app.get("/api/version")
def version():
    return "1.0"

# create a get request /api/about  and return first name and last name


@app.get("/api/about")
def about_json():

    # return me["first"] + " " + me["last"]

    # return f"{me['first']} {me['last']}"

    return json.dumps(me)  # parse the dicionary into a json string


# get /api/products
# return mock_data as a json string

@app.get("/api/products")
def products_data():
    return json.dumps(mock_data)


@app.get("/api/products/<id>")
def get_products_by_id(id):
    for prod in mock_data:
        if str(prod["id"]) == id:
            return json.dumps(prod)
    return "404 NOT FOUND"

    # travel mock_data list
    # compare the id with id variable
    # if they match, return the product as a json string


## GET /api/categories
# return the list of categories
# 1- return ok
# 2- travel mock_data and print the category of every product
# 3- put the category in a list and at the end of the loop return the list as a json string


@app.get('/api/categories')
def get_categories():
    categories = []
    for product in mock_data:
        cat = product["category"]
        if not cat in categories:
            categories.append(cat)

    return json.dumps(categories)

    # GET /api/products_category/<category>
    # return the list of products whose category is the same

    # travel the list and get every prod
    # if prod -> category is equal to the category variable
    # add prod to the results list
    # outside the for loop, return the results list as a json string


@app.get('/api/products_category/<category>')
def get_prods_category(category):
    print("Your category is: ", category)
    results = []
    for prod in mock_data:
        if prod["category"].lower() == category.lower():
            results.append(prod)
    return json.dumps(results)

# Get /api/product_cheapest


@app.get('/api/product_cheapest')
def get_cheapest():
    for num in mock_data:
        if num < solution:
            solution = num


app.run(debug=True)
