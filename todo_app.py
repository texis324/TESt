import json
import random

class TodoApp:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open('tasks.json', 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, task, priority='中'):
        emoji = self.get_emoji(task)
        self.tasks.append({"task": task, "completed": False, "priority": priority, "emoji": emoji})
        self.save_tasks()
        print(f"{emoji} タスク '{task}' を追加しました！ (優先度: {priority})")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save_tasks()
            message = random.choice([
                "素晴らしい！タスク完了だね！ 🎉",
                "よくやった！次もがんばろう！ 💪",
                "完了！君はスーパーヒーローだ！ 🦸‍♂️",
                "お疲れ様！少し休憩しようか？ ☕"
            ])
            print(f"{self.tasks[index]['emoji']} タスク '{self.tasks[index]['task']}' を完了にしました。 {message}")
        else:
            print("無効なインデックスです。")

    def list_tasks(self):
        if not self.tasks:
            print("タスクがありません。新しいタスクを追加しよう！ 📝")
        else:
            sorted_tasks = sorted(self.tasks, key=lambda x: ['高', '中', '低'].index(x['priority']))
            for i, task in enumerate(sorted_tasks):
                status = "✅" if task["completed"] else "⏳"
                pri = task.get("priority", "中")
                emoji = task.get("emoji", "")
                print(f"{i}: {emoji} {task['task']} [{pri}] {status}")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"{removed['emoji']} タスク '{removed['task']}' を削除しました。さようなら！ 👋")
        else:
            print("無効なインデックスです。")

    def get_emoji(self, task):
        keywords = {
            '仕事': '💼', '勉強': '📚', '買い物': '🛒', '運動': '🏃‍♂️',
            '料理': '🍳', '旅行': '✈️', '会議': '📅', '読書': '📖'
        }
        for key, emoji in keywords.items():
            if key in task:
                return emoji
        return '📌'  # デフォルト

def main():
    app = TodoApp()
    while True:
        print("\n🎯 楽しい To-Do アプリ 🎯")
        print("1. タスクを追加 (優先度指定可能)")
        print("2. タスクを完了")
        print("3. タスク一覧")
        print("4. タスクを削除")
        print("5. 終了")
        choice = input("選択: ")
        
        if choice == "1":
            task = input("タスクを入力: ")
            priority = input("優先度 (高/中/低) [デフォルト: 中]: ") or '中'
            if priority not in ['高', '中', '低']:
                priority = '中'
            app.add_task(task, priority)
        elif choice == "2":
            app.list_tasks()
            index = int(input("完了するタスクの番号: "))
            app.complete_task(index)
        elif choice == "3":
            app.list_tasks()
        elif choice == "4":
            app.list_tasks()
            index = int(input("削除するタスクの番号: "))
            app.remove_task(index)
        elif choice == "5":
            app.save_tasks()
            print("またね！ 👋")
            break
        else:
            print("無効な選択です。")

if __name__ == "__main__":
    main()