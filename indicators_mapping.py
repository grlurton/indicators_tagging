### Script to map indicators based on tagging in indicators_lists_json##
import json
import pandas



with open('data/indicators_lists.json') as data_file:
    data = json.load(data_file)

ethiopia = data['ethiopia']
kivu = data['kivu']
rca = data['rca']


def get_indicator(indicator1) :
    """Gets an indicator and looks into it.
    Args:
        indicator1: Indicator we want to look into.
    """
    print(indicator1)



def measure_dimension_distance( indicator1 , indicator2 , dimension , distance):
    """Measures disance in given dimension between two indicators

    """
    dim1 = indicator1[dimension]
    dim2 = indicator2[dimension]
    distance_indics = (dim1 != dim2)*distance
    return distance_indics

measure_dimension_distance(ethiopia['ETH1'] , ethiopia['ETH3'] , 'icd10' , 10)
