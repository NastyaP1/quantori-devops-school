## Описание

В папке /var/ftp/ - есть подпапки пользователей (/var/ftp/ivan, /var/ftp/aleksei, etc.), куда они складывают свои файлы.
Есть пользователь и группа ftp-admin - они используются администратором ftp сервера, и он может управлять содержимым всех подпапок всех пользователей. При этом обычные пользователи могут управлять только своими файлами.
Начинающий администратор случайно поломал права на папки и файлы, а также сменил пользователей владельцев и групп владельцев у некоторых файлов. Вам предстоит починить и привести систему к рабочему состоянию.

## Результат

Для начала создадим двух пользователей  - ivan и alex с правами обычного пользователя и отнесем их к группам ivan и alex соотвественно. А  также администратора - FTP_admin, отнесенного к группе ftp_admin и имеющего права root.

```

sudo useradd <username>                      <----- добавление пользователя
sudo passwd <username>                       <----- добавление пароля пользователю
sudo usermod -aG <group> <username>          <----- добавление пользователя к группе
sudo useradd -ou 0 -g 0 <username>           <----- создать пользователя с правами root

```

---

**Демонстрация групп**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Architecture/hw3/resources/LinuxArch1.png)

**Демонстрация пользователей**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Architecture/hw3/resources/LinuxArch3.png)

**Демонстрация доступа FRT_admin к папкам root**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Architecture/hw3/resources/LinuxArch2.png)

---

В ходе некорректного обращения с данными администратор неправильно настроил права доступа к личным папкам пользователя.

Также у пользователя ivan для файла /var/ftp/ivan/file.tx администратор удалил права на чтение пользователю.

---

**Демонстрация доступа неправильных прав для личных папок**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Architecture/hw3/resources/LinuxArch4.png)

**Демонстрация доступа alex к файлам ivan. Отсуствие права чтения у файла**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Architecture/hw3/resources/LinuxArch5.png)

---

Администратор, имеющий права root, быстро восстановил ошибки при помощи следующих комманд:

```
Смена прав доступа к личным папкам пользователей:

sudo chown -R ivan:ivan var/ftp/ivan
sudo chown -R alex:alex var/ftp/alex

```

---

**Демонстрация восстановленных прав**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Architecture/hw3/resources/LinuxArch6.png)

**Демонстрация, что alex не может больше писать в файл ivan**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Architecture/hw3/resources/LinuxArch7.png)

Но право на чтение файла даже для ivan еще не восстановлено.

**Демонстрация, что ivan все еще не может читать файл**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Architecture/hw3/resources/LinuxArch8.png)

---

Для восстановления прав на чтение файла пользователю FTP_admin использовал следующую команду:

```

sudo chmod u+r /var/ftp/ivan/file.tx

```

---

**Демонстрация изменения прав файла**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Architecture/hw3/resources/LinuxArch9.png)

**Демонстрация чтения файла**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Architecture/hw3/resources/LinuxArch10.png)
