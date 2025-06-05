#!/usr/bin/env python3
"""测试脚本，用于验证2048游戏中的bug"""

from game import Game

def test_vertical_merge_bug():
    """测试垂直移动时的合并bug"""
    print("测试垂直移动的合并bug...")
    
    # 创建游戏实例
    game = Game()
    
    # 手动设置一个特定的游戏状态来测试
    # 设置一个可以触发bug的场景
    game.grid = [
        [2, 0, 0, 0],
        [2, 0, 0, 0],
        [4, 0, 0, 0],
        [4, 0, 0, 0]
    ]
    
    print("初始状态:")
    for row in game.grid:
        print(row)
    
    # 测试向下移动
    print("\n执行向下移动...")
    try:
        game.move('down')
        print("移动后的状态:")
        for row in game.grid:
            print(row)
    except Exception as e:
        print(f"错误: {e}")
        import traceback
        traceback.print_exc()
    
    # 再次测试向上移动
    game.grid = [
        [2, 0, 0, 0],
        [2, 0, 0, 0],
        [4, 0, 0, 0],
        [4, 0, 0, 0]
    ]
    
    print("\n\n重置状态并测试向上移动...")
    print("初始状态:")
    for row in game.grid:
        print(row)
    
    print("\n执行向上移动...")
    try:
        game.move('up')
        print("移动后的状态:")
        for row in game.grid:
            print(row)
    except Exception as e:
        print(f"错误: {e}")
        import traceback
        traceback.print_exc()

def test_horizontal_merge():
    """测试水平移动的合并"""
    print("\n\n测试水平移动的合并...")
    
    game = Game()
    game.grid = [
        [2, 2, 4, 4],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    
    print("初始状态:")
    for row in game.grid:
        print(row)
    
    print("\n执行向左移动...")
    game.move('left')
    print("移动后的状态:")
    for row in game.grid:
        print(row)

if __name__ == "__main__":
    test_vertical_merge_bug()
    test_horizontal_merge()