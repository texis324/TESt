# Simple To-Do App in Python

class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"タスク '{task}' を追加しました。")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f"タスク '{self.tasks[index]['task']}' を完了にしました。")
        else:
            print("無効なインデックスです。")

    def list_tasks(self):
        if not self.tasks:
            print("タスクがありません。")
        else:
            for i, task in enumerate(self.tasks):
                status = "完了" if task["completed"] else "未完了"
                print(f"{i}: {task['task']} [{status}]")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"タスク '{removed['task']}' を削除しました。")
        else:
            print("無効なインデックスです。")


def main():
    app = TodoApp()
    while True:
        print("\nTo-Do アプリ")
        print("1. タスクを追加")
        print("2. タスクを完了")
        print("3. タスク一覧")
        print("4. タスクを削除")
        print("5. 終了")
        choice = input("選択: ")
        
        if choice == "1":
            task = input("タスクを入力: ")
            app.add_task(task)
        elif choice == "2":
            index = int(input("完了するタスクの番号: "))
            app.complete_task(index)
        elif choice == "3":
            app.list_tasks()
        elif choice == "4":
            index = int(input("削除するタスクの番号: "))
            app.remove_task(index)
        elif choice == "5":
            break
        else:
            print("無効な選択です。")

if __name__ == "__main__":
    main()