#!/usr/bin/env python3
"""修正的游戏结束检测测试"""

from game import Game

def test_game_over_with_correct_cases():
    """使用正确的测试案例测试游戏结束检测"""
    print("测试游戏结束检测（修正版）...")
    print("="*50)
    
    game = Game()
    
    # 测试1：满格但有相邻相同数字（游戏未结束）
    game.grid = [
        [2, 2, 8, 16],  # 第一行有两个相邻的2
        [4, 8, 16, 8],
        [8, 16, 2, 4],
        [16, 8, 4, 128]
    ]
    
    print("测试1：满格但第一行有相邻的2（应该不是游戏结束）")
    print("Grid状态:")
    for row in game.grid:
        print(row)
    print(f"is_game_over(): {game.is_game_over()}")
    print(f"期望: False ✓" if not game.is_game_over() else "期望: False ✗")
    
    # 测试2：满格但有垂直相邻相同数字
    game.grid = [
        [2, 4, 8, 16],
        [4, 8, 16, 32],
        [4, 16, 32, 64],  # 第一列有两个相邻的4
        [16, 32, 64, 128]
    ]
    
    print("\n测试2：满格但第一列有相邻的4（应该不是游戏结束）")
    print("Grid状态:")
    for row in game.grid:
        print(row)
    print(f"is_game_over(): {game.is_game_over()}")
    print(f"期望: False ✓" if not game.is_game_over() else "期望: False ✗")
    
    # 测试3：真正的游戏结束状态
    game.grid = [
        [2, 4, 8, 16],
        [4, 8, 16, 32],
        [8, 16, 32, 64],
        [16, 32, 64, 128]
    ]
    
    print("\n测试3：满格且无法合并（真正的游戏结束）")
    print("Grid状态:")
    for row in game.grid:
        print(row)
    print(f"is_game_over(): {game.is_game_over()}")
    print(f"期望: True ✓" if game.is_game_over() else "期望: True ✗")
    
    # 测试4：有空格的情况
    game.grid = [
        [2, 4, 8, 16],
        [4, 8, 16, 32],
        [8, 16, 32, 64],
        [16, 32, 0, 128]  # 有一个空格
    ]
    
    print("\n测试4：有空格（游戏未结束）")
    print("Grid状态:")
    for row in game.grid:
        print(row)
    print(f"is_game_over(): {game.is_game_over()}")
    print(f"期望: False ✓" if not game.is_game_over() else "期望: False ✗")

if __name__ == "__main__":
    test_game_over_with_correct_cases()