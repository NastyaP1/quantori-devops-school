## Описание

Исследовать работу протокола ICMP и утилит traceroute и ping:
- Выяснить количество хопов до крупных сетевых узлов: google, yandex, cisco, aws, microsoft, etc.
- Попробовать определить ОС которая управляет доступными серверами этих сетевых узлов.
- При помощи утилиты mtr определить узкие места в сети по маршруту до этих узлов.
- Сравнить результаты выполнения traceroute при использовании разных сетевых протоколов: IP, TCP, UDP.

## Результат

### 1. Выяснить количество хопов до крупных сетевых узлов.

**используемые команды**
```
traceroute <host>

или

sudo traceroute -I <host>

```

**анализ результа**
| Хост | Количество хопов |
|---|---|
| google.com | 21 |
| yandex.ru | 9 |
| cisco.com | 18 |
| aws.amazon.com | 15 |
| microsoft.com | маршрут был потерян с 22 хоста|

---

**маршрут до google.com**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw4/resources/NWpicture1.png)

---

**маршрут до yandex.ru**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw4/resources/NWpicture2.png)

---

**маршрут до cisco.com**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw4/resources/NWpicture3.png)

---

**маршрут до aws.amazon.com**


![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw4/resources/NWpicture4.png)

---

**маршрут до microsoft.com**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw4/resources/NWpicture5.png)

---

### 2. Определение ОС
Для определения ОС удаленного хоста использовалась утилита ping и значение счетчика TTL. Если TTL 254 или меньше - это UNIX-based системы, если TTl 128 и меньше, то Windows.

Анализируя результаты ping команды, можно предполождить, что google.com(74.125.131.113) Windows система, у остальный серверов Unix, ping до microsoft.com не прошел.

```
Anastasias-MacBook-Pro-3:~ anastasiapereslavceva$ ping yandex.ru
PING yandex.ru (77.88.55.77): 56 data bytes
64 bytes from 77.88.55.77: icmp_seq=0 ttl=247 time=20.974 ms
```

```
Anastasias-MacBook-Pro-3:~ anastasiapereslavceva$ ping google.com
PING google.com (74.125.131.113): 56 data bytes
64 bytes from 74.125.131.113: icmp_seq=0 ttl=110 time=28.700 ms
```

```
Anastasias-MacBook-Pro-3:~ anastasiapereslavceva$ ping aws.amazon.com
PING dr49lng3n1n2s.cloudfront.net (52.85.119.72): 56 data bytes
64 bytes from 52.85.119.72: icmp_seq=0 ttl=229 time=52.890 ms
```

```
Anastasias-MacBook-Pro-3:~ anastasiapereslavceva$ ping cisco.com
PING cisco.com (72.163.4.185): 56 data bytes
64 bytes from 72.163.4.185: icmp_seq=0 ttl=238 time=197.992 ms
```

```
Anastasias-MacBook-Pro-3:~ anastasiapereslavceva$ ping microsoft.com
PING microsoft.com (40.76.4.15): 56 data bytes
Request timeout for icmp_seq 0
```

### 3. Использование утилиты mtr

Утилита mtr совмещает в себе функциональность программа traceroute и ping. То есть эта программа показывает маршрут до указанного узла и непрерывно пингует каждые хоп и при этом собирает общую статистику потерь — на основе этих данных можно определить проблемный узел, на котором теряются пакеты.

В колонке Loss% можно увидеть процентное соотношение потерь на определенном узле.

**используемые команды**
```
sudo mtr <host>

```
---

**mtr до google.com**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw4/resources/NWpicture6.png)

---

**mtr до yandex.ru**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw4/resources/NWpicture7.png)

---

**mtr до cisco.com**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw4/resources/NWpicture8.png)

---

**mtr до aws.amazon.com**


![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw4/resources/NWpicture9.png)

---

**mtr до microsoft.com**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw4/resources/NWpicture10.png)

---

### 4. Утилита traceroute и протоколы IP, TCP, UDP.

При использовании команда traceroute больше всего информации о хопах было получено при использовании UDP и TCP протоколов, IP протокол показал наименьший результат.

---

**UDP**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw4/resources/NWpicture11.png)

---

**TCP**


![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw4/resources/NWpicture12.png)

---

**IP**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw4/resources/NWpicture13.png)

---

