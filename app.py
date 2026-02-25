from flask import Flask, request, jsonify
from suma import sumar

app = Flask(__name__)

@app.route("/sumar", methods=["GET"])
def api_sumar():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    resultado = sumar(a, b)
    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(debug=True)