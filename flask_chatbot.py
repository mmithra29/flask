from flask import Flask, request, jsonify #type:ignore
from pymongo import MongoClient#type:ignore
#tried to do a demo test for flask limiter by making a flask chatbot 
app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/trial2'
client = MongoClient(app.config['MONGO_URI'])
db = client.trial2

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data['message']
    response_message = f"You said: {user_message}" 
    
    # Log conversation in MongoDB
    db.conversations.insert_one({"user_message": user_message, "response_message": response_message})
    
    return jsonify({"response": response_message})

if __name__ == '__main__':
    app.run(debug=True)
