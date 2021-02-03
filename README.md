# Klonowanie paczki

Aby sklonować nasze repozytorium, należy ponownie wejść do lokalizacji catkin-a, przejść do folderu src i sklonować paczke z github-a:

```
$ cd ~/catkin_ws/src
$ git clone git@github.com:GrzegorzStrojny/Turtlebot_SZUM.git
```

Teraz należy zbudować pliki:

```
$ cd ~/catkin_ws
$ catkin_make
```

# Uruchamianie paczki

Aby uruchomić paczke najpierw w każdym uruchamianym terminalu, należy podlinkować plik **setup.bash** w folderu **devel**:

```
source ~/catkin_ws/devel/setup.bash
```

Pierwszą czynnością jest uruchomienie **roscore**:

```
roscore
```

Następnie w nowym terminalu należy odpalić symulacje:

```
rosrun turtlesim turtlesim_node
```

Teraz również w nowym terminalu, aby poruszać robotem należy uruchomić albo plik **move.py** albo **circle.py**:

```
rosrun Turtlebot_SZUM move.py
# albo
rosrun Turtlebot_SZUM circle.py
```