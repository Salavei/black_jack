import sqlite3


class SQLBot:
    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def check_user(self, user_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
            return bool(len(result))

    def user_exists(self):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `users`', ).fetchall()
            return len(result)

    def add_user(self, user_id):
        """Добавляем нового юзера"""
        nums = self.user_exists()
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`id`,`user_id`,`balance`) VALUES(?,?, ?)",
                                       (int(nums) + 1, user_id, 1000))
