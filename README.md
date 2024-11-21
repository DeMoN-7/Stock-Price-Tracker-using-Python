# Stock Price Tracker Using Python

A simple desktop application built with Python using `tkinter` and `matplotlib` to track and display real-time stock prices and historical price data. It integrates with the Twelve Data API to fetch both current stock prices and historical data for various stock symbols.

## Features

- Track the current price of a stock symbol.
- View the historical price data of a stock for the last 30 days.
- Real-time updates every minute for current stock prices.
- Visual representation of historical stock prices using a line graph.

## Technologies Used

- **Python 3.x**
- **Tkinter** (for creating the GUI)
- **Requests** (for fetching stock price data via API)
- **Matplotlib** (for plotting stock price history)
- **Twelve Data API** (for fetching real-time and historical stock data)

## Setup and Installation

### Prerequisites
Make sure Python 3.x is installed on your machine. You can download Python from the official website: [python.org](https://www.python.org/).

### Steps to Install

1. Clone the repository:
   ```bash
   git clone https://github.com/DeMoN-7/Stock-Price-Tracker-using-Python.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Stock-Price-Tracker-using-Python
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Obtain an API key:
   - Sign up for a free account on [Twelve Data](https://twelvedata.com/) to get your API key.
   - Replace the placeholder `api_key` in the script with your actual API key.

5. Run the application:
   ```bash
   python stock_price_tracker.py
   ```

## Usage

Once the application is running, you can:

1. Enter a stock symbol (e.g., `AAPL` for Apple, `TSLA` for Tesla) in the input field.
2. Click "Track Current Price" to view the real-time stock price, which will update every minute.
3. Click "Show Price History" to view the stock's historical prices for the past 30 days, displayed on a graph.

Example:
```bash
Enter stock symbol: AAPL
Fetching stock data...
Current Price: $150.25
```

## Functions

- **`get_stock_price(ticker_symbol)`**: Fetches the current price of the given stock symbol using the Twelve Data API.
- **`get_price_history(ticker_symbol, interval="1day", output_size=30)`**: Fetches historical stock data for the given symbol and returns a list of dates and closing prices.
- **`update_price()`**: Updates the current stock price displayed in the GUI every minute.
- **`show_price_history()`**: Displays a line graph of the stock's historical price data.

## Screenshot

Below is a screenshot of the Stock Price Tracker application:<br>
<img src="https://github.com/user-attachments/assets/96fffbae-c1a4-4d3d-953a-9e600f9f113f" alt="Screenshot 1" width="250" height="250">
<img src="https://github.com/user-attachments/assets/c3633718-5e2c-425b-bccd-cfac5c81913f" alt="Screenshot 2" width="250" height="250">


*The screenshot above shows the stock symbol input field, the real-time stock price, and the option to view the stock's price history as a graph.*

## Customization

You can customize the following:
- **API Key**: Replace the `api_key` variable with your own Twelve Data API key.
- **Stock Data Interval**: Adjust the `interval` parameter in `get_price_history` (e.g., `1day`, `1hour`) for different time spans.
- **Graph Appearance**: Modify `matplotlib` settings to change the appearance of the historical price graph.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgements

- [Twelve Data API](https://twelvedata.com/) for providing free stock data.
- [Matplotlib](https://matplotlib.org/) for data visualization.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for building the GUI.

---
