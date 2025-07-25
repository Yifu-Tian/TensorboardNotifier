# train_notifier/tb_reader.py
import os
import matplotlib.pyplot as plt
from tensorboard.backend.event_processing import event_accumulator

def plot_tensorboard_tags(output_dir="tb_images", logdir="logs"):
    os.makedirs(output_dir, exist_ok=True)
    ea = event_accumulator.EventAccumulator(logdir)
    ea.Reload()
    tags = ea.Tags().get('scalars', [])
    img_paths, latest_losses = [], {}

    for tag in tags:
        scalars = ea.Scalars(tag)
        steps = [s.step for s in scalars]
        values = [s.value for s in scalars]
        if len(steps) == 0:
            continue
        plt.figure()
        plt.plot(steps, values, label=tag)
        plt.xlabel("Step"); plt.ylabel("Value"); plt.legend()
        path = os.path.join(output_dir, f"{tag.replace('/', '_')}.png")
        plt.savefig(path, dpi=100, bbox_inches="tight")
        plt.close()
        img_paths.append(path)
        latest_losses[tag] = (steps[-1], values[-1])

    return img_paths, latest_losses
