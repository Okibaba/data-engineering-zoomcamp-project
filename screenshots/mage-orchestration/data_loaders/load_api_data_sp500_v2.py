import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_from_api(*args, **kwargs):
    #url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz'
    url= 'https://raw.githubusercontent.com/Okibaba/data-engineering-zoomcamp-project/main/data/sp500_stocks.csv'
  
    

    sp500_dtypes = {
                   # 'Date':str,
                    'Symbol':str,
                    'Adj Close':float,
                    'Close':float,
                    'Adj Close':float,
                    'High':float,
                    'Low':float,
                    'Open':float,
                    'Volume': pd.Int64Dtype()
                }

    # native date parsing 
    parse_dates = ['Date']

    return pd.read_csv(
        url, sep=',', dtype=sp500_dtypes, parse_dates=parse_dates
        )
    # return pd.read_csv(
    #     url, sep=',', dtype=sp500_dtypes
    #     )

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'