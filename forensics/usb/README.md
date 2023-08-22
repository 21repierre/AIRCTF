# USB

## Description

Un de nos agents nous a transmis cette clé USB mais nous n'arrivons pas a déterminer le contenu de celle-ci, aidez nous!

- Resources: [usb.img](usb.img)
- Difficulté: facile/moyen

## Fonctionnement

Exploration en local

## Solve

Avec `file usb.img` on sait qu'on a une image disque.
On utilise `fdisk -l usb/img` pour avoir des informations sur les partitions:
```
Disk usb.img: 64 MiB, 67108864 bytes, 131072 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x61856374

Device     Boot Start    End Sectors Size Id Type
usb.img1         2048 131071  129024  63M  7 HPFS/NTFS/exFAT
```

Une seule partition, on va la monter pour chercher dedans: 

```bash
mkdir /tmp/usb_mount
sudo mount -o loop,offset=1048576 usb.img /tmp/usb_mount
```
L'offset est calculé comme ceci: $start \times sector\_size = 2048 \times 512 = 1048576$
On peut donc lister les fichiers: `ls -al /tmp/usb_mount`
On tombe sur un seul fichier `petit_poney.png` qui ne s'ouvre pas comme PNG.
A l'aide de `file petit_poney.png` on se rend compte que c'est en réalité une archive ZIP.
L'ouvrir comme archive nous donne un fichier `flag.txt` avec `AIRCTF{d3LEte_1S_a_LIE}`.