## Tensorboard Notifier

**Tensorboard Notifier** 是一个基于 **TensorBoard 日志** 的训练监控工具, 能够自动获取 Loss 曲线, 并通过 **Server酱** API将Loss曲线图像推送至微信端

<img width="1080" height="1739" alt="image" src="https://github.com/user-attachments/assets/6d382528-ce4e-488d-87a5-b7b0c3e2a8cd" />

---
## Quick Start

1. Download ZIP
2. 解压train_notifier.zip到你的项目目录下
如下所示
```
your-project/
├── train/
|   ├── train.py
├── train_notifier/
│   ├── ...
├── setup.py
├── README.md
```
3. 切换到train_notifier目录下安装
```
cd train_notifier/ && pip install -e .
```
4. 如果有训练入口脚本, 需要在脚本中调用(否则在训练循环脚本中添加)
如下所示
```
from train_notifier import Notifier
...

notifier = Notifier(sendkey="your-SCT-api-key", logdir="your-logs-path", interval=60)
trainer.train(num_epochs=300, save_ckpt_epoch=50, notifier=notifier)
```
5. 在训练循环脚本中添加
如下所示
```
def train(self, num_epochs: int, save_ckpt_epoch: int = None, notifier=None):
    ...
    for epoch_idx in tglobal:
        ...
        if notifier:
            notifier.update()  # 每个 epoch 结束时推送一次(也可以自定义)
```
6. 运行train.py
7. 在微信上查看信息

## Features

- **自动绘制多条 Loss 曲线**：从 TensorBoard 事件文件中提取所有 loss/accuracy 等标量。
- **实时 WeChat 通知**：通过 [Server酱](https://sct.ftqq.com/) 将曲线图发送到微信。
- **可拼接多张曲线图**：支持将多条 Loss 图拼接成一张总览图。
- **模块化设计**：仅需几行代码即可在训练中启用。

