# pairwise-lightprobe-tetra-leak

## 领域

游戏、图形与多媒体

## 主题

光照探针四面体插值

## 说明

完整四面体权重、版本回读与越界钳制。

初始状态下 `graphics/lightprobe_tetra_leak.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
