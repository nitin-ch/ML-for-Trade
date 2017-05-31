"""Utility functions"""

import os
import pandas as pd
import matplotlib.pyplot as plt


def plot_data(df, title="Stock prices"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()


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


def plot_selected(df, symbol, sd, ed):

    # Slice
    df = df.loc[sd:ed, symbol]
    df = normalize(df)
    # plot_selected
    plot_data(df)


def normalize(df):
    # Normalize using the first row of data
    return df / df.iloc[0]


def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']

    # Get stock data
    df = get_data(symbols, dates)
    # print df

    # Row Indexing using iloc and loc
    # print df.loc['2010-01-01':'2010-01-31']  # month of January

    # Column Slicing
    # print df[['IBM', 'GOOG']]  # Multiple Stocks

    # Row + Column Slicing
    # print df.loc['2010-01-01':'2010-01-31', ['IBM', 'GOOG']]

    # ax = df.plot.line(title="Stock Prices", fontsize=2)
    # ax.set_xlabel("Date")
    # ax.set_ylabel("Price")
    # plt.show()
    plot_selected(df, ['SPY', 'IBM', 'GOOG', 'GLD'], '2010-01-01', '2010-12-31')


if __name__ == "__main__":
    test_run()
