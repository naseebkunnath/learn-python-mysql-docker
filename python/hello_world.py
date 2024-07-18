from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
mysql_config = {
    'user': 'root',
    'password': 'root',
    'host': 'mysql',
    'port': 3306,
    'database': 'db'
}

# Route to fetch students data
@app.route('/students', methods=['GET'])
def get_students():
    try:
        connection = mysql.connector.connect(**mysql_config)
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()

        cursor.close()
        connection.close()

        # Convert tuple results to a list of dictionaries (JSON serializable format)
        students_list = []
        for student in students:
            student_dict = {
                'id': student[0],
                'name': student[1],
                'age': student[2]
                # Add more fields as needed
            }
            students_list.append(student_dict)

        return jsonify(students_list)

    except mysql.connector.Error as err:
        return jsonify({'error': f'Database error: {err}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
