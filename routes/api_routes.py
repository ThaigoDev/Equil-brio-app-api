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
   name = request.form.get('name')
   email = request.form.get('email')
   password = request.form.get('password')  
   newUser = User(name = name, email = email, password =password) 
   db.session.add(newUser) 
   db.session.commit()  
   return jsonify(
     {
       "status":200, 
       "msg" : "User criado com sucesso!",  
       "autorized" : True 
        }
     ) 
 except Exception as e :  
   db.session.rollback()
   return jsonify(
      {
         "status":400, 
         "msg" : str(e), 
         }
      ) 

@app.route("/users/all",methods = ['GET']) 
def getAllUsers() : 
 allUsers =  User.query.all()   
 result = []
 for user in allUsers : 
  result.append({
   "id": user.id,
   "name": user.name,
   "email": user.email,
   "password": user.password,
  })
 return jsonify(
  {
    "users" :  result
  }
  )