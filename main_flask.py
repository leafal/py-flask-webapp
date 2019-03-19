from flask import Flask, render_template, request
from horoscopeapi import zodiac_sign, handle_horoscope

app = Flask("MyApp")

def calculate_gen(year_parameter) :
    gen='Unknown'

    # add logic here to identify generation
    if year_parameter >= 1964 and year_parameter <=1978:
        gen='very OLD'
    if year_parameter > 1979 and year_parameter <= 1995:
         gen='Y - Millenials'
    if year_parameter > 1996 and year_parameter <= 2012:
        gen='Z'

    return gen

@app.route("/<visitor>")
def hello(visitor):
    m = "Welcome to my page:" + visitor.title()
    return render_template("index.html", message=m)


@app.route("/gen", methods=["POST"])
def showgeneration():
    form_data = request.form #Getting hold of a Form object
    year = form_data["dob"]
    day = form_data["day"]
    month = form_data["month"]

    gen = calculate_gen(int(year))

    return render_template("gen.html", generation=gen)

@app.route("/horoscope", methods=["POST"])
def get_horoscope():
    form_data = request.form #Getting hold of a Form object
    day = form_data["day"]
    month = form_data["month"]
    print month
    print day
    z_sign = zodiac_sign(int(month),int(day))
    raw_data = handle_horoscope(z_sign)

    return render_template("horoscope.html", data=raw_data)

app.run()
