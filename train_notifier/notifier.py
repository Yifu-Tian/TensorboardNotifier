# train_notifier/notifier.py
import time, os
from .wechat import WeChatNotifier
from .tb_reader import plot_tensorboard_tags
from .image_combine import combine_images

class Notifier:
    def __init__(self, sendkey, logdir="logs", interval=20, img_dir="tb_images"):
        self.notifier = WeChatNotifier(sendkey=sendkey, interval=interval)
        self.logdir = logdir
        self.img_dir = img_dir
        os.makedirs(img_dir, exist_ok=True)

    def update(self):
        img_paths, latest_losses = plot_tensorboard_tags(output_dir=self.img_dir, logdir=self.logdir)
        if not img_paths:
            return
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        loss_info = "\n".join([f"- {tag}: {val[1]:.6f}" for tag, val in latest_losses.items()])
        desp = f"**最新Loss值**:\n{loss_info}\n\n时间: {current_time}"
        print("loss: ", loss_info, "desp" , desp)
        combined = combine_images(img_paths, os.path.join(self.img_dir, "combined.png"), cols=2, scale=0.5)
        self.notifier.auto_push(combined, title=f"Tensorboard Loss Update | {current_time}", desp=desp)

