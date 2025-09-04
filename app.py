from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    mode = data.get('mode')
    text = data.get('text', '')
    shift = str(data.get('shift', 0))

    print(f"[INFO] Received: mode={mode}, shift={shift}, text={text}")

    try:
        result = subprocess.run(
            ['./caesar_cipher'],
            input=f"{mode}\n{text}\n{shift}",
            text=True,
            capture_output=True,
            check=True
        )
        output = result.stdout.strip()
        return jsonify({'result': output})
    except subprocess.CalledProcessError as e:
        print("[ERROR] Subprocess failed:", e)
        return jsonify({'error': 'C++ execution failed'}), 500

if __name__ == '__main__':
    app.run(debug=True)
