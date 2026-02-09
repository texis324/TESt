import time
import sys

class Stopwatch:
    """インタラクティブなストップウォッチクラス"""
    
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0.0
        self.is_running = False
    
    def start(self):
        """ストップウォッチを開始する"""
        if not self.is_running:
            self.start_time = time.time() - self.elapsed_time
            self.is_running = True
            print("✓ ストップウォッチを開始しました")
        else:
            print("⚠ 既に実行中です")
    
    def stop(self):
        """ストップウォッチを停止する"""
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time
            self.is_running = False
            print(f"✓ ストップウォッチを停止しました")
        else:
            print("⚠ 既に停止しています")
    
    def reset(self):
        """ストップウォッチをリセットする"""
        self.start_time = None
        self.elapsed_time = 0.0
        self.is_running = False
        print("✓ ストップウォッチをリセットしました")
    
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


def print_menu():
    """メニューを表示"""
    print("\n" + "="*50)
    print("ストップウォッチ - インタラクティブメニュー")
    print("="*50)
    print("コマンド一覧:")
    print("  [s] start   - ストップウォッチを開始")
    print("  [p] stop    - ストップウォッチを停止")
    print("  [r] reset   - ストップウォッチをリセット")
    print("  [t] time    - 現在の経過時間を表示")
    print("  [q] quit    - 終了")
    print("="*50)


if __name__ == "__main__":
    sw = Stopwatch()
    print_menu()
    
    while True:
        try:
            command = input("\nコマンドを入力してください (s/p/r/t/q): ").strip().lower()
            
            if command == 's':
                sw.start()
            elif command == 'p':
                sw.stop()
            elif command == 'r':
                sw.reset()
            elif command == 't':
                print(f"⏱ 経過時間: {sw.display_time()}")
            elif command == 'q':
                print("ストップウォッチを終了します。")
                break
            else:
                print("❌ 不正なコマンドです。s/p/r/t/q を入力してください")
        
        except KeyboardInterrupt:
            print("\n\nストップウォッチを終了します。")
            break
        except Exception as e:
            print(f"エラーが発生しました: {e}")