#!/usr/bin/env python3
"""综合测试脚本，检查2048游戏的各种边界条件和潜在bug"""

from game import Game
import json

def test_game_over_detection():
    """测试游戏结束检测逻辑"""
    print("测试游戏结束检测...")
    print("="*50)
    
    game = Game()
    
    # 测试1：满格但还能合并的情况
    game.grid = [
        [2, 4, 8, 16],
        [4, 2, 16, 8],
        [8, 16, 2, 4],
        [16, 8, 4, 2]
    ]
    
    print("测试1：满格但相邻有相同数字（应该不是游戏结束）")
    print("Grid状态:")
    for row in game.grid:
        print(row)
    print(f"is_game_over(): {game.is_game_over()}")
    print(f"期望: False")
    
    # 测试2：真正的游戏结束状态
    game.grid = [
        [2, 4, 8, 16],
        [4, 8, 16, 32],
        [8, 16, 32, 64],
        [16, 32, 64, 128]
    ]
    
    print("\n测试2：满格且无法合并（真正的游戏结束）")
    print("Grid状态:")
    for row in game.grid:
        print(row)
    print(f"is_game_over(): {game.is_game_over()}")
    print(f"期望: True")

def test_win_condition():
    """测试胜利条件检测"""
    print("\n\n测试胜利条件检测...")
    print("="*50)
    
    game = Game()
    
    # 测试1：没有2048
    game.grid = [
        [1024, 512, 256, 128],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    
    print("测试1：最大值是1024")
    print(f"has_won(): {game.has_won()}")
    print(f"期望: False")
    
    # 测试2：有2048
    game.grid[0][0] = 2048
    print("\n测试2：有2048")
    print(f"has_won(): {game.has_won()}")
    print(f"期望: True")
    
    # 测试3：有大于2048的值
    game.grid[0][0] = 4096
    print("\n测试3：有4096")
    print(f"has_won(): {game.has_won()}")
    print(f"期望: True")

def test_move_when_no_change():
    """测试当移动不会改变棋盘时的行为"""
    print("\n\n测试无效移动...")
    print("="*50)
    
    game = Game()
    game.grid = [
        [2, 4, 8, 16],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    
    # 记录初始状态
    initial_grid = [row[:] for row in game.grid]
    
    # 移除自动添加新方块，以便观察
    game.add_new_tile = lambda: None
    
    print("初始状态（所有数字都在顶部）:")
    for row in game.grid:
        print(row)
    
    print("\n执行向上移动（应该不会改变棋盘）...")
    result = game.move('up')
    
    print("\n移动后的状态:")
    for row in game.grid:
        print(row)
    
    print(f"\n棋盘是否改变: {game.grid != initial_grid}")
    print("期望: False（棋盘不应该改变）")

def test_score_calculation():
    """测试分数计算是否正确"""
    print("\n\n测试分数计算...")
    print("="*50)
    
    game = Game()
    game.grid = [
        [2, 2, 4, 4],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    game.score = 0
    
    # 移除自动添加新方块
    game.add_new_tile = lambda: None
    
    print("初始状态:")
    print(f"Grid: {game.grid[0]}")
    print(f"初始分数: {game.score}")
    
    print("\n执行向左移动...")
    game.move('left')
    
    print(f"移动后Grid: {game.grid[0]}")
    print(f"分数: {game.score}")
    print(f"期望分数: 12 (4 + 8)")

def test_api_response_format():
    """测试get_game_state返回的格式"""
    print("\n\n测试API响应格式...")
    print("="*50)
    
    game = Game()
    state = game.get_game_state()
    
    print("检查返回的状态对象包含所有必需字段:")
    required_fields = ['grid', 'score', 'game_over', 'has_won']
    
    for field in required_fields:
        if field in state:
            print(f"✓ '{field}' 字段存在")
        else:
            print(f"✗ '{field}' 字段缺失")
    
    print(f"\n返回的状态对象: {json.dumps(state, indent=2)}")

if __name__ == "__main__":
    test_game_over_detection()
    test_win_condition()
    test_move_when_no_change()
    test_score_calculation()
    test_api_response_format()