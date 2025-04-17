from flask import  request,  jsonify
from main import app 
from models.user import User 
from database.db_setup import db 


@app.route('/',methods = ['GET'])
def index():
 msg = {"success":"success"} 
 return jsonify(msg,200)

@app.route('/signup',methods = ['POST'])  

def signUp ():  
 


 try : 
   data = request.get_json()
   name = request.get('name')
   email = request.get('email')
   password = request.get('password')  
   newUser = User(name = name, email = email, password =password) 
   db.session.add(newUser) 
   db.session.commit()  
   return jsonify(
     {
       "status":200, 
       "msg" : "user criado com sucesso", 
        }
     ) 
 except Exception as e :  
   db.session.rollback()
   return jsonify(
      {
         "status":400, 
         "msg" : e, 
         }
      ) 

