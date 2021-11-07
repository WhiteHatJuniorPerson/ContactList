from flask import Flask, jsonify, request
app = Flask(__name__)
data = [{
    "id": 1,
    "name": "Vihaan Tampi",
    "contact": "9625370962"
}]


@app.route("/addData", methods=["POST"])
def addData():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "add data before running the program"
        })
    else:
        D = {
            "id": data[-1]["id"]+1,
            "name": request.json["name"],
            "contact": request.json["contact"]
        }
        data.append(D)
        return jsonify({
            "status": "succesfull",
            "message": "data was added succesfully"
        })


@app.route("/display")
def displayData():
    return jsonify({
        "data": data
    })


if(__name__ == "__main__"):
    app.run(debug=True)
