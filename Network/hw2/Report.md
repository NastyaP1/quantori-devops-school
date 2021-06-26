## Описание

Построить сеть на коммутаторах и концентраторах в Cisco PT. Продемонстрировать широковещание.

## Результат

Для демонстрации широковещания был взят маршрут от PC0 до PC6 c передачей пакетов по ARP, а затем ICMP протоколу.

**1. передача пакета по ARP**
![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw2/resources/NWpicture1.png)

---

**2. обратная передача пакета по ARP**
![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw2/resources/NWpicture2.png)

---

**3. передача пакета по ICMP**
![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw2/resources/NWpicture3.png)

---

ICMP пакет не идет через Hub0, так как у коммутатора уже известны MAC-адреса в ходе передачи первого пакета по ARP протоколу.

<br>

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw2/resources/NWpicture4.png)

---
 
**4. ICMP пакет достиг PC6**
![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw2/resources/NWpicture5.png)

---

**5. результат симуляции**
![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw2/resources/NWpicture6.png)

---
