#Versiones
#Python 3.10.1
#Flask 2.0.2



from flask import Flask, jsonify, json


app = Flask(__name__)


albums = []
comments = []
users = []


def data_load():
    global albums
    global comments
    global users
    with open('albums.json') as content:
        albums = json.load(content)
    with open('comments.json') as content:
        comments = json.load(content)
    with open('users.json') as content:
        users = json.load(content)




#●	Todos los comentarios disponibles
@app.route('/comments')
def com () :
    return jsonify({'comments' : comments})


# ●	Dado un id de posteo, retornar todos los comentarios relacionados a dicho posteo.
@app.route('/comments/<string:postId>')
def getComentsById(postId):
    try:
        postId = int(postId)
        commentsFounds = [comment for comment in comments if comment['postId'] == postId]
        if len(commentsFounds) > 0:
            return jsonify({'comments' : commentsFounds})
        return jsonify({'message' : 'Usuario sin comentarios o el usuario no existe'})
    except:
        return jsonify({'message' : 'No ha ingresado un numero valido'})


#●	Retornar el posteo con mayor cantidad de comentarios asociados. 
# Si existe más de uno, devolverlos todos.
@app.route('/comments/postMax')
def getPostByMaxComments():

    post_comments = {}
    for comment in comments:
        postId = comment['postId']
        if ('postID_' + str(postId)) in post_comments:
            post_comments['postID_' + str(postId)] += 1
        else:
            post_comments['postID_' + str(postId)] = 1

    maximoComentarios = max(post_comments.values())

    resultado = {}
    for pC in post_comments:
        if post_comments[pC] == maximoComentarios:
            resultado[pC] = post_comments[pC]

    return jsonify({'maxComments': resultado})
    
    
#●	Dado un id de usuario, devolver los álbumes que tiene asociado.
@app.route('/albums/<string:id>')
def getAlbumsByUser(id):
    try:
        id = int(id)
        resultado = []
        for yuyu in albums:
            if yuyu['userId'] == id:
                resultado.append(yuyu)
        # print(resultado)
        if len(resultado) > 0:
            print('hola')
            return jsonify({'albums' : resultado})
        return jsonify({'message' : 'El id de usuario no tiene ningun album asociado o no existe'})    
    except: 
        return jsonify({'message' : 'No ha ingresado un numero valido'})
            





if __name__ == '__main__':
    data_load()
    app.run()