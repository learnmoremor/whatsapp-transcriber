from flask import Flask , request

app = Flask(__name__)
@app.route('/whatsapp/incoming' , methods=['POST'])
def incoming_message():
    data = request.form
    print("Received whatsapp message:" , data)
    

    return "OK" , 200 

if __name__ == '__main__':
    app.run()
