from flask import Flask, request, jsonify

app = Flask(__name__)

def is_prime(number):
    if number == 1:
        return False
    for i in range(2, number):
            if number % i == 0:
                return False
    return True

@app.route("/alkuluku/<int:number>")
def prime_check(number):
    response = {"Number": number, "isPrime": is_prime(number)}
    return jsonify(response)

if __name__ == "__main__":
    app.run(use_reloader=True, host = '127.0.0.1', port=3000)