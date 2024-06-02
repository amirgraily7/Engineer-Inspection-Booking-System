from flask import Flask, jsonify, request
import mysql.connector
import json

app = Flask(__name__)

# Database configuration
db_config = {
    'user': 'admin',
    'password': 'mjafarnia66',
    'host': '127.0.0.1',
    'database': 'engineerinspection',
    'raise_on_warnings': True
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/engineer/<engineer_id>', methods=['GET'])
def get_engineer_availability(engineer_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = '''
        SELECT engineer_id, available_day, slot_09_00, slot_09_30, slot_10_00, slot_10_30, slot_11_00, slot_11_30, 
               slot_12_00, slot_12_30, slot_13_00, slot_13_30, slot_14_00, slot_14_30, slot_15_00, slot_15_30, 
               slot_16_00, slot_16_30, updated_timestamp 
        FROM engineers 
        WHERE engineer_id = %s
    '''
    cursor.execute(query, (engineer_id,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(result)

@app.route('/bookings', methods=['GET'])
def get_bookings_summary():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = '''
        SELECT inspection_id, inspection_date, start_time, end_time, engineer_id 
        FROM inspections
    '''
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(result)

@app.route('/')
def index():
    return "Welcome to the Engineer Inspection Booking API!"

if __name__ == '__main__':
    app.run(debug=True)
