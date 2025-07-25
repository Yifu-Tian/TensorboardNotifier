## Tensorboard Notifier

**Tensorboard Notifier** 是一个基于 **TensorBoard 日志** 的训练监控工具，能够自动提取 Loss 曲线，并通过 **Server酱 API** 将 Loss 曲线图像和最新指标实时推送到微信端。  

在深度学习训练时，模型往往需要几个小时甚至几天才能收敛, 传统的做法是打开 TensorBoard 或控制台，不断查看 Loss 是否下降🤯
**Tensorboard Notifier** 的设计初衷是让你不用时刻守在电脑前🤩
- 它会自动收集训练的最新 Loss 曲线;
- 定期生成图片并通过 **Server酱** API推送到你的微信;
- 让你在手机上实时查看模型训练状态，省时且高效
有了它，你不必再守在电脑前盯着终端或 TensorBoard，训练过程中可以去喝一杯咖啡 ☕，也不会错过模型的收敛趋势😋

<img width="200" height="500" alt="image" src="https://github.com/user-attachments/assets/6d382528-ce4e-488d-87a5-b7b0c3e2a8cd" />

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

### Example
```
from train_notifier import Notifier
...

notifier = Notifier(sendkey="your-SCT-api-key", logdir="your-logs-path", interval=60)
trainer.train(num_epochs=300, save_ckpt_epoch=50, notifier=notifier)
```
5. 在训练循环中调用 `notifier.update()`

### Example
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

### Notifier 参数
- **sendkey**: 你的 Server酱 API Key
- **logdir**: TensorBoard 日志目录 (与 `SummaryWriter` 的 `log_dir` 对应)
- **interval**: 推送间隔（秒）
## 获取API Key
You can get your API [here](https://sct.ftqq.com/sendkey).

