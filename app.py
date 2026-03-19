from flask import Flask, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

# This function saves the transaction to a text file so you don't lose data
def save_to_log(data):
    with open("transactions.log", "a") as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"[{timestamp}] {json.dumps(data)}\n")

@app.route('/mpesa/callback', methods=['POST'])
def mpesa_listener():
    data = request.get_json()
    
    if not data:
        return jsonify({"ResultCode": 1, "ResultDesc": "No Data"}), 400

    # Save the raw data immediately for backup
    save_to_log(data)

    try:
        # Extract the items list safely
        stk_callback = data.get('Body', {}).get('stkCallback', {})
        metadata = stk_callback.get('CallbackMetadata', {}).get('Item', [])
        
        # Convert list of dicts to a single easy dictionary
        details = {item['Name']: item.get('Value') for item in metadata}

        # Extract values with fallbacks to avoid "None" errors
        receipt = details.get('MpesaReceiptNumber', 'UNKNOWN')
        amount = details.get('Amount', 0.0)
        phone = details.get('PhoneNumber', 'N/A')
        raw_date = details.get('TransactionDate')

        # Fix the date error: If date is missing or wrong, use current time
        if raw_date:
            try:
                formatted_date = datetime.strptime(str(raw_date), '%Y%m%d%H%M%S').strftime('%d-%b-%Y %H:%M:%S')
            except:
                formatted_date = datetime.now().strftime('%d-%b-%Y %H:%M:%S')
        else:
            formatted_date = datetime.now().strftime('%d-%b-%Y %H:%M:%S')

        # Print a clean, professional report to your Kali terminal
        print("\n" + "█"*40)
        print(f"      NEW MPESA TRANSACTION")
        print("█"*40)
        print(f" RECEIPT: {receipt}")
        print(f" AMOUNT:  KES {amount}")
        print(f" SENDER:  {phone}")
        print(f" TIME:    {formatted_date}")
        print("█"*40 + "\n")

        return jsonify({"ResultCode": 0, "ResultDesc": "Success"}), 200

    except Exception as e:
        print(f"Error processing: {e}")
        return jsonify({"ResultCode": 1, "ResultDesc": "Internal Error"}), 500

if __name__ == '__main__':
    # Running on all network interfaces of your T480
    app.run(host='0.0.0.0', port=5000, debug=True)