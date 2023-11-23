from flask import Flask

app = Flask(__name__)


@app.route('/prime_number/<number>')
def is_prime(number):
    number = int(number)
    result = True
    if number <= 1:
        result = False
    else:
        for i in range(2, number):
            if number % i == 0:
                result = False

    response = {"Number": number, "isPrime": result}
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

