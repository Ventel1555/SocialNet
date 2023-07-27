# SocialNetwork (blog) by Ventel
How to start project? 
    Write the following lines in the consol:

```
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```

Done!:white_check_mark: Go to browser using the link from the console.
____
**About the project**:
  A project, such as a social network, in which you can create, change, delete a user.
The user can create, change, delete posts.
Made basic registration, login, logout, reset and password change (based on django).
There is pagination on the pages.

And I’ll add, when you reset your password, a unique link is sent to the console.

**На русском люто**:
  Проект, типа соц сети, в котором можно создавать, изменять, удалять пользователя.
Пользователь может создавать, изменять, удалять посты.
Сделана базвая регистрация, вход, выход, сброс и изменение пароля на основе джанго.
Присутсвует пагинация на сраницах.

И ещё добавлю, при сбросе пароля уникальная ссылка отправляется в консоль.

