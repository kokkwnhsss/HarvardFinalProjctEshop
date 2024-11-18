import sqlite3

import flask
from flask import Flask, render_template, request

# import requests

app = Flask(__name__, static_folder='static')


# bootstrap=Bootstrap(app)
@app.route('/')
def harvard_homepage():
    # Connect to the products database
    conn = sqlite3.connect('products1.db')

    # Retrieve all products from the database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products1")

    pinakas = cursor.fetchall()
    # print(pinakas)
    # Close the database connection
    conn.close()

    return render_template('HARVARD HTML.html', products=pinakas)


@app.route('/theo.html', methods=['POST'])
def harvard_homepage1():
    row_data = request.form['row_data']

    # Connect to the products database
    conn = sqlite3.connect('products1.db')

    # Retrieve all products from the database
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products1 where [Product Code]=" + row_data)

    rows = cursor.fetchall()

    # Close the database connection
    conn.close()

    return render_template('theo.html', products=rows)


@app.route('/BAG.html', methods=['GET', 'POST'])
def harvard_homepage15():
    # product_description = request.form['Product Description']
    product_code = request.form['row_data']
    # image = request.form['Image']
    # price = request.form['Price']
    # Connect to the products database
    conn = sqlite3.connect('products1.db')

    # Retrieve all products from the database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products1 where [Product Code]=" + product_code)

    rows = cursor.fetchall()

    product_description = rows[0][1]
    image = rows[0][2]
    price = rows[0][3]
    # VALUES(?, ?, ?)", (var1, var2, var3))
    sql = "INSERT INTO products1 VALUES (?,?,?,?,?)"
    # val = row_data

    cursor.execute(sql, (product_code, product_description, image, price,''))

    # Close the database connection
    conn.close()

    return render_template('BAG.html', products=rows)

@app.route('/payment1.html', methods=['GET', 'POST'])
def harvard_homepage25():
    return render_template('payment1.html')


@app.route('/payment15.html', methods=['POST'])
def harvard_homepage16():
    full_name = request.form['full name']
    email = request.form['Email']
    adress = request.form['adress']
    city = request.form['city']
    state = request.form['state']
    zip_code = request.form['zip code']
    card_Name = request.form['Card Name']
    card_Number = request.form['Card Number']
    card_expire_month = request.form['Card expire Month']

    # Connect to the products database
    conn = sqlite3.connect('products1.db')

    # Retrieve all products from the database
    cursor = conn.cursor()
    # cursor.execute(
    #     "SELECT * FROM paymentdata where " + row_data)

    rows = cursor.fetchall()

    sql = "INSERT INTO PAYMENTDATA(full_name, email, adress, city, state, zip_code, card_Name, card_Number, card_expire_month) VALUES (?,?,?,?,?,?,?,?,?)"
    # val = row_data
    # '{full name}', '{Email}', '{adress}', '{city}', '{state}', '{zip }', '{Card Name}', '{Card Number}', '{Card expire Month}'
    cursor.execute(sql, (full_name, email, adress, city, state, zip_code, card_Name, card_Number, card_expire_month))

    # Close the database connection
    conn.close()

    return render_template('payment1.html', products=rows)


# @app.route('/2nd page.html')
# def harvard_homepage2():
#     return render_template('/2nd page.html')
#
#
@app.route('/login.html', methods=['GET', 'POST'])
def harvard_homepage19():
    if request.method == 'GET':
        email = request.args.get('email')
        password = request.args.get('password')

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

    # Connect to the products database
    conn = sqlite3.connect('products1.db')

    # Retrieve all products from the database
    cursor = conn.cursor()
    # cursor.execute(
    #     "SELECT * FROM signinfo where " + row_data)

    rows = cursor.fetchall()

    sql = "INSERT INTO signinfo VALUES (?,?)"
    # val = row_data
    # '{password}', '{Email}'
    cursor.execute(sql, (email,password))

    # Close the database connection
    conn.close()

    return render_template('login.html')


@app.route('/SignIn.html',methods=['GET', 'POST'])
def harvard_homepage3():
    return render_template('SignIn.html')


# @app.route('/BAG.html')
# def harvard_homepage4():
#     return render_template('/BAG.html')


@app.route('/SignInupdate.html')
def harvard_homepage5():
    Email = request.form['Email']
    password = request.form['password']
    Repeat_password = request.form['Repeat password']

    conn = sqlite3.connect('SignIn.db')

    # Retrieve all products from the database
    cursor = conn.cursor()
    # cursor.execute(
    #     "SELECT * FROM paymentdata where " + row_data)

    rows = cursor.fetchall()

    sql = "INSERT INTO PAYMENTDATA(PAYMENTDATA) VALUES (?,?,?,?)"
    # val = row_data
    # '{full name}', '{Email}', '{adress}', '{city}', '{state}', '{zip }', '{Card Name}', '{Card Number}', '{Card expire Month}'
    cursor.execute(sql, (password, email, Repeat_password))

    # Close the database connection
    conn.close()
    harvard_homepage()


@app.route('/Dumbels.html')
def harvard_homepage20():
    # Connect to the products database
    conn = sqlite3.connect('products1.db')

    # Retrieve all products from the database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products1 where [Product Description]='Dumbels'")

    pinakas = cursor.fetchall()
    # print(pinakas)
    # Close the database connection
    conn.close()

    return render_template('theo.html', products=pinakas)


# return render_template('/H.html')

@app.route('/BenchPress.html')
def harvard_homepage30():
    # Connect to the products database
    conn = sqlite3.connect('products1.db')

    # Retrieve all products from the database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products1 where [Product Description]='Bench Press'")

    pinakas = cursor.fetchall()
    # print(pinakas)
    # Close the database connection
    conn.close()

    return render_template('2nd page.html', products=pinakas)


if __name__ == '__main__':
    app.run(debug=True)
