import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_location_names():
    global __data_columns
    global __locations
    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    return __locations


def load_location_names():
    print('loading saved artifacts ----start')
    # with open("./artifacts/columns.json", "r") as f:
    #     __data_columns = json.load(f)['data_columns']
    #     __locations = __data_columns[3:]
    # global __model
    # with open("./artifacts/banglore_home_price_model.pickle", "rb") as f:
    #     __model = pickle.load(f)
    print('loading saved artifacts......done')


def get_estimated_price(location, total_sqft, bhk, bath):
    global __model
    with open("./artifacts/banglore_home_price_model.pickle", "rb") as f:
        __model = pickle.load(f)
    # loc_index = np.where(x.columns == location)[0][0]
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    xx = np.zeros(len(__data_columns))
    xx[0] = total_sqft
    xx[1] = bath
    xx[2] = bhk
    if loc_index >= 0:
        xx[loc_index] = 1
    return round(__model.predict([xx])[0], 2)


if __name__ == '__main__':
    load_location_names()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Indira Nagar', 1000, 4, 4))
    print(get_estimated_price('kalhalli', 1000, 4, 4))
