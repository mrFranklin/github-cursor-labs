from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Game state
class Game:
    def __init__(self):
        self.grid = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.add_new_tile()  # Add first tile during initialization
        self.add_new_tile()  # Add second tile during initialization
    
    def add_new_tile(self):
        """Add a new tile (2 with 90% probability, 4 with 10% probability) at a random empty cell."""
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.grid[i][j] == 0]
        if empty_cells:
            import random
            i, j = random.choice(empty_cells)
            self.grid[i][j] = 2 if random.random() < 0.9 else 4
    
    def move(self, direction):
        """根据指定方向移动和合并方块"""
        original_grid = [row[:] for row in self.grid]
        merged = [[False] * 4 for _ in range(4)]
        
        if direction in ['left', 'right']:
            for i in range(4):
                row = self.grid[i][:]
                if direction == 'right':
                    row.reverse()
                
                # Move and merge
                new_row = [0] * 4
                write_pos = 0
                for read_pos in range(4):
                    if row[read_pos] != 0:
                        if write_pos > 0 and new_row[write_pos-1] == row[read_pos] and not merged[i][write_pos-1]:
                            new_row[write_pos-1] *= 2
                            self.score += new_row[write_pos-1]
                            merged[i][write_pos-1] = True
                        else:
                            new_row[write_pos] = row[read_pos]
                            write_pos += 1
                
                if direction == 'right':
                    new_row.reverse()
                self.grid[i] = new_row
        
        elif direction in ['up', 'down']:
            for j in range(4):
                col = [self.grid[i][j] for i in range(4)]
                if direction == 'down':
                    col.reverse()
                
                # Move and merge
                new_col = [0] * 4
                write_pos = 0
                for read_pos in range(4):
                    if col[read_pos] != 0:
                        # 修正索引顺序，确保与merged初始化方式一致
                        if write_pos > 0 and new_col[write_pos-1] == col[read_pos] and not merged[write_pos-1][j]:
                            new_col[write_pos-1] *= 2
                            self.score += new_col[write_pos-1]
                            merged[write_pos-1][j] = True
                        else:
                            new_col[write_pos] = col[read_pos]
                            write_pos += 1
                
                if direction == 'down':
                    new_col.reverse()
                for i in range(4):
                    self.grid[i][j] = new_col[i]
        
        if self.grid != original_grid:
            self.add_new_tile()
        
        return self.get_game_state()
    
    def has_won(self):
        """检查是否达到胜利条件（存在值为2048或更高的方块）"""
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] >= 2048:
                    return True
        return False
    
    def get_game_state(self):
        """获取当前游戏状态，包括网格、分数、游戏结束和胜利状态"""
        return {
            'grid': self.grid,
            'score': self.score,
            'game_over': self.is_game_over(),
            'has_won': self.has_won()
        }
    
    def is_game_over(self):
        """检查游戏是否结束（没有空格且无法合并）"""
        # Check for empty cells
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] == 0:
                    return False
        
        # Check for possible merges
        for i in range(4):
            for j in range(4):
                current = self.grid[i][j]
                # Check right
                if j < 3 and current == self.grid[i][j+1]:
                    return False
                # Check down
                if i < 3 and current == self.grid[i+1][j]:
                    return False
        
        return True

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

@app.route('/move', methods=['POST'])
def move():
    """处理移动请求并返回更新后的游戏状态"""
    try:
        direction = request.json.get('direction')
        if direction not in ['up', 'down', 'left', 'right']:
            return jsonify({'error': 'Invalid direction'}), 400
        
        return jsonify(game.move(direction))
    except Exception as e:
        app.logger.error(f"Error processing move: {str(e)}")
        return jsonify({'error': 'Failed to process move'}), 500

if __name__ == '__main__':
    app.run(debug=True)
