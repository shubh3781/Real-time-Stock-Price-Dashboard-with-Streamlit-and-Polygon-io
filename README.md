# Real-Time Stock Price Dashboard using Streamlit and Polygon.io API

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Key Setup](#api-key-setup)
- [Code Structure](#code-structure)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Overview

This project is a Streamlit web application that provides real-time and historical stock price data visualization using the [Polygon.io API](https://polygon.io/). Users can input a stock symbol and select a time interval to view candlestick charts representing the Open, High, Low, and Close (OHLC) prices of the stock over the specified period.

## Features

- **Real-Time Stock Prices**: Fetches and displays the latest stock price data.
- **Historical Data Visualization**: Allows users to select a date range and interval to view historical stock prices.
- **Interactive Candlestick Charts**: Uses Plotly to generate interactive candlestick charts for data visualization.
- **User-Friendly Interface**: Built with Streamlit for easy interaction and deployment.

## Requirements

- Python 3.x
- Streamlit
- pandas
- requests
- plotly

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/real-time-stock-dashboard.git
   cd real-time-stock-dashboard
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install the Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

   *Note: If `requirements.txt` is not available, install the packages manually:*

   ```bash
   pip install streamlit pandas requests plotly
   ```

## Usage

1. **Set Up the Polygon.io API Key**

   - Sign up for a free API key at [Polygon.io](https://polygon.io/).
   - Replace the `API_KEY` variable in the `get_real_time_price` and `get_historical_price` functions with your API key.

2. **Run the Streamlit App**

   ```bash
   streamlit run app.py
   ```

3. **Interact with the App**

   - **Enter Stock Symbol**: Input the stock ticker symbol (e.g., `AAPL` for Apple Inc.).
   - **Select Time Interval**: Choose between real-time or various historical intervals (1 minute, 5 minutes, etc.).
   - **Select Date Range** (for historical data): Pick the start and end dates for the data you wish to view.
   - **View the Candlestick Chart**: The app will display an interactive candlestick chart of the stock's OHLC prices over the selected period.

## API Key Setup

To use the Polygon.io API, you need to obtain an API key:

1. **Sign Up**: Go to [Polygon.io](https://polygon.io/) and sign up for a free account.
2. **Obtain API Key**: After signing up, navigate to your dashboard to find your API key.
3. **Update the Code**: Replace the placeholder `API_KEY` in the `app.py` file with your actual API key:

   ```python
   API_KEY = 'YOUR_ACTUAL_API_KEY'
   ```

## Code Structure

- **app.py**: The main Streamlit application file containing all the functions and the app's layout.

### Functions

- `get_real_time_price(symbol)`: Fetches real-time stock price data for the given symbol.
- `get_historical_price(symbol, from_date, to_date, interval)`: Fetches historical stock price data for the given symbol and date range.
- `display_stock_price(symbol, interval)`: Processes the data and displays the candlestick chart.
- `main()`: The main function that sets up the Streamlit interface.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/) for providing an easy-to-use web application framework.
- [Polygon.io](https://polygon.io/) for providing financial market data APIs.
- [Plotly](https://plotly.com/python/) for interactive data visualization.
