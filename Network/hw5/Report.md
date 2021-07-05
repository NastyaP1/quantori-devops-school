## Описание

Продемонстрировать работу протоколов прикладного уровня HTTP и SMTP при помощи программы telnet:
- Отправить GET запрос удаленному серверу.
- Отправить POST запрос удаленному серверу.
- Отправить письмо самому себе.

## Результат

### 1. Telnet - GET запрос удаленному серверу
---

Необходимо использовать следующий синтаксис, чтобы подключиться к серверу [SERVER] на некоторому порту [PORT] через telnet и запросить HTTP заголовок некоторой страницы [WEB PAGE] :

```
$ telnet [SERVER] [PORT]
Trying xxx.xxx.xxx.xxx...
Connected to [SERVER].
Escape character is '^]'.
HEAD [WEB PAGE] HTTP/1.1
HOST: [SERVER]
<Press ENTER>
```

В качестве тестирования отправки GET запроса использовался сервер httpbin.org, порт 80 - протокол tcp, страница /anything

**Демонстрация**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw3/resources/NWPicture1.png)

### 2. Telnet - POST запрос удаленному серверу
---

Необходимо использовать следующий синтаксис, чтобы подключиться к серверу [SERVER] на некоторому порту [PORT] через telnet и отправить POST запрос на некоторую страницу [WEB PAGE] с форматом отправляемого содержимого [TYPE] и длиной содержимого [LENGTH]:

```
$ telnet [SERVER] [PORT]
Trying xxx.xxx.xxx.xxx...
Connected to [SERVER].
Escape character is '^]'.
POST [WEB PAGE] HTTP/1.1
HOST: [SERVER]
Connection: close
Content-type: [TYPE]
Content-length: [LENGTH]
<Press ENTER>
```

В качестве тестирования отправки POST запроса использовался сервер httpbin.org, порт 80 - протокол tcp, страница /post, сообщение {"message": Hi}, длиной в 14 символов и форматом application/json

**Демонстрация**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw3/resources/NWPicture2.png)

### 3. Telnet - передача сообщения на почту
---

Необходимо использовать следующий синтаксис и выполнить следующие шаги, чтобы отправить письмо на почту:

1) подключиться к mail серверу через telnet

```
$ telnet <server> 25
```

2) Использовать HELO команду, для указания домена:

```
$ HELO host
```

3) Указать адрес отправитель

```
MAIL FROM: <address@example.com>
```

4) Указать адрес получателя

```
RCPT TO: <someone@example.com>
```

5) Указать тему и само сообщение

```
DATA
Subject: Sending an email using telnet

Hello,

Here is my body? Do you like it?

cheers
.
```

> Для отправки сообщения необходимо на отдельной строке напечать . как указано в синтаксисе выше

6) Для выхода напечатай:

```
quit
```

В качестве тестирования отправки email сообщения использовался сервер mx.yandex.ru, порт 25 - протокол smtp

**Демонстрация**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw3/resources/NWPicture3.png)

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw3/resources/NWPicture4.png)

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw3/resources/NWPicture5.png)
