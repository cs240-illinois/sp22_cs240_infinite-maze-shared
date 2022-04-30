from flask import Flask, jsonify
from .random_mg import RandomMazeGenerator
from random import randint

app = Flask(__name__)

min_size = 4
max_size = 7


@app.route('/generate', methods=["GET"])
def GET_maze_segment():
    height = randint(min_size, max_size)
    width = randint(min_size, max_size)

    maze = RandomMazeGenerator(height, width).create()
    print(f"height:{height}, width:{width}")

    response = jsonify({"geom": maze.encode()})
    response.headers["Cache-Control"] = 'no-store'

    return response, 200
