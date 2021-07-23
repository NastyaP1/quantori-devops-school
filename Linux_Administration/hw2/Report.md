## Описание

1) Рассчитать вероятность потерять данные при использовании дисков в raid массиве, для разных raid level и разных количествах дисков. Считать вероятность выхода из строя одного диска - 1%.

2) Рассчитать насколько уменьшится суммарный объем памяти при использовании дисков в raid массиве, для разных raid level и разном количестве дисков, по сравнению с использованием дисков как независимых.

3) обрать несколько lv поверх md (raid5). Смонтировать с разными опциями в дерево каталогов.

## Результат

### Задание 1

**raid0**

```
вероятность выхода из строя одного диска:
p1 = 1%
N = 2

вероятность отказа двух дисков:

p2 = p1 * N = 2%
```

**raid1**

```
вероятность выхода из строя одного диска:
p1 = 1%
N = 2

вероятность отказа двух дисков:

p2 = p1 / N = 0.5%
```

**raid5**

```
вероятность выхода из строя одного диска:
p1 = 1%
N = 4

вероятность отказа двух дисков:

p4 = p1 * (N - 1) = 3%
```

### Задание 2

**raid0**

```
N = 2
hddsize = 20GB

hddsize * N = 40 GB       <---- 100% потеря данных

```

**raid1**

```
N = 2
hddsize = 20GB            <---- равно потере данных одного диска

```

**raid5**

```
N = 4
hddsize = 40GB

(N - 1) * hddsize = 120    <---- 25% потери данных

```

**raid6**

```
N = 4
hddsize = 40GB

(N - 2) * hddsize = 80    <---- 50% потери данных

```

### Задание 3

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw2/resources/LinuxAdm_diagram.png)

* Создадим 4 файла, размером в 1M и преобразуем их в loop устройства:

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw2/resources/LinuxAdm1.png)

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw2/resources/LinuxAdm2.png)

* Добавим их в массив raid5, а loop устройство /dev/loop3 оставим запасным:

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw2/resources/LinuxAdm3.png)

* Сконвертируем raid5 в физический том и создадим группу этих физических томов:

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw2/resources/LinuxAdm4.png)

* Создадим логические тома:

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw2/resources/LinuxAdm5.png)

* Демонстрация физических томов:

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw2/resources/LinuxAdm6.png)

* Демонстрация группы:

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw2/resources/LinuxAdm7.png)

* Демонстрация логических томов:

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw2/resources/LinuxAdm8.png)

* Создадим файловую систему на основе первого логического тома:

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw2/resources/LinuxAdm9.png)

* Смонтируем ее в каталог /mnt:

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw2/resources/LinuxAdm11.png)

* Демонстрация результата при помощи команд lsblk и df -hT

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw2/resources/LinuxAdm10.png)

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw2/resources/LinuxAdm12.png)
