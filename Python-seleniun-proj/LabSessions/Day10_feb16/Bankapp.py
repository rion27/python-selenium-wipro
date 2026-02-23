from flask import Flask, request,jsonify

app=Flask(__name__)

customers={}
current_id=1

@app.route("/")
def home():
    return "Bank API is running"


#POST - Create customer
@app.route("/customers",methods=["POST","GET"])
def create_customer():
    global current_id
    if request.method == "POST":
        data = request.json
        customer = {
            "ID": current_id,
            "Name": data["Name"],
            "E-mail": data["E-mail"],
            "Balance": data["Balance"]
        }
        customers[current_id] = customer
        current_id += 1
        return jsonify(customer), 201

    elif request.method == "GET":
        return jsonify(list(customers.values())), 200

#GET - retrieve customer details
@app.route("/customers/<int:customer_id>",methods=["GET"])
def get_customer(customer_id):
    customer=customers.get(customer_id)

    if not customer:
        return jsonify({"Error": "Customer not found"}), 404

    return jsonify(customer),200

#PUT - Update whole customer(updates all fields)
@app.route("/customers/<int:customer_id>",methods=["PUT"])
def update_customer(customer_id):
    customer=customers.get(customer_id)
    if not customer:
        return jsonify({"Error": "Customer not found"}),404

    data=request.json
    customer["E-mail"]=data.get("E-mail",customer["E-mail"])
    return jsonify(customer),200

#DELETE - Remove customer
@app.route("/customers/<int:customer_id>",methods=["DELETE"])
def delete_customer(customer_id):
    if customer_id not in customers:
        return jsonify({"Error": "Customer not found"}),404

    del customers[customer_id]
    return "",204

if __name__=="__main__":
    app.run(debug=True)

