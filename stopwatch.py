import time

class Stopwatch:
    """シンプルなストップウォッチクラス"""
    
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0.0
        self.is_running = False
    
    def start(self):
        """ストップウォッチを開始する"""
        if not self.is_running:
            self.start_time = time.time() - self.elapsed_time
            self.is_running = True
            print("ストップウォッチを開始しました...")
    
    def stop(self):
        """ストップウォッチを停止する"""
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time
            self.is_running = False
            print(f"ストップウォッチを停止しました。経過時間: {self.elapsed_time:.2f}秒")
    
    def reset(self):
        """ストップウォッチをリセットする"""
        self.start_time = None
        self.elapsed_time = 0.0
        self.is_running = False
        print("ス���ップウォッチをリセットしました。")
    
    def get_time(self):
        """現在の経過時間を取得する"""
        if self.is_running:
            return time.time() - self.start_time
        else:
            return self.elapsed_time
    
    def display_time(self):
        """経過時間を見やすく表示する"""
        elapsed = self.get_time()
        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        seconds = elapsed % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:06.3f}"


if __name__ == "__main__":
    # 使用例
    sw = Stopwatch()
    
    print("=== ストップウォッチデモ ===")
    sw.start()
    print(f"現在時刻: {sw.display_time()}")
    
    time.sleep(2)
    print(f"現在時刻: {sw.display_time()}")
    
    time.sleep(2)
    print(f"現在時刻: {sw.display_time()}")
    
    sw.stop()
    print(f"\n最終時刻: {sw.display_time()}")