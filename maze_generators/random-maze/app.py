from flask import Flask, jsonify, request
from .random_mg import RandomMazeGenerator

app = Flask(__name__)

height = 7
width = 7

@app.route('/generate', methods=["GET"])
def GET_maze_segment():
    maze = RandomMazeGenerator(height, width).create()
    print("Hello")
    maze = maze.add_boundary()
    response = jsonify({"geom": maze.encode()})
    response.headers["Cache-Control"] = 'no-store'
    return response, 200
