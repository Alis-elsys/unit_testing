#from flask import Flask, render_template, request

#app = Flask(__name__, template_folder='C:/Users/HP/Documents/School/Практика/praktika/flask/src/templates')

def kelvin_to_fahrenheit(K):
    F = K * 1.8 - 459.67
    return F

def kelvin_to_celsius(K):
    C = K - 273.15
    return C

def fahrenheit_to_kelvin(F):
    K = (F + 459.67) * 5/9
    return K

def fahrenheit_to_celsius(F):
    C = (F - 32) * 5/9
    return C

def celsius_to_kelvin(C):
    K = C + 273.15
    return K

def celsius_to_fahrenheit(C):
    F = C * 1.8 + 32
    return F

#@app.route('/')
#def home():
 #   return render_template('index.html')

#@app.route('/convert', methods=['POST'])
def convert(value):
    number = float(value[:-1])
    unit = value[-1].upper()
    conversion_result = ''

    if unit == 'K':
        result_fahrenheit = kelvin_to_fahrenheit(number).__round__(2)
        result_celsius = kelvin_to_celsius(number).__round__(2)
        conversion_result = f"{number} K = {result_fahrenheit} F\n{number} K = {result_celsius} C"
    elif unit == 'F':
        result_kelvin = fahrenheit_to_kelvin(number).__round__(2)
        result_celsius = fahrenheit_to_celsius(number).__round__(2)
        conversion_result = f"{number} F = {result_kelvin} K\n{number} F = {result_celsius} C"
    elif unit == 'C':
        result_kelvin = celsius_to_kelvin(number).__round__(2)
        result_fahrenheit = celsius_to_fahrenheit(number).__round__(2)
        conversion_result = f"{number} C = {result_kelvin} K\n{number} C = {result_fahrenheit} F"
    else:
        conversion_result = "Invalid choice. Please try again."

    return conversion_result
    #return render_template('index.html', conversion_result=conversion_result)

#if __name__ == '__main__':
 #   app.run()
