import click
import pandas as pd

def load_csv_calc_keystats(csvfilename):
    # Load series of stock prices from CSV file and return average/min/max of closing prices

    # load csv into dataframe
    df = pd.read_csv(csvfilename)

    # calculate avg/min/max
    avgprice = round(df['Close'].mean(),2)
    minprice = round(df['Close'].min(),2)
    maxprice = round(df['Close'].max(),2)
    return [avgprice, minprice, maxprice]

@click.command()
@click.argument('csvfilename', type=click.Path(exists=True))
def main(csvfilename):
    # Load stock prices from CSV file, and print keystats based on series of closing prices
    
    # load csv and then calculate avg/min/max
    [avgprice, minprice, maxprice] = load_csv_calc_keystats(csvfilename)
    
    # print keystats on screen
    click.echo(
        f'Price Source : {csvfilename}\n'
        f'Average Closing Price : {avgprice:.2f}\n'
        f'Min Closing Price : {minprice:.2f}\n'
        f'Max Closing Price : {maxprice:.2f}'
    )