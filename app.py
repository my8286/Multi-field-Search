from flask import Flask, jsonify
from csv import reader

app = Flask(__name__)

# Render home page endpoint
@app.route('/home')
def home():
    return "hello world"

#Data preprocessing endpoint
@app.route('/data')
def data():
    result=[]
    mydict={}
    with open('data.csv',encoding="utf8") as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)

        count=0
        for row in list_of_rows:
            new_row=row[0:5]
            new_row.append(str(count))
            count=count+1
            result.append(new_row)
    # make dictionary for json format
    mydict["data"]=result[1:]
    return jsonify(mydict)

if __name__== '__main__':
    app.run(debug=True)