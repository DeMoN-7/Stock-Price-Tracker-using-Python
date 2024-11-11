import requests
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import datetime

# API details
api_key = "f8dd3e83089f4bd5ab4007cd0272a01d"

# Function to fetch the current stock price
def get_stock_price(ticker_symbol):
    url = f"https://api.twelvedata.com/price?symbol={ticker_symbol}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data.get("price")

# Function to fetch historical price data
def get_price_history(ticker_symbol, interval="1day", output_size=30):
    url = f"https://api.twelvedata.com/time_series?symbol={ticker_symbol}&interval={interval}&outputsize={output_size}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    
    # Extract dates and closing prices
    if "values" in data:
        # Format dates to only include month and day
        dates = [entry['datetime'][5:10] for entry in data['values']]  # Extract MM-DD from 'YYYY-MM-DD'
        prices = [float(entry['close']) for entry in data['values']]
        return dates, prices
    else:
        return None, None


# Function to update the current price in the GUI
def update_price():
    ticker_symbol = symbol_entry.get().upper()
    if not ticker_symbol:
        messagebox.showerror("Input Error", "Please enter a stock symbol.")
        return

    price = get_stock_price(ticker_symbol)
    if price:
        price_label.config(text=f"Current price of {ticker_symbol}: ${price}")
    else:
        price_label.config(text="Error fetching price data. Check symbol and try again.")
    
    # Schedule the next update
    root.after(60000, update_price)  # Update every 60 seconds

# Function to display the historical price plot
def show_price_history():
    ticker_symbol = symbol_entry.get().upper()
    dates, prices = get_price_history(ticker_symbol)
    
    if dates and prices:
        fig, ax = plt.subplots(figsize=(8, 6))  # Increase figsize for better readability
        ax.plot(dates, prices, label="Closing Price", color="blue", marker="o")
        ax.set_title(f"{ticker_symbol} Price History")
        ax.set_xlabel("Date (MM-DD)")
        ax.set_ylabel("Price (USD)")
        ax.invert_xaxis()  # Show recent dates on the right
        ax.grid(True)

        # Rotate x-axis labels and adjust layout
        plt.xticks(rotation=45, ha="right")
        fig.tight_layout()

        # Display the plot in Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=20)  # Add padding to separate the graph from other widgets

    else:
        messagebox.showerror("Data Error", "Could not retrieve historical data. Check symbol or try again later.")



# Set up the GUI
root = tk.Tk()
root.title("Stock Price Tracker")
root.geometry("600x500")

# Stock symbol entry
symbol_label = tk.Label(root, text="Enter Stock Symbol:")
symbol_label.pack(pady=10)

symbol_entry = tk.Entry(root, width=20)
symbol_entry.pack(pady=5)

# Price display label
price_label = tk.Label(root, text="Price will be displayed here", font=("Helvetica", 16))
price_label.pack(pady=20)

# Button to track current price
track_button = tk.Button(root, text="Track Current Price", command=update_price)
track_button.pack(pady=10)

# Button to show historical price
history_button = tk.Button(root, text="Show Price History", command=show_price_history)
history_button.pack(pady=10)

# Start the GUI loop
root.mainloop()
