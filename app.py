from flask import Flask, render_template, jsonify
from ai_model import generate_dynamic_strategy

app = Flask(__name__)

ASSETS = ["BTC-USD", "ETH-USD", "BNB-USD", "XRP-USD", "SOL-USD", "ADA-USD", "DOGE-USD", 
          "TRX-USD", "DOT-USD", "MATIC-USD", "LTC-USD", "SHIB-USD", "AVAX-USD", "LINK-USD", 
          "ATOM-USD", "XMR-USD", "UNI-USD", "BCH-USD", "XLM-USD", "ALGO-USD", "GC=F"] 

@app.route('/')
def home():
    return render_template('index.html', assets=ASSETS)

@app.route('/api/predict/<symbol>')
def get_prediction(symbol):
    # Yapay zeka motorunu doğrudan çağırıyoruz
    result = generate_dynamic_strategy(symbol)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
