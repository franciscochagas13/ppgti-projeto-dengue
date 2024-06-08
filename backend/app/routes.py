# app/routes.py
from flask import Blueprint, jsonify, request
from app.apiDengue import fetch_and_store_data
from app.database_queries import query_total_cases, query_cases_by_city,query_cases_by_month, query_scatter_temp_humidity_cases
from app import db

bp = Blueprint('routes', __name__)

@bp.route('/data', methods=['GET'])
def get_data():
    # Recuperar parâmetros da URL
    ew_start = request.args.get('ew_start')
    ew_end = request.args.get('ew_end')
    ey_start = request.args.get('ey_start')
    ey_end = request.args.get('ey_end')

    if not all([ew_start, ew_end, ey_start, ey_end]):
        return jsonify({"error": "Missing required parameters"}), 400

    try:
        fetch_and_store_data(ew_start, ew_end, ey_start, ey_end)
        return jsonify({"message": "Data fetched and stored successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('/api/total-cases', methods=['GET'])
def get_total_cases():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    if not all([start_date, end_date]):
        return jsonify({"error": "Missing required parameters"}), 400
    
    total_cases = query_total_cases(start_date,end_date)
    
    if total_cases.alive:  # Verifica se há resultados
        result = total_cases.next()
    else:
        result = {"total_cases": 0}
    
    return jsonify(result)

@bp.route('/api/cases-by-city', methods=['GET'])
def get_cases_by_city():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    if not all([start_date, end_date]):
        return jsonify({"error": "Missing required parameters"}), 400
    
    cases_by_city = query_cases_by_city(start_date,end_date)
    
    result = [{"geocode": case["_id"], "city_name": case["city_name"], "total_cases": case["total_cases"]} for case in cases_by_city]
    return jsonify(result)

@bp.route('/api/cases-by-month', methods=['GET'])
def get_cases_by_month():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if not all([start_date, end_date]):
        return jsonify({"error": "Missing required parameters"}), 400
    
    cases_by_month = query_cases_by_month(start_date,end_date)
    
    result = [{"year": int(case["_id"][:4]), "month": int(case["_id"][5:7]), "total_cases": case["total_casos"]} for case in cases_by_month]
    return jsonify(result)

@bp.route('/api/scatter-temp-humidity-cases', methods=['GET'])
def get_scatter_temp_humidity_cases():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    if not all([start_date, end_date]):
        return jsonify({"error": "Missing required parameters"}), 400
      
    data = query_scatter_temp_humidity_cases(start_date,end_date)

    scatter_data = [{"temperatura": d["_id"]["temperatura"], "umidade": d["_id"]["umidade"], "casos": d["casos"]} for d in data]
    return jsonify(scatter_data)