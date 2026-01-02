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


@app.route('/notif', methods=['POST'])
def notification():
    """Handle payment notification
    
    Expected JSON payload:
    {
        "status": str,
        "invoice_id": str,
        "amount_crypto": int,
        "currency": str,
        "order_id": str,
        "invoice_info": dict
    }
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['status', 'invoice_id', 'amount_crypto', 'currency', 'order_id', 'invoice_info']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Process the notification
        status = data.get('status')
        invoice_id = data.get('invoice_id')
        amount_crypto = data.get('amount_crypto')
        currency = data.get('currency')
        order_id = data.get('order_id')
        invoice_info = data.get('invoice_info')
        
        # Here you can add logic to process the payment notification
        # For example, update database, send confirmation email, etc.
        
        return jsonify({'message': 'payment_accepted'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=False)
