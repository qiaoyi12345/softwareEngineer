from entity.model import CurrentSituation, SpecialFishery, User, Fishery, Notice, Slog, Fish
from utils.JsonUtils import get_class_one, get_class_list
from utils.PageUtils import get_page_start, PageData
from utils.Result import Result
from utils.SySQL import SQLManager


# 根据ID查询数据
def select_fishery_history_by_id(id):
    sql = "SELECT * FROM specialfishery WHERE id=%s"
    sqlManager = SQLManager()
    data = sqlManager.get_one(sql, id)
    fishery_history = get_class_one(data, SpecialFishery)
    sqlManager.close()
    return fishery_history


def select_fishery_history_list(page, limit, where):
    page, limit, where = get_page_start(int(page), int(limit), where)
    params_sql = get_search_params(where)
    data_sql = "SELECT * FROM specialfishery WHERE 1=1 " + params_sql + " ORDER BY id DESC LIMIT %s,%s"
    count_sql = "SELECT COUNT(id) as i FROM specialfishery WHERE 1=1 " + params_sql
    sqlManager = SQLManager()
    data = sqlManager.get_list(data_sql, (page, limit))  # 获取分页数据
    count = sqlManager.get_one(count_sql)['i']  # 获取数据总数
    fishery_history = get_class_list(data, SpecialFishery)
    page_result = PageData(count, fishery_history)
    return page_result


# 查询条件处理
def get_search_params(where):
    sql = ''
    if where:
        if where['fishery_name'] and len(where['fishery_name']) > 0:
            sql = sql + " AND fishery_name like '%%" + where['fishery_name'] + "%%' "
        if where['record_date'] and len(where['record_date']) > 0:
            sql = sql + " AND record_date = '" + where['record_date'] + "' "
    return sql


# 获取渔场名称列表
def get_fishery_list():
    sql = "SELECT fishery_name FROM specialfishery GROUP BY fishery_name"
    sqlManager = SQLManager()
    fishery_list = []
    data = sqlManager.get_list(sql)
    for i in data:
        fishery_list.append(i['fishery_name'])
    sqlManager.close()
    return fishery_list


def get_fish_list():
    sql = "SELECT fish_name FROM specialfishery GROUP BY fish_name"
    sqlManager = SQLManager()
    fish_list = []
    data = sqlManager.get_list(sql)
    for i in data:
        fish_list.append(i['fish_name'])
    sqlManager.close()
    return fish_list


# 插入渔场历史数据
def insert_fishery_history(data):
    sqlManager = SQLManager()
    check_sql = "SELECT COUNT(id) as `i` FROM `specialfishery` WHERE fishery_name=%s AND record_date=%s"
    count = sqlManager.get_one(check_sql, (data['fishery_name'], data['record_date']))['i']
    if count > 0:
        return Result(False, "数据重复")
    sql = "INSERT INTO specialfishery (fishery_name, record_date, high_temp, low_temp, ph_value, dissolved_oxygen, turbidity, fish_name) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    sqlManager.instert(sql, (
        data['fishery_name'], data['record_date'], data['high_temp'], data['low_temp'], data['ph_value'], data['dissolved_oxygen'], data['turbidity'], data['fish_name']))
    sqlManager.close()
    return Result(True, "添加成功")


# 修改渔场历史数据
def edit_fishery_history(data):
    sqlManager = SQLManager()
    sql = "UPDATE specialfishery SET high_temp=%s, low_temp=%s, ph_value=%s, dissolved_oxygen=%s, turbidity=%s, fish_name=%s WHERE id=%s"
    sqlManager.moddify(sql, (data['high_temp'], data['low_temp'], data['ph_value'], data['dissolved_oxygen'], data['turbidity'], data['fish_name'], data['id']))
    sqlManager.close()
    return Result(True, "修改成功")


# 删除渔场历史数据
def del_fishery_history(id):
    sqlManager = SQLManager()
    sql = "DELETE FROM specialfishery WHERE id=%s"
    sqlManager.moddify(sql, id)
    sqlManager.close()
    return Result(True, "删除成功")


# 批量删除渔场历史数据
def del_fishery_history_list(ids):
    sqlManager = SQLManager()
    sql = "DELETE FROM specialfishery WHERE id IN (" + ids + ")"
    sqlManager.moddify(sql)
    sqlManager.close()
    return Result(True, "删除成功")


def get_fishery_history(id):
    sqlManager = SQLManager()
    sql = "SELECT * FROM `specialfishery` WHERE id=%s"
    data = sqlManager.get_one(sql, id)
    sqlManager.close()
    return data
