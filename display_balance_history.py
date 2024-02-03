import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime as dt
from sys import argv as args

def main():
    fp = args[1]
    
    fig, ax = plt.subplots()
    ax.grid("both")

    for fp in args[1:len(args)]:
        plot_history(ax, fp)

    ax.legend()
    plt.show()

def plot_history(ax, fp):
    with open(fp) as f:
        giro_html = f.read()

    giro = pd.read_html(giro_html)

    i = 1
    j = -1

    date = list(giro[0].Date)[i:j]
    balance = list(giro[0]["Running Balance"])[i:j]

    #parse dates and balances

    date = [dt.strptime(i, "%m/%d/%Y") for i in date]
    balance = [strp_currency(i) for i in balance]

    ax.plot(date, balance, label = fp)

def strp_currency(amount: str):
    amount = amount.replace("€", "")
    amount = amount.replace(",", "")
    return float(amount)

if __name__ == "__main__":
    main()