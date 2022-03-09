from flask import Flask,jsonify,request

app=Flask(__name__)

stores={}

@app.route('/')
def home():
    return 'hey'

@app.route('/store',methods=['POST'])
def create_store():
    req_data=request.get_json()
    new_store={
        'name':req_data['name'],
        items:[]
    }
    stores.append(new_store)
    return jsonify(new_store)


if __name__ == '__main__':
    app.run(debug=True)