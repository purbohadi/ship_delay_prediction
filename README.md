# ship_delay_prediction
Ship Delay Prediction AWS Lambda Function

This function will process event json data consist of vessel information that carry given container number [po_container_id].

The vessel information will be passed as json event and leverage vessel historical movement data at that location during that month each year.

The solution make an assumption if the average delta between current eta-timeOfLastPosition is bigger than the average delta eta-timeOfLastPosition from historical data, this will be treated as delay condition since on average the historical data show the threshold for the best time for this position.

1. The vessel event data assumed to be provided by getting from tracking API.
2. The historical vessel data is dummy for the scope of this solution, but can be easily replaced by query to local database contains vessels historical data.
3. The dummy historical data only contain key of year and month and the value is the delta of eta-timeOfLastPosition in unix time format.
4. The function will return True and print "Vessel Will Delay" Otherwise it will return False and print "Vessel Will Not Delay".



