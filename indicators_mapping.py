### Script to map indicators based on tagging in indicators_lists_json##
import json
import pandas



with open('data/indicators_lists.json') as data_file:
    data = json.load(data_file)

ethiopia = data['ethiopia']
kivu = data['kivu']
rca = data['rca']

def measure_dimension_distance( indicator1 , indicator2 , dimension , distance):
    """Measures disance in given dimension between two indicators

    """
    dim1 = indicator1[dimension]
    dim2 = indicator2[dimension]
    distance_indics = (dim1 != dim2)*distance
    return distance_indics

def get_indicator_dimension(indicator):
    """Gets the dimensions in a given indicator.

    Gets the different tagging dimensions in an indicator and returns them as a
    list.

    Args:
        indicator: an indicator for which we want to know distance

    Returns:
        A list of dimensions of indicator
    """
    keys = {}
    for key in indicator.keys() :
        if isinstance(indicator[key],str) == True :
            sub_key = None
        if isinstance(indicator[key],dict) == True :
            sub_key = list(indicator[key].keys())
        keys[key] = sub_key
    return keys



measure_dimension_distance(ethiopia['ETH1'] , ethiopia['ETH3'] , 'icd10' , 10)






get_indicator_dimension(ethiopia['ETH3'] )
