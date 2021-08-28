#module import
import datetime
import os
import json
import boto3
import numpy as np
from decimal import Decimal

IMOS = [9811000]

def lambda_handler(event, context):
    print("Hello!")
    """
        Criteria of delay:
        Current diff (eta-timeOfLastPost) > average diff (eta-timeOfLastPost) from historical data
    """

    json_vesell_file = open('vessel_data.json',)

    try:
        decoded = json.loads(json_vesell_file, parse_float=Decimal)

        # Access data
        time_eta = decoded['reported_eta']
        time_cur = decoded['time_of_latest_position']

        json_historical_file.close()
    except (ValueError, KeyError, TypeError):
        print "JSON format error"

    curr_diff = calc_diff_time(time_eta, time_cur)

    json_historical_file = open('historical_data.json',)

    try:
        decoded = json.loads(json_historical_file, parse_float=Decimal)

        diff_values = []
    
        # Access data
        for data in decoded['historical']:
            diff_values.append(data['value'])

        json_historical_file.close()
    except (ValueError, KeyError, TypeError):
        print "JSON format error"

    average_diff = calc_average_diff_time(diff_values)
    if(cur_diff > average_diff):
        return true
    elif
        return false

    return {
        'statusCode': 200,
        'body': json.dump('hello!')
    }

def calc_average_diff_time(arr):
    return np.mean(arr)        

def calc_diff_time(time_eta, time_cur):
    date_format = "%Y-%m-%d %H:%M:%S"
    time_1 = datetime.datetime.strptime(time_eta,
                                         date_format)
    time_2 = datetime.datetime.strptime(time_cur,
                                         date_format)
    unix_time_1 = datetime.datetime.timestamp(time_1)
    unix_time_2 = datetime.datetime.timestamp(time_2)
    return (unix_time_1 - unix_time_2)
