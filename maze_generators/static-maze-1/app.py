from flask import Flask, jsonify
import os
import sys
import inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
parent_dir = os.path.dirname(parent_dir)
sys.path.insert(0, parent_dir)

from maze import *

app = Flask(__name__)

@app.route('/generate', methods=["GET"])
def GET_maze_segment():
    maze = Maze(3, 3)
    maze = maze.add_boundary().expand_maze_with_blank_space(maze.height + 2, maze.width + 2)
    maze = maze.add_boundary().expand_maze_with_blank_space(maze.height + 2, maze.width + 2)
    maze = maze.add_boundary()

    response = jsonify({"geom": maze.encode()})
    response.headers["Cache-Control"] = f"public,max-age={365*24*60*60}"
    response.headers["Age"] = 0
    return response, 200
