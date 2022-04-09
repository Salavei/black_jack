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

    def check_balance(self, user_id):
        """Проверяем, баланс юзера"""
        with self.connection:
            return self.cursor.execute('SELECT `balance` FROM `users` WHERE `user_id` = ?', (user_id,)).fetchone()[0]

    def update_balance_minus(self, user_id):
        """Изменяем, баланс юзера(отнимаем 50)"""
        with self.connection:
            balance = self.check_balance(user_id) - 50
            return self.cursor.execute(
                "UPDATE `users` SET `balance` = ? WHERE `user_id` = ?", (balance, user_id))

    def update_balance_add(self, user_id):
        """Изменяем, баланс юзера(добавляем 50)"""
        with self.connection:
            balance = self.check_balance(user_id) + 50

            return self.cursor.execute(
                "UPDATE `users` SET `balance` = ? WHERE `user_id` = ?", (balance, user_id))

    def story_exists(self):
        """Для получения айди"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `story`', ).fetchall()
            return len(result)

    def add_story(self, user_id, status_win):
        """Добавляем историю юзера"""
        nums = self.story_exists()
        with self.connection:
            return self.cursor.execute("INSERT INTO `story` (`id`,`win`,`user_id`) VALUES(?,?, ?)",
                                       (nums, status_win, user_id))

    def check_story(self, user_id):
        """Узнать, историю игр юзера"""
        with self.connection:
            return self.cursor.execute('SELECT `id`,`win` FROM `story` WHERE `user_id` = ?', (user_id,)).fetchall()
