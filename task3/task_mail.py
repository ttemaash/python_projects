import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
letter_template = '''\
From: devmanorg@yandex.ru
To: shl-tema@yandex.ru
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
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''

website_link = "https://dvmn.org/profession-ref-program/old2sk/abu5C/"
friend_name = "Николай"
sender_name = "Тёмка"

letter = letter_template.replace('%website%',website_link).replace('%friend_name%',friend_name).replace('%my_name%',sender_name)
letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(os.environ['LOGIN'], os.environ['PASSWORD'])
server.sendmail('devmanorg@yandex.ru','shl-tema@yandex.ru',letter)
server.quit()
