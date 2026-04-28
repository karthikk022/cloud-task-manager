import os
import boto3
from flask import Flask, request, jsonify
from botocore.exceptions import ClientError

app = Flask(__name__)

# Configuration for LocalStack
DYNAMODB_ENDPOINT = os.getenv("DYNAMODB_ENDPOINT", "http://localhost:4566")
REGION = os.getenv("AWS_REGION", "us-east-1")

dynamodb = boto3.resource('dynamodb', endpoint_url=DYNAMODB_ENDPOINT, region_name=REGION)
table = dynamodb.Table('Tasks')

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task_id = data.get('id')
    title = data.get('title')
    
    try:
        table.put_item(Item={'id': task_id, 'title': title, 'status': 'PENDING'})
        return jsonify({"message": "Task created", "id": task_id}), 201
    except ClientError as e:
        return jsonify({"error": str(e)}), 500

@app.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    try:
        response = table.get_item(Key={'id': task_id})
        if 'Item' in response:
            return jsonify(response['Item']), 200
        return jsonify({"error": "Task not found"}), 404
    except ClientError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
