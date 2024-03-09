import streamlit as st
import pandas as pd
import requests
import plotly.graph_objects as go
from datetime import datetime

def get_real_time_price(symbol):
    """Fetches real-time stock price data from Polygon.io API."""
    API_KEY = 'QwznCIMoAuFPf2M1chnINcXmd9TzGxAQ'
    base_url = 'https://api.polygon.io/v2/aggs/ticker/' + symbol + '/prev'
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    response = requests.get(base_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {'Error': f"API request failed with status code: {response.status_code}"}

def get_historical_price(symbol, from_date, to_date, interval='1min'):
    """Fetches historical stock price data from Polygon.io API."""
    API_KEY = 'QwznCIMoAuFPf2M1chnINcXmd9TzGxAQ'
    base_url = f"https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/minute/2023-01-01/2024-03-07?adjusted=true&sort=asc&limit=120&apiKey=QwznCIMoAuFPf2M1chnINcXmd9TzGxAQ"
    response = requests.get(base_url)
    if response.status_code == 200:
        return response.json()
    else:
        return {'Error': f"API request failed with status code: {response.status_code}"}

def display_stock_price(symbol, interval):
    """Displays stock price data and chart."""
    interval_map = {'Real-time': 'Real-time', 'minute': '1', '5 minute': '5', '15 minute': '15', '30 minute': '30',
                    'hour': '60'}
    try:
        if interval == 'Real-time':
            data = get_real_time_price(symbol)
            if 'Error' in data:
                st.error(data['Error'])
                return
            df = pd.DataFrame([data['results'][0]])
            df['t'] = pd.to_datetime(df['t'], unit='ms')
            df.set_index('t', inplace=True)
            st.write(f"**{symbol} (as of {df.index[-1]})**")
        else:
            today = datetime.today().strftime('%Y-%m-%d')  # Get today's date
            from_date = st.date_input("From Date:", value=pd.Timestamp(year=2023, month=11, day=28))  # Preset start date
            to_date = st.date_input("To Date:", value=pd.Timestamp(today))  # Preset end date to today
            data = get_historical_price(symbol, from_date.strftime('%Y-%m-%d'), to_date.strftime('%Y-%m-%d'), interval_map[interval])
            if 'Error' in data:
                st.error(data['Error'])
                return
            df = pd.DataFrame(data['results'])
            df['t'] = pd.to_datetime(df['t'], unit='ms')
            df.set_index('t', inplace=True)

        st.write("""
                            This chart displays the Open, High, Low, Close (OHLC) prices of the stock over time. 
                            Each candlestick represents the price movement within a specific time interval.
                            """)

        # Create candlestick chart
        fig = go.Figure(data=[go.Candlestick(x=df.index,
                                             open=df['o'],
                                             high=df['h'],
                                             low=df['l'],
                                             close=df['c'])])
        fig.update_layout(title=f"{symbol} Candlestick Chart",
                          xaxis_title='Date',
                          yaxis_title='Price',
                          xaxis_rangeslider_visible=False)
        st.plotly_chart(fig, use_container_width=True)

    except requests.exceptions.RequestException as e:
        st.error("Error: Failed to connect to Polygon.io API. Please check your internet connection and try again.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")


def main():
    """Main function to display the Real-time Stock Price Dashboard"""
    symbol = st.text_input("Enter Stock Symbol:")
    interval_options = ["Real-time", "1 minute", "5 minute", "15 minute", "30 minute", "1 hour"]
    interval = st.selectbox("Select Time Interval:", interval_options)
    if symbol:
        with st.spinner('Fetching data...'):
            display_stock_price(symbol, interval)

if __name__ == '__main__':
    main()
