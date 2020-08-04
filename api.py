#  Lucas Uesato
# 
from flask import Flask , jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'newsdb'
app.config['MONGO_URI'] = 'mongodb+srv://apiTest:743xBtWtHSFLtSCC@cluster0-fcpmn.gcp.mongodb.net/newsdb?retryWrites=true&w=majority'

mongo = PyMongo(app)
# GET ALL NOTICIAS
@app.route('/news', methods=['GET'])
def get_all_news():
    new = mongo.db.news
    output = []
    for n in new.find():
      print(n)
      output.append({'Title' : n['Title'], 'Text' : n['Text'], "Author" : n["Author"]})
    return jsonify({'result': output}) 

# GET NOTICIA FILTRA 1 por titulo
@app.route('/news/', methods=['GET'])
def get_new():
    title = request.args.get('title')
    new = mongo.db.news
    n = new.find_one({'Title' : title})
    if n:
      output = {'Title' : n['Title'], 'Text' : n['Text'], "Author" : n["Author"]} 
    else:
      output =   "No such name"
    return jsonify({'result' : output})

# POST Insert Noticia
@app.route('/news',methods=['POST'])
def post_news() :
  new =  mongo.db.news
  title = request.json['title']
  text = request.json['text']
  author = request.json['author']

  new_id = new.insert({'Title' : title, 'Text' : text, "Author" : author})

  n = new.find_one({'_id': new_id })
  output = {'id':str(n['_id']),'Title' : n['Title'], 'Text' : n['Text'], "Author" : n["Author"]}
  return jsonify({'result' : output})

# PATCH Update noticia
@app.route('/news',methods=['PATCH'])
def update_news() :
  new =  mongo.db.news
  title = request.json['title']
  text = request.json['text']
  author = request.json['author']
  id_new = request.json['id']

  n = new.find_one_and_update({'_id' : ObjectId(id_new)},{'$set' : {'Title' : title, 'Text' : text, "Author" : author}})

  output = {'id':str(n['_id']),'Title' : n['Title'], 'Text' : n['Text'], "Author" : n["Author"]}
  
  return jsonify({'Objeto atualizado' : output})  

# Post DELETE noticia
@app.route('/news/',methods=['DELETE'])
def delete_news() :
  new =  mongo.db.news
  id_delete = request.args.get('id')

  n = new.find_one_and_delete({'_id' : ObjectId(id_delete)})
  
  return jsonify({'Obj deletado' : str(n)})  




