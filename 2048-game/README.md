# 2048 Game

一个使用Flask和Python实现的2048游戏。

## 项目结构

```
2048-game/
├── app.py              # Flask应用主文件
├── game.py             # 游戏逻辑实现
├── requirements.txt    # Python依赖
├── templates/
│   └── index.html      # 游戏前端界面
└── tests/              # 测试文件
    ├── test_bug.py
    ├── test_bug_detailed.py
    ├── test_comprehensive.py
    └── test_game_over_fix.py
```

## Bug修复

已修复的主要bug：
- **垂直移动时的合并逻辑错误**：修复了在处理up/down移动时merged数组索引不正确的问题

详细信息请查看 `/workspace/bug_report.md`

## 安装和运行

1. 创建虚拟环境（推荐）：
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 运行应用：
```bash
python app.py
```

4. 在浏览器中访问 `http://localhost:5000`

## 游戏玩法

- 使用方向键（↑↓←→）移动方块
- 相同数字的方块碰撞时会合并
- 目标是创造出2048方块
- 当无法移动时游戏结束

## 运行测试

```bash
cd tests
python test_comprehensive.py  # 运行综合测试
```