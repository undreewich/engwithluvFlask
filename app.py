from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/', methods=['GET'])
def home():
    """Display home page"""
    return render_template('index.html')


@app.route('/SuccessPayment', methods=['GET'])
def success_payment():
    """Display success payment page"""
    return render_template('success_payment.html')


@app.route('/UnsuccessPayment', methods=['GET'])
def unsuccess_payment():
    """Display unsuccessful payment page"""
    return render_template('unsuccess_payment.html')


@app.route('/notif', methods=['GET', 'POST'])
def notification():
    # print(request)
    data = request.get_data()
    # print(2)
    # status = data.get('status')
    # print(3)
    # invoice_id = data.get('invoice_id')
    # print(4)
    # amount_crypto = data.get('amount_crypto')
    # print(5)
    # currency = data.get('currency')
    # print(6)
    # order_id = data.get('order_id')
    # print(7)
    # token = data.get('token')
    # print(8)

    return jsonify({'message': 'payment_accepted'}), 200




if __name__ == '__main__':
    app.run()
