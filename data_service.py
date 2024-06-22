from entity.model import CurrentSituation, SpecialFishery, User, Fishery, Notice, Slog, Fish
from utils.JsonUtils import get_class_list
from utils.SySQL import SQLManager


# 渔场特殊情况数据
def temp_fishery_data(fishery_name):
    sqlManager = SQLManager()
    data_sql = f"SELECT record_date, high_temp, low_temp FROM specialfishery WHERE fishery_name ='{fishery_name}' ORDER BY record_date DESC LIMIT 15"
    data = sqlManager.get_list(data_sql)
    x_data = [k['record_date'] for k in data]
    y1_data = [k['high_temp'] for k in data]
    y2_data = [k['low_temp'] for k in data]
    x_data.reverse()
    y1_data.reverse()
    y2_data.reverse()
    sqlManager.close()
    return {'x': x_data, 'high_temp_data': y1_data, 'low_temp_data': y2_data}


# 渔场特殊情况数据
def ph_fishery_data(fishery_name):
    sqlManager = SQLManager()
    data_sql = f"SELECT record_date,ph_value FROM specialfishery WHERE fishery_name ='{fishery_name}' ORDER BY record_date DESC LIMIT 15"
    data = sqlManager.get_list(data_sql)
    x_data = [k['record_date'] for k in data]
    y_data = [k['ph_value'] for k in data]
    x_data.reverse()
    y_data.reverse()
    sqlManager.close()
    return {'x': x_data, 'ph_value_data': y_data}


def oxygen_fishery_data(fishery_name):
    sqlManager = SQLManager()
    data_sql = f"SELECT record_date,dissolved_oxygen FROM specialfishery WHERE fishery_name ='{fishery_name}' ORDER BY record_date DESC LIMIT 15"
    data = sqlManager.get_list(data_sql)
    x_data = [k['record_date'] for k in data]
    y_data = [k['dissolved_oxygen'] for k in data]
    x_data.reverse()
    y_data.reverse()
    sqlManager.close()
    return {'x': x_data, 'dissolved_oxygen_data': y_data}


def turbidity_fishery_data(fishery_name):
    sqlManager = SQLManager()
    data_sql = f"SELECT record_date, turbidity FROM specialfishery WHERE fishery_name ='{fishery_name}' ORDER BY record_date DESC LIMIT 15"
    data = sqlManager.get_list(data_sql)
    x_data = [k['record_date'] for k in data]
    y_data = [k['turbidity'] for k in data]
    x_data.reverse()
    y_data.reverse()
    sqlManager.close()
    return {'x': x_data, 'turbidity_data': y_data}


def current_change_data(fishery_name):
    sqlManager = SQLManager()
    data_sql = f"SELECT record_date, record_time,water_temp,water_quality,ph_value,dissolved_oxygen,turbidity FROM currentsituation WHERE fishery_name ='{fishery_name}' ORDER BY record_date DESC LIMIT 15"
    data = sqlManager.get_list(data_sql)
    x_data = [str(k['record_date']) + ' ' + str(k['record_time']) for k in data]
    y1_data = [k['water_temp'] for k in data]
    y2_data = [k['water_quality'] for k in data]
    y3_data = [k['ph_value'] for k in data]
    y4_data = [k['dissolved_oxygen'] for k in data]
    y5_data = [k['turbidity'] for k in data]
    x_data.reverse()
    y1_data.reverse()
    y2_data.reverse()
    y3_data.reverse()
    y4_data.reverse()
    y5_data.reverse()
    sqlManager.close()
    return {'x': x_data, 'water_temp': y1_data, 'water_quality': y2_data,'ph_value': y3_data, 'dissolved_oxygen': y4_data, 'turbidity': y5_data}
# 首页数据
def top_page_data():
    sqlManager = SQLManager()
    key_sql = "SELECT water_quality, COUNT(id) AS n FROM currentsituation WHERE is_old=0 GROUP BY water_quality ORDER BY COUNT(id) DESC LIMIT 4"
    key_data = sqlManager.get_list(key_sql)
    num_data = [{k['water_quality']: k['n']} for k in key_data]
    table_sql = "SELECT * FROM currentsituation WHERE fishery_name IN ('北京渔场', '海淀渔场') AND is_old=0"
    table_data = sqlManager.get_list(table_sql)
    temp_top_sql = "SELECT fishery_name, water_temp FROM currentsituation WHERE is_old=0 ORDER BY water_temp DESC LIMIT 15"
    temp_list = sqlManager.get_list(temp_top_sql)
    temp_data = [{'fishery': i['fishery_name'], '温度': i['water_temp']} for i in temp_list]
    ph_top_sql = "SELECT fishery_name, ph_value FROM currentsituation WHERE is_old=0 ORDER BY ph_value DESC LIMIT 15"
    ph_list = sqlManager.get_list(ph_top_sql)
    ph_data = [{'fishery': i['fishery_name'], 'PH值': float(i['ph_value'])} for i in ph_list]
    oxygen_top_sql = "SELECT fishery_name, dissolved_oxygen FROM currentsituation WHERE is_old=0 ORDER BY dissolved_oxygen DESC LIMIT 15"
    oxygen_list = sqlManager.get_list(oxygen_top_sql)
    oxygen_data = [{'fishery': i['fishery_name'], '溶氧量': i['dissolved_oxygen']} for i in oxygen_list]
    sqlManager.close()
    return {'num_data': num_data, 'table_data': table_data, 'temp_data': temp_data, 'ph_data': ph_data, 'oxygen_data': oxygen_data}

B3 Modification in data_service.py
