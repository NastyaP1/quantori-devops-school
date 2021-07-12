## Описание

Программа ping в операционной системе solaris не выводит подробности взаимодействия по icmp, а кратко сообщает о том, доступен ли удаленный сетевой узел:
$ ping google.com
google.com is alive
$ ping eeeerrr.fff.rrrs
eeeerrr.fff.rrr is not alive
Написать bash скрипт ping.sh - который будет эмулировать поведение программы ping из ОС Solaris.

## Результат

**Shell скрипт ping.sh:**

```
host=$1                                      <---- приравнивание переменной host к первому переданному аргументу

ping -c1 $host 2>/dev/null 1>/dev/null       <---- ping хоста, -c1 вернет первую отправку пакета; stdout и stderr отправляем в /dev/null

if [[ $? -eq 0 ]]; then                      <---- проверка на доступность хоста - доступен, если результат предыдщей команды успешен
  echo "$host is alive"
else                                         <---- иначе
  echo "$host is not alive"
fi

```

**команда:**

```
./ping.sh <host>
```

---

**Демонстрация**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Architecture/hw5/resources/LinuxArch1.png)
