from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Example calculation logic
def calculate_output(inputs):
    try:
        a1 = float(inputs.get('A1', 0))
        b1 = float(inputs.get('B1', 0))
        multiplier = float(inputs.get('multiplier', 1))  # Default to 1
        c1 = (a1 * multiplier) + (b1 * multiplier)
        return {"outputs": {"C1": c1}}
    except Exception as e:
        return {"error": f"Calculation error: {str(e)}"}

# API endpoint for calculation
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Parse the input data from the request
        data = request.json
        inputs = data.get("inputs", {})
        
        # Debug log for inputs
        print("Received inputs:", inputs)

        # Perform calculations
        output = calculate_output(inputs)

        # Return the result as JSON
        return jsonify(output), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
