from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/update_excel', methods=['POST'])
def update_excel():
    data = request.json['data']
    print("Received data:", data)
    
    # Assuming 'data' contains your updated data in JSON format
    
    # Here you'll write code to update your Excel file on your local machine
    # Example:
    with open('C:\\Users\\Anjali Shukla\\Desktop\\Excelll.xlsx', 'w') as f:
        f.write(data)
    
    return 'Excel file updated successfully!'

@app.route('/')
def index():
    print("Hello from index route")
    return 'This is the index route.'

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app
