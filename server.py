from flask import Flask, jsonify, request, session
from flask_socketio import SocketIO, emit,send
from chessEval import ChessGame
import json
from flask_cors import CORS, cross_origin
app = Flask(__name__)
app.config['CORS_HEADER'] = 'aplication/json'
# app.config['SECERT_KEY'] = 'secret'
cors = CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app,cors_allowed_origins="*")



@cross_origin()
@app.route("/getTheGame")
def getTheGame():
    print(session)
    chessGame = ChessGame()
    # print(chessGame)
    return {"data":str(chessGame.game)}

@cross_origin()
@app.route("/startGame", methods = ['POST'])
def startGame():
    if request.method == 'POST':
        chessGame = ChessGame()
        chessGame.startNewGame()
        print(chessGame.game)
    return {"data":str(chessGame.game)}

@cross_origin()
@app.route("/makemove", methods = ['GET','POST'])
def makeAMove():
    # move = request.args.get('move')
    if request.method =="POST":
        data = request.get_json()
        chess = ChessGame()
        print(data['move'])
        try:
            chess.makeMove(data['move'])
            return {"data":str(chess.game)}
        except:
            return {"data":str(chess.game)}
    #     print(request.form['move'])
    # return ""

@cross_origin()
@socketio.on('makeAMove')
def test_connection(data):
    print(data)
    chess = ChessGame()
    # print(data['move'])
    # emit('response':str(chess.game))
    print(chess.game)
    try:
        chess.makeMove(data)
        emit('move',{'data':str(chess.game)}, broadcast = True)
    except:
        emit('move',{'data':str(chess.game)}, broadcast = True)
    # emit('connect',{"data":"lets dance"})
    return {"data":"success"}


@socketio.on('connect')
@cross_origin()
def test_connect():
    emit('after connect',  {'data':'Lets dance'})
    return {"data":"hi"}


@cross_origin()
@app.route("/")
def mainFunc():
    return "<div> hi</div>"

if __name__== '__main__':
    socketio.run(app, host='0.0.0.0')