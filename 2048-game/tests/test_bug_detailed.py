#!/usr/bin/env python3
"""详细测试脚本，展示2048游戏中的merged数组索引bug"""

from game import Game

def test_merged_index_bug():
    """测试merged数组索引bug"""
    print("测试merged数组索引bug...")
    print("="*50)
    
    game = Game()
    
    # 设置一个会触发问题的场景
    # 在向下移动时，如果有多个连续相同的数字，应该只合并一次
    game.grid = [
        [2, 0, 0, 0],
        [2, 0, 0, 0],
        [2, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    
    print("测试场景: 三个连续的2")
    print("初始状态:")
    for i, row in enumerate(game.grid):
        print(f"Row {i}: {row}")
    
    # 移除自动添加新方块的功能，以便更清楚地看到合并结果
    original_add_new_tile = game.add_new_tile
    game.add_new_tile = lambda: None
    
    print("\n执行向下移动...")
    print("期望结果: 前两个2合并成4，第三个2保持不变")
    print("期望状态应该是: [0,0,0,0], [0,0,0,0], [2,0,0,0], [4,0,0,0]")
    
    game.move('down')
    
    print("\n实际结果:")
    for i, row in enumerate(game.grid):
        print(f"Row {i}: {row}")
    
    # 恢复add_new_tile
    game.add_new_tile = original_add_new_tile
    
    # 测试更复杂的场景
    print("\n" + "="*50)
    print("测试更复杂的场景：多列都有数字")
    
    game.grid = [
        [2, 4, 2, 2],
        [2, 4, 2, 2],
        [2, 0, 2, 2],
        [0, 0, 0, 0]
    ]
    
    print("初始状态:")
    for i, row in enumerate(game.grid):
        print(f"Row {i}: {row}")
    
    # 再次移除自动添加新方块
    game.add_new_tile = lambda: None
    
    print("\n执行向下移动...")
    game.move('down')
    
    print("\n实际结果:")
    for i, row in enumerate(game.grid):
        print(f"Row {i}: {row}")
    
    # 测试IndexError的可能性
    print("\n" + "="*50)
    print("测试可能的IndexError...")
    
    # 这个测试会尝试触发索引越界错误
    game.grid = [
        [0, 0, 0, 2],
        [0, 0, 0, 2],
        [0, 0, 0, 2],
        [0, 0, 0, 2]
    ]
    
    print("初始状态（最右列全是2）:")
    for i, row in enumerate(game.grid):
        print(f"Row {i}: {row}")
    
    try:
        print("\n执行向下移动...")
        game.move('down')
        print("\n移动成功，结果:")
        for i, row in enumerate(game.grid):
            print(f"Row {i}: {row}")
    except IndexError as e:
        print(f"\n发生IndexError: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_merged_index_bug()