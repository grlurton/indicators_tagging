### Script to map indicators based on tagging in indicators_lists_json##
import json
import pandas as pd

with open('data/indicators_lists.json') as data_file:
    data = json.load(data_file)

ethiopia = data['ethiopia']
kivu = data['kivu']
rca = data['rca']

def measure_dimension_distance( indicator1 , indicator2 , dimension , distance):
    """Measures disance in given dimension between two indicators

    """
    try :
        dim1 = indicator1[dimension]
        dim2 = indicator2[dimension]
        distance_indics = (dim1 != dim2)*distance
        return distance_indics
    except KeyError :
        return distance

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

def compare_indicators(indicator1 , indicator2):
    distances = {}
    dims_indicator1 = get_indicator_dimension(indicator1)
    dims_indicator2 = get_indicator_dimension(indicator2)
    for dim in dims_indicator1 :
        if dims_indicator1[dim] == None :
            dist = measure_dimension_distance(indicator1 , indicator2 , dim , 100)
            distances[dim] = dist
        if dims_indicator1[dim] != None :
            for sub_dim in dims_indicator1[dim] :
                dist = measure_dimension_distance(indicator1[dim] , indicator2[dim] , sub_dim , 5)
                distances[sub_dim] = dist
    return(distances)

def match_indicator_in_dataset(indicator , data_set):
    distances = []
    indicators = []
    lib = []
    for indicator2 in data_set.keys() :
        indicators.append(indicator2)
        lib.append(data_set[indicator2]['lib'])
        try :
            dists = compare_indicators(indicator , data_set[indicator2])
            out = sum(dists.values()) / len(dists)
            distances.append(out)
        except KeyError :
            distances.append(None)
    data_out = {'indicators' : indicators , 'distances' : distances , 'lib':lib}
    out = pd.DataFrame(data_out)
    return(out)

match_ethiopie_rca = {}
for indic in ethiopia.keys() :
    pca_match = match_indicator_in_dataset(ethiopia[indic] , rca['pca'])
    pma_match = match_indicator_in_dataset(ethiopia[indic] , rca['pma'])
    full = pca_match.append(pma_match)
    full = full.to_json( orient = 'records' )
    match_ethiopie_rca[indic] = {'lib':ethiopia[indic]['lib'] , 'matching':full}


match_ethiopie_kivu = {}
for indic in ethiopia.keys() :
    pca_match = match_indicator_in_dataset(ethiopia[indic] , kivu['pca'])
    pma_match = match_indicator_in_dataset(ethiopia[indic] , kivu['pma'])
    full = pca_match.append(pma_match)
    full = full.to_json( orient = 'records' )
    match_ethiopie_kivu[indic] = {'lib':ethiopia[indic]['lib'] , 'matching':full}

with open('outputs/ethiopie_rca_map.json', 'w') as f:
    json.dump(match_ethiopie_rca, f , ensure_ascii=False)

with open('outputs/ethiopie_kivu_map.json', 'w') as f:
    json.dump(match_ethiopie_kivu, f , ensure_ascii=False)
