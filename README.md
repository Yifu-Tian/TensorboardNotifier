# Tensorboard Notifier

**Tensorboard Notifier** 是一个基于 **TensorBoard 日志** 的训练监控工具，能够自动获取 Loss 曲线，并通过 **Server酱** API将Loss曲线图像推送到微信

---
## Quick Start

```bash
git clone https://github.com/yourname/train_notifier.git
cd train_notifier
pip install -e .
```

## Features

- **自动绘制多条 Loss 曲线**：从 TensorBoard 事件文件中提取所有 loss/accuracy 等标量。
- **实时 WeChat 通知**：通过 [Server酱](https://sct.ftqq.com/) 将曲线图发送到微信。
- **可拼接多张曲线图**：支持将多条 Loss 图拼接成一张总览图。
- **模块化设计**：仅需几行代码即可在训练中启用。

