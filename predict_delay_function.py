# module import
import datetime
import os
import json
import boto3
import numpy as np
from decimal import Decimal

IMOS = [9811000]

print('Loading function')

#Dummy historical data consist of diff value of (eta-timeOfLastPost) each year during specific month of the vessel at that position
json_historical_data = """
        {
            "historical":[
                {
                    "key":"2011-08",
                    "value":60400.0
                },
                {
                    "key":"2012-08",
                    "value":98400.0
                },
                {
                    "key":"2013-08",
                    "value":90400.0
                },
                {
                    "key":"2014-08",
                    "value":89400.0
                },
                {
                    "key":"2015-08",
                    "value":85400.0
                },
                {
                    "key":"2016-08",
                    "value":216400.0
                },
                {
                    "key":"2017-08",
                    "value":206400.0
                },
                {
                    "key":"2018-08",
                    "value":106400.0
                },
                {
                    "key":"2019-08",
                    "value":76400.0
                },
                {
                    "key":"2020-08",
                    "value":96400.0
                }
            ]
        }
        """


def lambda_handler(event, context):
    """
        Criteria of delay:
        Current diff (eta-timeOfLastPost) > average diff (eta-timeOfLastPost) from historical data

        If the vessel will be delayed it will return True and print "Vessel Will Delay"
        Otherwise it will return False and print "Vessel Will Not Delay"

    """
    try:
        # json_vesell_file = open('vessel_data.json')
        # decoded = json.loads(json_vesell_file, parse_float=Decimal)

        # Access data
        # time_eta = decoded['reported_eta']
        # time_cur = decoded['time_of_latest_position']

        time_eta = event['reported_eta']
        time_cur = event['time_of_latest_position']

        curr_diff = calc_diff_time(time_eta, time_cur)

        # json_vesell_file.close()

        decoded = json.loads(json_historical_data, parse_float=Decimal)

        diff_values = []

        # Access data
        for data in decoded['historical']:
            diff_values.append(data['value'])

        average_diff = calc_average_diff_time(diff_values)

        if(curr_diff > average_diff):
            print("Vessel Will Delay")
            return True
        else:
            print("Vessel Will Not Delay")
            return False

        # json_historical_file.close()

    except (ValueError, KeyError, TypeError):
        print("JSON format error")

    return {
        'statusCode': 200,
        'body': json.dumps('hello!')
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
