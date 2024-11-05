from task import Task
print("Добро пожаловать в меню" + "\n"+ "1 - Добавить задачу" + "\n" + "2 - Удалить задачу" + "\n" + "3 - Показать задачи" + "\n" + "4 - Выход")

operation = input("ВВедите операцию: ")


match operation:
    case "1":
        Task.add_task()
    case "2":
        Task.delete_task()
    case "3":
        Task.show_tasks()
    case "4":
        exit()