from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_mining', methods=['POST'])
def start_mining():
    # Логика старта майнинга
    return jsonify({'status': 'mining_started', 'time_left': 10, 'earned_coins': 0})

@app.route('/claim_coins', methods=['POST'])
def claim_coins():
    # Логика завершения майнинга и получения монет
    return jsonify({'status': 'coins_claimed', 'total_coins': 100})

if __name__ == '__main__':
    app.run(debug=True)
