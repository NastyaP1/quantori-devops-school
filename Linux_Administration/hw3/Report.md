## Описание

Прислать мне бинарный файл защищенный паролем, объемом не более 2 мегабайт. И сам пароль. Используя программы из пакета GNUPG и пароль, я должен иметь возможность смонтировать полученный файл через /dev/loop в свое дерево каталогов. Внутри полученного каталога рассчитываю увидеть текстовый файл с контрольной фразой.

## Результат

==========================================================================================

Бинарный файл находится здесь: [file](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw3/files/file.fs.gpg)

Пароль: ananas

==========================================================================================

Для начала создадим файл, заполненный нулями, размером в 1M

```
dd if=/dev/zero of=file.fs bs=1M count=1
```

Далее создадим файловую систему:

```
mkfs.ext2 -F file.fs
```

Смонтируем файловую систему:

```
sudo mount -t ext4 -o loop file.fs /mnt/disk
```

Создадим текстовый файл с кодовой фразовой и положим его в /mnt/disk:

```
echo "<message>" > message.txt
```

Отмонтируем файл:

```
sudo umount /mnt/disk
```

Зашифруем файл и введем пароль:

```
gpg -c file.fs

// введем пароль ananas
```

Для проверки расшифруем бинарный файл file.fs.gpg, снова смонтируем в систему и прочитаем текстовый файл:

```
gpg file.fs.gpg
// введем пароль ananas

sudo mount -t ext2 -o loop file.fs /mnt/disk

cat /mnt/disk/message.txt
```

**Демонстрация**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw3/resources/LinuxAdm1.png)

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw3/resources/LinuxAdm2.png)

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw3/resources/LinuxAdm3.png)

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw3/resources/LinuxAdm4.png)

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw3/resources/LinuxAdm5.png)

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw3/resources/LinuxAdm6.png)

