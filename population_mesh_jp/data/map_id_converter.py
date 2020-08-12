import itertools
from typing import List

import pandas as pd


def build_map_id_list(prefecture_name_list: List[str]):
    map_id_list = []
    for prefecture_name in prefecture_name_list:
        partial_map_id_list = convert_prefecture_to_mapid_list(prefecture_name=prefecture_name)
        map_id_list += partial_map_id_list

    map_id_list = sorted(list(set(map_id_list)))
    return map_id_list


def convert_prefecture_to_mapid_list(prefecture_name: str):
    minlat, maxlat, minlon, maxlon = convert_prefecture_to_latlon(prefecture_name=prefecture_name)
    minlat_id = lat2id(minlat)
    maxlat_id = lat2id(maxlat)
    minlon_id = lon2id(minlon)
    maxlon_id = lon2id(maxlon)

    lats = list(range(minlat_id, maxlat_id + 1))
    lons = list(range(minlon_id, maxlon_id + 1))
    latlon_pairs = itertools.product(lats, lons)
    mapid_list = sorted([f'{lat}{lon}' for lat, lon in latlon_pairs])
    return mapid_list


def convert_prefecture_to_latlon(prefecture_name: str):
    prefecture_df = pd.read_csv('./population_mesh_jp/data/prefec_edges.csv')
    match_df = prefecture_df.query(f'prefec_name.str.contains("{prefecture_name}")')

    if match_df.shape[0] != 1:
        raise ValueError(f'Prefecture {prefecture_name} is not valid.')

    minlat = float(match_df.iloc[0]['minlat'])
    maxlat = float(match_df.iloc[0]['maxlat'])
    minlon = float(match_df.iloc[0]['minlon'])
    maxlon = float(match_df.iloc[0]['maxlon'])

    return minlat, maxlat, minlon, maxlon


def lat2id(lat):
    return int((float(lat) - 34) * 3 / 2 + 51)


def lon2id(lon):
    return int(float(lon) - 100)
