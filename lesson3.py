from dotenv import load_dotenv
import smtplib
import os

load_dotenv()

EMAIL_USER_NAME = os.getenv('EMAIL_USER_NAME')
EMAIL_APPS_PASSSWORD = os.getenv('EMAIL_APPS_PASSSWORD')

website = "https://dvmn.org/profession-ref-program/skislyakov84/82SOp/"
friend_name = "Виталий"
my_name = "Сергей Кисляков"
email_from = "kislyakov84@yandex.ru"
email_to = "s.kislyakov84@gmail.com"

letter = f"""From: {email_from}
To: {email_to}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".replace('%website%', website).replace('%friend_name%', friend_name).replace('%my_name%', my_name)

letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(EMAIL_USER_NAME, EMAIL_APPS_PASSSWORD)
server.sendmail(email_from, email_to, letter)
server.quit()