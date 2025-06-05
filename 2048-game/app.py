from flask import Flask, render_template, jsonify, request
from game import Game

app = Flask(__name__)
# Game instance
game = Game()

@app.route('/')
def index():
    """渲染游戏主页"""
    return render_template('index.html')

@app.route('/new_game', methods=['POST'])
def new_game():
    """创建新游戏并返回初始游戏状态"""
    global game
    try:
        game = Game()
        return jsonify(game.get_game_state())
    except Exception as e:
        app.logger.error(f"Error creating new game: {str(e)}")
        return jsonify({'error': 'Failed to create new game'}), 500

@app.route('/jump', methods=['POST'])
def jump():
    """处理移动请求并返回更新后的游戏状态"""
    try:
        direction = request.json.get('direction')
        if direction not in ['up', 'down', 'left', 'right']:
            return jsonify({'error': 'Invalid direction'}), 400
        
        return jsonify(game.jump(direction))
    except Exception as e:
        app.logger.error(f"Error processing jump: {str(e)}")
        return jsonify({'error': 'Failed to process jump'}), 500

if __name__ == '__main__':
    app.run(debug=True)
