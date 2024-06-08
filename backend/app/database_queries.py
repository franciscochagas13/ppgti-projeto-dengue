from app import db


def query_total_cases(start_date,end_date):
    
    return db.dengue_data.aggregate([
        {"$match": {"start_data": {"$gte": start_date, "$lte": end_date}}},
        {"$group": {"_id": None, "total_cases": {"$sum": "$casos"}}}
    ])
    
def query_cases_by_city(start_date,end_date):
    
   return db.dengue_data.aggregate([
        {"$match": {"start_data": {"$gte": start_date, "$lte": end_date}}},
        {"$group": {"_id": "$geocode", "total_cases": {"$sum": "$casos"}, "city_name": {"$first": "$name_city"}}}
    ])
   
def query_cases_by_month(start_date,end_date):
    return db.dengue_data.aggregate([
        {"$match": {"start_data": {"$gte": start_date,"$lte": end_date}}},
        {"$group": {"_id": { "$substr": ["$start_data", 0, 7] },"total_casos": { "$sum": "$casos" }}},
        {"$sort": {"_id": 1}}
    ])

def query_scatter_temp_humidity_cases(start_date,end_date):
    return  db.dengue_data.aggregate([
        {
            "$match": {
                "start_data": {"$gte": start_date, "$lte": end_date},
                "tempmin": {"$exists": True},
                "umidmin": {"$exists": True},
                "casos": {"$exists": True}
            }
        },
        {
            "$group": {
                "_id": {
                    "temperatura": "$tempmin",
                    "umidade": "$umidmin"
                },
                "casos": {"$sum": "$casos"}
            }
        }
    ])