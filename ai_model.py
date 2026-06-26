import pandas as pd
import numpy as np

def fetch_data(symbol="BTC-USD", period="5y", interval="15m"):
    # Gerçek projede Binance API veya yfinance kullanılır. 
    # Not: yfinance 15m veriyi en fazla 60 gün verir. 5 yıl için Binance geçmiş veri arşivi (Klines) indirilmelidir.
    # Burada konsepti anlaman için sahte bir veri çerçevesi oluşturuyoruz.
    dates = pd.date_range(end=pd.Timestamp.now(), periods=100, freq='15T')
    data = pd.DataFrame({
        'Close': np.random.uniform(100, 200, size=100),
        'Volume': np.random.uniform(1000, 5000, size=100)
    }, index=dates)
    return data

def generate_dynamic_strategy(data, symbol):
    """
    Mehmet Alparslan'ın özgün tahmini. 
    Gerçek senaryoda burada önceden eğitilmiş bir LSTM veya XGBoost modeli (model.predict) çalışır.
    Her coin'in kendine has volatilite ve trend yapısına göre eğitilmiştir.
    """
    # Son 15 dakikanın kapanış fiyatı
    current_price = data['Close'].iloc[-1]
    
    # Yapay zekanın "gelecek öngörüsü" (Simülasyon)
    prediction_score = np.random.uniform(-1, 1) 
    
    if prediction_score > 0.2:
        action = "YÜKSELECEK (LONG)"
        color = "green"
    elif prediction_score < -0.2:
        action = "DÜŞECEK (SHORT)"
        color = "red"
    else:
        action = "YATAY/BEKLE"
        color = "gray"
        
    # Backtest verisi simülasyonu
    win_rate = round(np.random.uniform(55, 85), 2)
    total_trades = np.random.randint(500, 5000)
    
    return {
        "symbol": symbol,
        "current_price": round(current_price, 2),
        "prediction": action,
        "color": color,
        "backtest": {
            "win_rate": f"%{win_rate}",
            "total_trades": total_trades,
            "profit_factor": round(np.random.uniform(1.2, 3.5), 2)
        }
    }