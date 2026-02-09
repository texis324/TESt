import json
import random

class TodoApp:
    def __init__(self):
        self.tasks = []
        self.load_tasks()
        self.horror_phrases = [
            "魂を奪うタスクだ…",
            "血の匂いがする…",
            "呪いの始まりだ…",
            "幽霊が囁いている…",
            "闇が広がる…"
        ]

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open('tasks.json', 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, task):
        # ホラー絵文字
        emojis = ['👻', '🧛', '🧟', '🩸', '💀', '🕷️', '🦇', '🏚️']
        emoji = random.choice(emojis)
        # タスクをホラー風に変える
        modifiers = ['', 'を血まみれに', 'を呪って', 'を幽霊のように', 'を闇の��で']
        modified_task = task + random.choice(modifiers)
        self.tasks.append({"task": modified_task, "completed": False, "emoji": emoji})
        self.save_tasks()
        print(f"{emoji} '{modified_task}' を追加した… {random.choice(self.horror_phrases)}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save_tasks()
            horrors = [
                "完了…しかし魂はまだ彷徨っている… 👻",
                "よくやった…でも次はもっと恐ろしいタスクだ… 🧛",
                "お疲れ…血の海が広がる… 🩸",
                "スーパー完了…だが呪いは解けない… 💀",
                "おしまい…闇が君を包む… 🕷️"
            ]
            print(f"{self.tasks[index]['emoji']} '{self.tasks[index]['task']}' を完了にした… {random.choice(horrors)}")
        else:
            print("そんな番号はない… 消えたのか…")

    def list_tasks(self):
        if not self.tasks:
            print("タスクはない… 静寂だけが残る… 👻")
        else:
            print("恐ろしいタス��リストだ…")
            for i, task in enumerate(self.tasks):
                status = "完了（しかし幽霊は去らない…）" if task["completed"] else "未完了… 恐怖が忍び寄る…"
                emoji = task.get("emoji", "👻")
                print(f"{i}: {emoji} {task['task']} - {status}")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"{removed['emoji']} '{removed['task']}' を消した… {random.choice(self.horror_phrases)}")
        else:
            print("消せない… 呪われている…")


def main():
    app = TodoApp()
    while True:
        print("\n👻 ホラー To-Do アプリ 👻")
        print("1. タスクを追加（魂を賭けて…）")
        print("2. タスクを完了（闇を呼び…）")
        print("3. タスク一覧（恐怖のリスト）")
        print("4. タスクを削除（永遠の別れ…）")
        print("5. 終了（逃げられるのか…）")
        choice = input("何をする… ?: ")
        
        if choice == "1":
            task = input("タスクを入力（血��流して…）: ")
            app.add_task(task)
        elif choice == "2":
            app.list_tasks()
            try:
                index = int(input("完了する番号（幽霊の囁き…）: "))
                app.complete_task(index)
            except ValueError:
                print("数字を入れろ… さもなくば呪われる…")
        elif choice == "3":
            app.list_tasks()
        elif choice == "4":
            app.list_tasks()
            try:
                index = int(input("削除する番号（魂の叫び…）: "))
                app.remove_task(index)
            except ValueError:
                print("数字を入れろ… さもなくば呪われる…")
        elif choice == "5":
            app.save_tasks()
            print("また… 会おう… 👋")
            break
        else:
            print("正しい番号を入れろ… 闇が迫る…")

if __name__ == "__main__":
    main()