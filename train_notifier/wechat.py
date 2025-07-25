# train_notifier/wechat.py
import requests, time, os, base64

class WeChatNotifier:
    def __init__(self, sendkey: str, interval: int = 60):
        self.sendkey = sendkey
        self.interval = interval
        self.last_time = 0

    def send_image(self, title: str, image_path: str, desp: str = None):
        if not os.path.exists(image_path):
            print(f"[WeChatNotifier] Image not found: {image_path}")
            return
        with open(image_path, "rb") as f:
            img_base64 = base64.b64encode(f.read()).decode()
        url = f"https://sctapi.ftqq.com/{self.sendkey}.send"
        if desp:
            data = {"title": title, "desp": f"{desp}\n\n![img](data:image/png;base64,{img_base64})"}
        else:
            data = {"title": title, "desp": f"![img](data:image/png;base64,{img_base64})"}
        requests.post(url, data=data)

    def auto_push(self, image_path: str, title: str, desp: str = None):
        now = time.time()
        if now - self.last_time >= self.interval:
            self.send_image(title, image_path, desp)
            self.last_time = now
