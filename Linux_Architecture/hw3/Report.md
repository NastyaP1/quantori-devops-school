## Описание

В папке /var/ftp/ - есть подпапки пользователей (/var/ftp/ivan, /var/ftp/aleksei, etc.), куда они складывают свои файлы.
Есть пользователь и группа ftp-admin - они используются администратором ftp сервера, и он может управлять содержимым всех подпапок всех пользователей. При этом обычные пользователи могут управлять только своими файлами.
Начинающий администратор случайно поломал права на папки и файлы, а также сменил пользователей владельцев и групп владельцев у некоторых файлов. Вам предстоит починить и привести систему к рабочему состоянию.

## Результат

Для начала создадим двух пользователей  - ivan и alex с правами обычного пользователя. А также администратора - FTP_admin, отнесенного к группе ftp_admin.

```

sudo useradd <username>                      <----- добавление пользователя
sudo passwd <username>                       <----- добавление пароля пользователю
sudo usermod -aG <group> <username>          <----- добавление пользователя к группе

```

---

**Демонстрация пользователя и группы**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Architecture/hw3/resources/LinuxArch1.png)

---

Для начала необходимо создать папки пользователей и дать самим пользователям корректные права, а также администраторам доступ к папкам.

```

chmod 2775 var/ftp

sudo chown -R ivan:ftp_admin var/ftp/ivan
sudo chown -R alex:ftp_admin var/ftp/alex

```

---

**Демонстрация создания папок**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Architecture/hw3/resources/LinuxArch2.png)

**Демонстрация восстановленных прав**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Architecture/hw3/resources/LinuxArch3.png)

---

Зайдем под пользователем ivan и попытаемся создать в папке alex файл. Операция не будет разрешена, так как мы дали доступ others (2775) только на чтение и исполнение.

Так же продемоснтрируем, что сам ivan может создавать папки и файлы в своей папке.

**Демонстрация, что ivan не может писать в файл alex. alex имеет доступ к своей папке**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Architecture/hw3/resources/LinuxArch4.png)

---

Так же мы дали доступ группе ftp_admin, к которой относится наш администратор, ко всем папкам /var/ftp. ivan создал в своей папке файл cache.txt. Продемонстрируем, что ftp_admin сможет удалить этот файл.

**Демонстрация, что ftp_admin может удалить пользовательские файлы**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Architecture/hw3/resources/LinuxArch5.png)

