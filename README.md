## Tensorboard Notifier

**Tensorboard Notifier** is a training monitoring tool based on **TensorBoard logs**, which can automatically extract loss curves and push the loss curve images and the latest metrics to WeChat via the **Server酱** API 

🤯During deep learning training, models often take hours or even days to converge. The traditional approach is to constantly check TensorBoard or the console to see if the loss is decreasing. 

🤩**Tensorboard Notifier** is designed to free you from watching the computer all the time!
- It automatically collects the latest loss curves during training;

- Periodically generates images and pushes them to your WeChat via Server酱 API;

- Allows you to monitor your model's training status on your phone, saving time and improving efficiency.

😋You no longer have to stare at the terminal or TensorBoard. You can go grab a cup of coffee ☕ during training and still stay updated with the convergence trends.

<p align="center">
<img width="300" height="600" alt="image" src="https://github.com/user-attachments/assets/6d382528-ce4e-488d-87a5-b7b0c3e2a8cd" />
</p>

## Quick Start

1. Download ZIP
2. Extract `train_notifier.zip` into your project directory.
The structure should look like this:
```
your-project/
├── train/
|   ├── train.py
├── train_notifier/
│   ├── ...
├── setup.py
├── README.md
├── requirements.txt
```
3. Navigate to the `train_notifier` directory and install:
```
cd train_notifier/ && pip install -r requirements.txt && pip install -e .
```
4. If you have a training entry script, add the following code (or insert it into your training loop)

### Example
```
from train_notifier import Notifier
...

notifier = Notifier(sendkey="your-SCT-api-key", logdir="your-logs-path", interval=60)
trainer.train(num_epochs=300, save_ckpt_epoch=50, notifier=notifier)
```
5. Call `notifier.update()` within the training loop

### Example
```
def train(self, num_epochs: int, save_ckpt_epoch: int = None, notifier=None):
    ...
    for epoch_idx in tglobal:
        ...
        if notifier:
            notifier.update()  # 每个 epoch 结束时推送一次(也可以自定义)
```
6. Run `train.py`
7. Check messages on WeChat

### Notifier Parameters
- **sendkey**: Your Server酱 API Key
- **logdir**: TensorBoard logs directory (must match `log_dir` in your `SummaryWriter`)
- **interval**: Push interval (seconds)

## Get API Key
You can get your API [here](https://sct.ftqq.com/sendkey).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
