# app/routes.py
from flask import Blueprint, jsonify, request
from app.apiDengue import fetch_and_store_data

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
