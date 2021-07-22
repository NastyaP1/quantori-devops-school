## Описание

В папке /var/ftp/ - есть подпапки пользователей (/var/ftp/ivan, /var/ftp/aleksei, etc.), куда они складывают свои файлы.
Есть пользователь и группа ftp-admin - они используются администратором ftp сервера, и он может управлять содержимым всех подпапок всех пользователей. При этом обычные пользователи могут управлять только своими файлами.

Написать скрипт для добавления новых пользователей ftp-сервера в систему. Скрипт должен генерировать пароль, добавлять пользователя в систему, настраивать права пользователя, создавать домашний каталог.

## Результат

Код скрипта для добавления новых пользователей: [script](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw4/scripts/script.sh)

**Демонстрация**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw4/resources/LinuxAdm1.png)

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw4/resources/LinuxAdm2.png)

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw4/resources/LinuxAdm3.png)

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw4/resources/LinuxAdm4.png)
