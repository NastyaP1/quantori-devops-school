## Описание

Построить сеть на коммутаторах и концентраторах в Cisco PT. Продемонстрировать широковещание.

## Результат

Для демонстрации широковещания был взят маршрут от PC0 до PC6 c передачей пакетов по ARP, а затем ICMP протоколу.

**передача пакета по ARP**
![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw1/resources/NWpicture1.png)

**обратная передача пакета по ARP**
![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw1/resources/NWpicture2.png)

**передача пакета по ICMP**
![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw1/resources/NWpicture3.png)

ICMP пакет не идет через Hub0, так как у коммутатора уже известны MAC-адреса в ходе передачи первого пакета по ARP протоколу.
![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw1/resources/NWpicture4.png)

**ICMP пакет достиг PC6**
![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw1/resources/NWpicture5.png)

**резудьтат симуляции**
![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Network/hw1/resources/NWpicture6.png)
