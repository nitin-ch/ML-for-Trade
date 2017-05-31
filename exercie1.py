"""Utility functions"""

import os
import pandas as pd


def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.join(current_dir, base_dir)
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        # TODO: Read and join data for each symbol
        dfSym = pd.read_csv(symbol_to_path(symbol), index_col="Date",
                            parse_dates=True, usecols=['Date', 'Adj Close'],
                            na_values='nan')
        dfSym = dfSym.rename(columns={'Adj Close': symbol})
        df = df.join(dfSym, how='inner')
#        if symbol == 'SPY':
#            df = df.dropna(subset=['SPY'])
    return df


def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-22', '2010-01-26')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']

    # Get stock data
    df = get_data(symbols, dates)
    print df


if __name__ == "__main__":
    test_run()
