# AIPI 510: Premodule Assignment: historical-price-stat

This is a Python script that can calculate key stats (average/minimum/maximum) of a time series of historical closing prices, from CSV price source.

## Installation

1. Install `setuptools`, if it has not already been installed in your system
```
pip install setuptools
```
2. In `historial-price-stat` directory, run `setup.py`
```
python setup.py develop
```
3. To run the code, type the followings in the terminal
```
pricestat <csvfilename>
```
where `<csvfilename>` is the path to the CSV file, with a series of historical closing prices in column `Close`
(If the column name is not named as `Close`, then you have to rename it to `Close` first)

For example, to calculate key stats (average/minimum/maximum closing prices) from `.\csvexamples\NVDA_1Y.csv`:
```
pricestat .\csvexamples\NVDA_1Y.csv
```
You should see output like this:
```
Price Source : .\csvexamples\NVDA_1Y.csv
Average Closing Price : 77.92
Min Closing Price : 40.33
Max Closing Price : 135.58
```

To calculate key stats (average/minimum/maximum closing prices) from `.\csvexamples\BTCUSD_1Y.csv`:
```
pricestat .\csvexamples\BTCUSD_1Y.csv
```
You should see output like this:
```
Price Source : .\csvexamples\BTCUSD_1Y.csv
Average Closing Price : 50788.95
Min Closing Price : 25133.30
Max Closing Price : 73097.77
```

Source of the example CSVs:
* https://finance.yahoo.com/quote/NVDA/history/ 
(Specify date range, then click 'Download' to download the CSV file)
* https://www.coingecko.com/en/coins/bitcoin/historical_data
(Click the download icon on the top right corner of the price table, and choose `.csv` from the drop-down menu; Once downloaded, rename column `price` to `Close`)

## Testing
1. Install `pytest`, if you would like to do a unit test and pytest has not already been installed in your system
```
pip install pytest
```
2. Run `pytest` to test the function `load_csv_calc_keystats`
```
pytest
```
Or
```
pytest .\tests\test_main.py
```
This will run function `test_load_csv_calc_keystats` in `.\tests\test_main.py`, using `GOOG_1Y.csv` in the `tests` folder
