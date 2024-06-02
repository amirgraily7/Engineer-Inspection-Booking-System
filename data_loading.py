import json
import mysql.connector
from datetime import datetime


def load_data_to_db(engineer_file, inspection_file, db_config):
    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Load and process engineer availability data
    with open(engineer_file, 'r') as f:
        engineer_data = json.load(f)
        for record in engineer_data:
            engineer_id = record['engineer_id']
            available_day = record['available_day']
            available_slots = record['slots']
            updated_timestamp = record['updated_timestamp']
            updated_timestamp = datetime.strptime(updated_timestamp, '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S')

            # Convert binary string to individual slots
            slots = [int(bit) for bit in available_slots]
            
            query = '''
                INSERT INTO engineers (engineer_id, available_day, slot_09_00, slot_09_30, slot_10_00, slot_10_30, slot_11_00, slot_11_30, 
                                       slot_12_00, slot_12_30, slot_13_00, slot_13_30, slot_14_00, slot_14_30, slot_15_00, slot_15_30, 
                                       slot_16_00, slot_16_30, updated_timestamp)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''
            cursor.execute(query, [engineer_id, available_day] + slots + [updated_timestamp])
    
    # Load and process booked inspections data
    with open(inspection_file, 'r') as f:
        inspection_data = json.load(f)
        for record in inspection_data:
            inspection_id = record['inspection_id']
            inspection_date = record['inspection_date']
            start_time = record['start_time']
            end_time = record['end_time']
            # Assume we can infer engineer_id from other logic or data
            engineer_id = record['engineer_id']
            
            query = '''
                INSERT INTO inspections (inspection_id, inspection_date, start_time, end_time, engineer_id)
                VALUES (%s, %s, %s, %s, %s)
            '''
            cursor.execute(query, [inspection_id, inspection_date, start_time, end_time, engineer_id])

    conn.commit()
    cursor.close()
    conn.close()


engineer_file = r'C:\Users\amirg\Desktop\position interview\engineer_avail.json'
inspection_file = r'C:\Users\amirg\Desktop\position interview\inspection_records.json'
db_config = {
  'user': 'admin',
  'password': 'mjafarnia66',
  'host': '127.0.0.1',
  'database': 'engineerinspection',
  'raise_on_warnings': True
}
load_data_to_db(engineer_file, inspection_file, db_config)