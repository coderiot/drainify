## *drainify* - Record your spotfify stream from pulseaudio.

### Dependencies
 * pulseaudio
 * pulseaudio-utils (command line tools)
 * lame
 * native spotify-client

### Requirements
 * dbus-python (does not support distutils)
 * eyed3d
 * pygobject (does not support distutils)

Notice: You have to install dbus-python and pyobject by your own

### Install dependecies on Ubuntu
```sh
sudo apt-get install pulseaudio-utils dbus-python python-gobject python-eye3d lame
```

### Installation of drainify

```sh
$ pip install -e git+https://github.com/coderiot/drainify.git#egg=drainify
```

### Features
 * split stream into audio files
 * does not record ads
 * id3tags and album art for audio files

### spotify preferences
 * disable gapless playing
 * disable crossfade tracks

### usage
Start spotify before recording.

Call:
```sh
drainify [--dir <MUSIC_DIR>]
```
