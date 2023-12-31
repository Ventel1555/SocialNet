# SocialNetwork (blog) by Ventel
How to start project? 
    - Write the following lines in the consol:
```
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations blog
python manage.py makemigrations account
python manage.py migrate
```
If you get error, try this:
```
python manage.py migrate --run-syncdb 
```
Run server:
```
python manage.py runserver
```
Done!:white_check_mark: Go to browser using the link from the console.

! **Remember** to set you *secret key*, and set up *gmail & password* (password reset) in settings.py ! 

**Pay attention to the last lines of README file.**

## Description
A project, such as a social network, in which you can create and change a user.
The user can create, change, delete posts.
Made basic registration, login, logout, reset and password change (based on django).
There is pagination on the pages. You can follow to your favorite bloggers.

And I’ll add, when you reset your password, a unique link is sent to the console.

To make the password reset work, in the ```SocialNetwork/settings.py``` , change the values in the last lines (EMAIL_HOST_USER, EMAIL_HOST_PASSWORD). More details on how to set your password here:
https://support.google.com/accounts/answer/185833?&p=InvalidSecondFactor&rd=1

## Описание
  Проект, типа соц сети, в котором можно редактировать пользователя.
Пользователь может создавать, изменять или удалять посты.
Сделана базвая регистрация, вход, выход, сброс и изменение пароля на основе джанго.
Присутсвует пагинация на сраницах.  Вы можете подписаться на своих любимых блоггеров.

И ещё добавлю, при сбросе пароля уникальная ссылка отправляется в консоль.


Чтобы работал сброс пароля, в фале ```SocialNetwork/settings.py``` , измените значения в последних строчках (EMAIL_HOST_USER, EMAIL_HOST_PASSWORD). Подробнее, как поставить свой пароль здесь: https://support.google.com/accounts/answer/185833?&p=InvalidSecondFactor&rd=1
