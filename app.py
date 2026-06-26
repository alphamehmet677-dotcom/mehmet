from flask import Flask, render_template, jsonify
from ai_model import fetch_data, generate_dynamic_strategy

app = Flask(__name__)

# İzlenecek Varlıklar (20 Coin + Altın)
ASSETS = ["BTC-USD", "ETH-USD", "BNB-USD", "XRP-USD", "SOL-USD", "ADA-USD", "DOGE-USD", 
          "TRX-USD", "DOT-USD", "MATIC-USD", "LTC-USD", "SHIB-USD", "AVAX-USD", "LINK-USD", 
          "ATOM-USD", "XMR-USD", "UNI-USD", "BCH-USD", "XLM-USD", "ALGO-USD", "GC=F"] # GC=F Altın (XAU) temsilidir

@app.route('/')
def home():
    return render_template('index.html', assets=ASSETS)

@app.route('/api/predict/<symbol>')
def get_prediction(symbol):
    data = fetch_data(symbol)
    result = generate_dynamic_strategy(data, symbol)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')