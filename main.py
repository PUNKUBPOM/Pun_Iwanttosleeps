from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Update this with your Raspberry Pi's IP address
RASPBERRY_PI_API_URL = "http://<192.168.1.36>:5000/capture"

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    try:
        # Send a request to the Raspberry Pi server
        response = requests.post(RASPBERRY_PI_API_URL)
        response_data = response.json()

        # Return the result to the frontend
        return jsonify({
            "message": response_data["message"],
            "image_url": response_data["image_url"]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='192.168.1.36', port=5000)
