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

</br>

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw4/resources/NWpicture1.png)

---

**маршрут до yandex.ru**

</br>

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw4/resources/NWpicture2.png)

---

**маршрут до cisco.com**

</br>

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw4/resources/NWpicture3.png)

---

**маршрут до aws.amazon.com**

</br>

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw4/resources/NWpicture4.png)

---

**маршрут до microsoft.com**

</br>

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw4/resources/NWpicture5.png)

---

### 2. Определение ОС

### 3. Использование утилиты mtr

### 4. Утилита traceroute и протоколы IP, TCP, UDP.

