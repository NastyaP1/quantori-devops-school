## Описание

Скачайте свежую версию исходников git. Скомпилируйте и инсталлируйте в каталог /usr/local. Убедитесь, что свежая версия установлена и готова к использованию.

## Результат

Для начала необходимо скачать последнюю версию git:

```
wget https://github.com/git/git/archive/v2.32.0.zip
```

Распаковать zip пакет:

```
unzip v2.32.0.zip
```

Перейти в папку git:

```
cd git-2.32.0
```

Сборка программы git:

```
make prefix=/usr/local all
```

Установаить программу git:

```
sudo make prefix=/usr/local install
```

Настройка git:

```
git config --global user.name <username>

git config --global user.email <email>

```

---

**Демонстрация проверки git**

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw1/resources/LinuxAdm1.png)
