## Описание

Иногда бывает задача записать stdout в файл, на который у пользователя нет прав:

$ echo “Secret Password” > /root/password.txt
permission denied

Начинающие пользователи сразу пробуют применить программу sudo:

$ sudo echo “Secret Password” > /root/password.txt
permission denied

Однако sudo здесь не помогает.

## Почему такое использование sudo не срабатывает?

Проблема в том, что команда запускается под sudo, но перенаправление в файл выполняется под текущим пользователем.

## Как можно обойти?

Можно обернуть команды в скрипт, который в дальнейшем вызовем в sudo, а команду и файл для записи передать в качестве аргументов

**Shell скрипт script.sh**

```
text=$1
file=$2

echo “$text” > $file
```

**команда:**

```

sudo ./script.sh "Secret Password" "/root/password.txt"
```

---

**Демонстрация**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Architecture/hw4/resources/LinuxArch1.png)

---

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Architecture/hw4/resources/LinuxArch2.png)

## Как правильно собрать такой pipeline с sudo?

Можно вызвать новую оболочку от имени root, используя -с аргумент

**команда:**

```

sudo sh -c "echo foo >> /root/password.txt"      <---- -с - передача команды в качестве аргумента в оболочку sh
```

---

**Демонстрация**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Architecture/hw4/resources/LinuxArch3.png)


![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Architecture/hw4/resources/LinuxArch4.png)
