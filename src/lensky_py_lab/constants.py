from enum import Enum


class Constants:
    default_date_field_name = 'DATE'
    default_timestamp_field_name = 'TS'
    hide_from_legend_suffix = '_Hidden'

    ims_rain_code_field_name = 'RAIN_CODE'
    ims_rainfall_field_name = 'RAINFALL'
    ims_temprature_field_name = 'TEMP'


class DataState(str, Enum):
    RAW = 'raw'
    FILTERED = 'filtered'
    CLEAN = 'clean'
    LOWESS = 'lowess'
