from flask import Flask, render_template, request, url_for, redirect, flash
import sqlite3

app = Flask(__name__)

pizzas_menu = [
    {"pizza": "Margarita", "description": "Composition: water, mozzarella, yeast, salt, flour, tomato sauce, green basil, tomato and olive oil.", "price": "250 UAH"},
    {"pizza": "Bavarian", "description": "Composition: tomatoes, mozzarella, tomato sauce, gherkins, hunting sausages, Bavarian sausages and onions.", "price": "200 UAH"},
    {"pizza": "Barbeque", "description": "Composition: olive oil, bacon, hunting sausages, smoked chicken breast, parsley, barbecue sauce.", "price": "150 UAH"},
    {"pizza": "4 Cheeses", "description": "Composition: Parmesan cheese, Mozzarella cheese, Gorgonzola cheese spicy or less spicy (dolce).", "price": "100 UAH"}
]

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/buy/")
def buy():
    return render_template("buy.html", menu=pizzas_menu)

@app.route("/buy_form/", methods=("GET", "POST"))
def buy_form():
    if request.method=="POST":
        pizza = request.form["pizza"]
        user_name = request.form["name_surname"]
        address = request.form["address"]
        ph_number = request.form["ph_number"]
        connection = create_db_connect()
        connection.execute("""INSERT INTO orders
                            (name_pizza, user_name, address, phone) VALUES (?, ?, ?, ?)""", (pizza, user_name, address, ph_number))
        connection.commit()
        connection.close()
        return redirect(url_for("main"))
    return render_template("forms.html")

def create_db_connect():
    connection = sqlite3.connect("oderman.db")
    connection.row_factory = sqlite3.Row
    return connection

app.run(port=23456, debug=True)