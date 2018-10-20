##
#
#   This data file holds basic commands for ssh and telnet.
#
#   Note: important to add date variable because a hacher will ensure the server shows the current date
#   Note: Shows correct output for date
#
##

import time
import datetime


todaysdate = time.strftime("%a %b %d %H:%M:%S %Y")

ssh_commands = {
        'ls': 'Servers  Databases   Top_Secret  Documents',
        'ifconfig': 'lo: flags=75<UP,LOOPBACK,RUNNING> mtu 43386' \
                    '\n     inet 127.0.0.1 netmask 255.0.0.0' \
                    '\n     inet6 ::1 prefixlen 128 scopeid 0x10<host>' \
                    '\n     loop txquuelen 1000 (Local Loopback)' \
                    '\n     RX packets 4840 bytes 385124 (376.0 KiB)' \
                    '\n     RX errors 0 dropped 0 overruns 0 frame 0' \
                    '\n     TX packets 4840 bytes 364914 (447.0 KiB)' \
                    '\n     TX errors dropped 0 overruns 0 carrier 0 collisions 0'\
                    '\n\n     -------TEST---TEST----TEST-----TEST---------------------',
            
        'date': todaysdate,
        'whoami': 'root',
        'netstat':  'Active Internet connections (w/o servers)' \
                    '\nProto Recv-Q Send-Q Local Address           Foreign Address         State' \
                    '\ntcp        0      0 localhost:51631         localhost:56104         ESTABLISHED' \
                    '\ntcp        0      0 localhost:60638         wf.networksolution:http TIME_WAIT' \
                    '\ntcp        0      0 localhost:42045         localhost:33768         ESTABLISHED' \
                    '\ntcp        0      0 localhost:34126         108.177.111.155:https   ESTABLISHED' \
                    '\ntcp        0      0 localhost:51847         localhost:54690         ESTABLISHED' \
                    '\ntcp        0      0 localhost:35614         188.55.190.35.bc.:https ESTABLISHED' \
                    '\ntcp        0      0 localhost:33745         localhost:40416         ESTABLISHED' \
                    '\ntcp        0      0 localhost:54690         localhost:51847         ESTABLISHED' \
                    '\ntcp        0      0 localhost:56104         localhost:51631         ESTABLISHED' \
                    '\ntcp        0      0 localhost:36219         localhost:37602         ESTABLISHED' \
                    '\ntcp        0      0 localhost:33768         localhost:42045         ESTABLISHED' \
                    '\ntcp        0      0 localhost:38395         localhost:38498         ESTABLISHED' \
                    '\ntcp        0      0 localhost:39459         localhost:48496         ESTABLISHED' \
                    '\ntcp        0      0 localhost:43453         localhost:42296         ESTABLISHED' \
                    '\ntcp        0      0 localhost:42216         localhost:60961         ESTABLISHED' \
                    '\ntcp        0      0 localhost:48496         localhost:39459         ESTABLISHED' \
                    '\ntcp        0      0 localhost:38770         localhost:54313         ESTABLISHED' \
                    '\ntcp        0      0 localhost:40416         localhost:33745         ESTABLISHED' \
                    '\ntcp        0      0 localhost:60961         localhost:42216         ESTABLISHED' \
                    '\ntcp        0      0 localhost:37602         localhost:36219         ESTABLISHED' \
                    '\ntcp        0      0 localhost:42296         localhost:43453         ESTABLISHED' \
                    '\ntcp        0      0 localhost:54313         localhost:38770         ESTABLISHED' \
                    '\ntcp        0      0 localhost:59180         65.66.190.35.bc.g:https ESTABLISHED' \
                    '\ntcp        0      0 localhost:38498         localhost:38395         ESTABLISHED' \
                    '\ntcp6       0      0 localhost:43510         ik-in-x65.1e100.n:https ESTABLISHED' \
                    '\ntcp6       0      0 localhost:37046         sfo03s18-in-x04.1:https ESTABLISHED' \
                    '\ntcp6       0      0 localhost:38278         2607:f8b0:4001:c1:https ESTABLISHED' \
                    '\ntcp6       0      0 localhost:40212         2607:f8b0:4001:c1:https ESTABLISHED' \
                    '\ntcp6       0      0 localhost:32838         2607:f8b0:4001:c1:https ESTABLISHED' \
                    '\ntcp6       0      0 localhost:54650         2607:f8b0:4001:c0:https ESTABLISHED' \
                    '\ntcp6       0      0 localhost:57074         2607:f8b0:4001:c1:https ESTABLISHED' \
                    '\ntcp6       0      0 localhost:41774         ik-in-x84.1e100.n:https ESTABLISHED' \
                    '\ntcp6       0      0 localhost:47584         jd-in-x5e.1e100.n:https ESTABLISHED' \
                    '\ntcp6       0      0 localhost:41178         2607:f8b0:4001:c1:https ESTABLISHED' \
                    '\ntcp6       0      0 localhost:36818         2607:f8b0:4001:c0:https ESTABLISHED' \
                    '\nActive UNIX domain sockets (w/o servers)' \
                    '\nProto RefCnt Flags       Type       State         I-Node   Path' \
                    '\nunix  18     [ ]         DGRAM                    13596    /run/systemd/journal/dev-log' \
                    '\nunix  2      [ ]         DGRAM                    3669063  /run/wpa_supplicant/wlan0' \
                    '\nunix  2      [ ]         DGRAM                    3669068  /run/wpa_supplicant/p2p-dev-wlan0' \
                    '\nunix  2      [ ]         DGRAM                    23416    /run/user/0/systemd/notify' \
                    '\nunix  2      [ ]         DGRAM                    13176    /run/user/131/systemd/notify' \
                    '\nunix  2      [ ]         DGRAM                    14479    /run/systemd/journal/syslog' \
                    '\nunix  3      [ ]         DGRAM                    16862    /run/systemd/notify' \
                    '\nunix  8      [ ]         DGRAM                    16893    /run/systemd/journal/socket' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     28148    /run/user/0/bus' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     15319    /run/systemd/journal/stdout' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     13226    @/tmp/.X11-unix/X0' \
                    '\nunix  3      [ ]         DGRAM                    14013    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     31251    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     27841    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     3676259  ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     25178    /run/user/0/bus' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     24170    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     18291    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     27212    /run/systemd/journal/stdout' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     30300    /var/run/dbus/system_bus_socket' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     28174    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     23219    @/tmp/dbus-CqGYXjGU' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     23999    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     29994    ' \
                    '\nunix  2      [ ]         SEQPACKET  CONNECTED     3824104  ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     31284    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     24398    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     24334    /run/systemd/journal/stdout' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     25967    ' \
                    '\nunix  2      [ ]         DGRAM                    23701    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     21575    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     3931512  ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     3090558  /run/systemd/journal/stdout' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     26153    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     31069    /run/user/0/bus' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     22522    /run/user/131/bus' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     15318    /run/systemd/journal/stdout' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     24623    ' \
                    '\nunix  2      [ ]         DGRAM                    19373    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     25125    /run/systemd/journal/stdout' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     30966    /run/user/0/bus' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     27867    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     3677056  ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     29293    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     29170    ' \
                    '\nunix  3      [ ]         DGRAM                    15600    ' \
                    '\nunix  2      [ ]         DGRAM                    3665758  ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     24962    /run/user/0/bus' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     25662    /var/run/dbus/system_bus_socket' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     23785    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     3673632  ' \
                    '\nunix  2      [ ]         DGRAM                    26754    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     17400    /run/systemd/journal/stdout' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     3675266  /run/user/0/bus' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     29194    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     31071    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     29001    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     22579    /run/systemd/journal/stdout' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     24966    /run/user/0/bus' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     27796    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     24061    /run/systemd/journal/stdout' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     18389    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     12999    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     25121    /run/systemd/journal/stdout' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     27031    /run/systemd/journal/stdout' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     22431    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     19362    /var/run/dbus/system_bus_socket' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     14187    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     19348    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     28173    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     29707    /run/user/131/bus' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     19355    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     27881    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     26872    /run/user/131/pulse/native' \
                    '\nunix  3      [ ]         DGRAM                    13178    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     3677053  ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     3088020  ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     24330    /run/systemd/journal/stdout' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     24122    @/tmp/.X11-unix/X1' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     28147    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     27020    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     26839    /run/systemd/journal/stdout' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     27649    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     23743    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     14024    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     2351422  /run/user/0/bus' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     29861    @/tmp/dbus-LJASGREu' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     13182    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     19778    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     3676249  ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     3089201  /var/run/dbus/system_bus_socket' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     24321    /run/systemd/journal/stdout' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     27847    ' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     30219    /run/user/0/bus' \
                    '\nunix  3      [ ]         STREAM     CONNECTED     27656    /run/systemd/journal/stdout',

        'find': ' ',
        'ping': ' ',
        'nslookup': '         ',
        'ps': '\nPID TTY          TIME CMD' \
                '\n  831 tty1     00:00:01 Xorg' \
                '\n  839 tty1     00:00:00 gnome-session-b' \
                '\n  861 tty1     00:00:13 gnome-shell' \
                '\n 1004 tty1     00:00:07 gsd-xsettings' \
                '\n 1006 tty1     00:00:00 gsd-a11y-settin' \
                '\n 1009 tty1     00:00:03 gsd-clipboard' \
                '\n 1010 tty1     00:00:13 gsd-color' \
                '\n1012 tty1     00:00:00 gsd-datetime' \
                '\n 1015 tty1     00:00:00 gsd-housekeepin' \
                '\n 1016 tty1     00:00:03 gsd-keyboard' \
                '\n 1021 tty1     00:00:03 gsd-media-keys' \
                '\n 1022 tty1     00:00:00 gsd-mouse' \
                '\n 1026 tty1     00:00:03 gsd-power' \
                '\n1032 tty1     00:00:00 gsd-print-notif' \
                '\n 1033 tty1     00:00:00 gsd-rfkill' \
                '\n 1039 tty1     00:00:00 gsd-screensaver' \
                '\n 1041 tty1     00:00:00 gsd-sharing' \
                '\n 1042 tty1     00:00:00 gsd-smartcard' \
                '\n 1048 tty1     00:00:00 gsd-sound' \
                '\n 1056 tty1     00:00:03 gsd-wacom' \
                '\n 1153 tty2     00:13:49 Xorg' \
                '\n 1162 tty2     00:00:00 gnome-session-b' \
                '\n 1246 tty2     00:24:34 gnome-shell' \
                '\n 1353 tty2     00:00:05 gsd-power' \
                '\n 1355 tty2     00:00:00 gsd-print-notif' \
                '\n 1356 tty2     00:00:00 gsd-rfkill' \
                '\n 1357 tty2     00:00:00 gsd-screensaver' \
                '\n 1358 tty2     00:00:21 gsd-sharing' \
                '\n 1359 tty2     00:00:00 gsd-smartcard' \
                '\n 1365 tty2     00:00:00 gsd-sound' \
                '\n 1371 tty2     00:00:08 gsd-xsettings' \
                '\n 1375 tty2     00:00:04 gsd-wacom' \
                '\n 1385 tty2     00:00:00 gsd-a11y-settin' \
                '\n 1386 tty2     00:00:04 gsd-clipboard' \
                '\n 1389 tty2     00:00:16 gsd-color' \
                '\n 1392 tty2     00:00:00 gsd-datetime' \
                '\n 1394 tty2     00:00:00 gsd-housekeepin' \
                '\n 1397 tty2     00:00:04 gsd-keyboard' \
                '\n 1402 tty2     00:00:04 gsd-media-keys' \
                '\n 1403 tty2     00:00:00 gsd-mouse' \
                '\n 1417 tty2     00:00:00 gsd-printer' \
                '\n 1460 tty2     00:00:00 gsd-disk-utilit' \
                '\n 1462 tty2     00:00:12 gnome-software' \
                '\n 1468 tty2     00:00:04 tracker-miner-f' \
                '\n 1469 tty2     00:00:02 tracker-extract' \
                '\n 1471 tty2     00:00:04 evolution-alarm' \
                '\n 1476 tty2     00:00:00 tracker-miner-a' \
                '\n 3627 tty2     00:37:01 firefox-esr' \
                '\n 3788 tty2     00:03:30 Web Content' \
                '\n 4101 tty2     01:18:47 Web Content' \
                '\n 6289 tty2     00:04:44 Web Content' \
                '\n 6332 tty2     00:07:45 Web Content' \
                '\n10009 pts/1    00:00:03 vim' \
                '\n10126 pts/2    00:00:00 ps',

        'ps -a': '\nPID TTY          TIME CMD' \
                '\n  831 tty1     00:00:01 Xorg' \
                '\n  839 tty1     00:00:00 gnome-session-b' \
                '\n  861 tty1     00:00:13 gnome-shell' \
                '\n 1004 tty1     00:00:07 gsd-xsettings' \
                '\n 1006 tty1     00:00:00 gsd-a11y-settin' \
                '\n 1009 tty1     00:00:03 gsd-clipboard' \
                '\n 1010 tty1     00:00:13 gsd-color' \
                '\n1012 tty1     00:00:00 gsd-datetime' \
                '\n 1015 tty1     00:00:00 gsd-housekeepin' \
                '\n 1016 tty1     00:00:03 gsd-keyboard' \
                '\n 1021 tty1     00:00:03 gsd-media-keys' \
                '\n 1022 tty1     00:00:00 gsd-mouse' \
                '\n 1026 tty1     00:00:03 gsd-power' \
                '\n1032 tty1     00:00:00 gsd-print-notif' \
                '\n 1033 tty1     00:00:00 gsd-rfkill' \
                '\n 1039 tty1     00:00:00 gsd-screensaver' \
                '\n 1041 tty1     00:00:00 gsd-sharing' \
                '\n 1042 tty1     00:00:00 gsd-smartcard' \
                '\n 1048 tty1     00:00:00 gsd-sound' \
                '\n 1056 tty1     00:00:03 gsd-wacom' \
                '\n 1153 tty2     00:13:49 Xorg' \
                '\n 1162 tty2     00:00:00 gnome-session-b' \
                '\n 1246 tty2     00:24:34 gnome-shell' \
                '\n 1353 tty2     00:00:05 gsd-power' \
                '\n 1355 tty2     00:00:00 gsd-print-notif' \
                '\n 1356 tty2     00:00:00 gsd-rfkill' \
                '\n 1357 tty2     00:00:00 gsd-screensaver' \
                '\n 1358 tty2     00:00:21 gsd-sharing' \
                '\n 1359 tty2     00:00:00 gsd-smartcard' \
                '\n 1365 tty2     00:00:00 gsd-sound' \
                '\n 1371 tty2     00:00:08 gsd-xsettings' \
                '\n 1375 tty2     00:00:04 gsd-wacom' \
                '\n 1385 tty2     00:00:00 gsd-a11y-settin' \
                '\n 1386 tty2     00:00:04 gsd-clipboard' \
                '\n 1389 tty2     00:00:16 gsd-color' \
                '\n 1392 tty2     00:00:00 gsd-datetime' \
                '\n 1394 tty2     00:00:00 gsd-housekeepin' \
                '\n 1397 tty2     00:00:04 gsd-keyboard' \
                '\n 1402 tty2     00:00:04 gsd-media-keys' \
                '\n 1403 tty2     00:00:00 gsd-mouse' \
                '\n 1417 tty2     00:00:00 gsd-printer' \
                '\n 1460 tty2     00:00:00 gsd-disk-utilit' \
                '\n 1462 tty2     00:00:12 gnome-software' \
                '\n 1468 tty2     00:00:04 tracker-miner-f' \
                '\n 1469 tty2     00:00:02 tracker-extract' \
                '\n 1471 tty2     00:00:04 evolution-alarm' \
                '\n 1476 tty2     00:00:00 tracker-miner-a' \
                '\n 3627 tty2     00:37:01 firefox-esr' \
                '\n 3788 tty2     00:03:30 Web Content' \
                '\n 4101 tty2     01:18:47 Web Content' \
                '\n 6289 tty2     00:04:44 Web Content' \
                '\n 6332 tty2     00:07:45 Web Content' \
                '\n10009 pts/1    00:00:03 vim' \
                '\n10126 pts/2    00:00:00 ps',

        'vi /etc/shadow': '\nroot:$1$/avpfBJ1$x0z8w5UF9Iv./DR9E9Lid.:14747:0:99999:7:::' \
                            '\ndaemon:*:14684:0:99999:7:::' \
                            '\nbin:*:14684:0:99999:7:::' \
                            '\nsys:$1$fUX6BPOt$Miyc3UpOzQJqz4s5wFD9l0:14742:0:99999:7:::' \
                            '\nsync:*:14684:0:99999:7:::' \
                            '\ngames:*:14684:0:99999:7:::' \
                            '\nman:*:14684:0:99999:7:::' \
                            '\nlp:*:14684:0:99999:7:::' \
                            '\nmail:*:14684:0:99999:7:::' \
                            '\nnews:*:14684:0:99999:7:::' \
                            '\nuucp:*:14684:0:99999:7:::' \
                            '\nproxy:*:14684:0:99999:7:::' \
                            '\nwww-data:*:14684:0:99999:7:::' \
                            '\nbackup:*:14684:0:99999:7:::' \
                            '\nlist:*:14684:0:99999:7:::' \
                            '\nirc:*:14684:0:99999:7:::' \
                            '\ngnats:*:14684:0:99999:7:::' \
                            '\nnobody:*:14684:0:99999:7:::' \
                            '\nlibuuid:!:14684:0:99999:7:::' \
                            '\ndhcp:*:14684:0:99999:7:::' \
                            '\nsyslog:*:14684:0:99999:7:::' \
                            '\nklog:$1$f2ZVMS4K$R9XkI.CmLdHhdUE3X9jqP0:14742:0:99999:7:::' \
                            '\nsshd:*:14684:0:99999:7:::' \
                            '\nmsfadmin:$1$XN10Zj2c$Rt/zzCW3mLtUWA.ihZjA5/:14684:0:99999:7:::' \
                            '\nbind:*:14685:0:99999:7:::' \
                            '\npostfix:*:14685:0:99999:7:::' \
                            '\nftp:*:14685:0:99999:7:::' \
                            '\npostgres:$1$Rw35ik.x$MgQgZUuO5pAoUvfJhfcYe/:14685:0:99999:7:::' \
                            '\nmysql:!:14685:0:99999:7:::' \
                            '\ntomcat55:*:14691:0:99999:7:::' \
                            '\ndistccd:*:14698:0:99999:7:::' \
                            '\nuser:$1$HESu9xrH$k.o3G93DGoXIiQKkPmUgZ0:14699:0:99999:7:::' \
                            '\nservice:$1$kR3ue7JZ$7GxELDupr5Ohp6cjZ3Bu//:14715:0:99999:7:::' \
                            '\ntelnetd:*:14715:0:99999:7:::' \
                            '\nproftpd:!:14727:0:99999:7:::' \
                            '\nstatd:*:15474:0:99999:7:::' \
                            '\nsnmp:*:15480:0:99999:7:::' \
                            '\nskywalker:$1$OHklYwhp$vwtbf4vho8RcuLUlYv9rL1:17741:0:99999:7:::' ,
        
        'vi /etc/passwd': '\nroot:x:0:0:root:/root:/bin/bash' \
                            '\ndaemon:x:1:1:daemon:/usr/sbin:/bin/sh' \
                            '\nbin:x:2:2:bin:/bin:/bin/sh' \
                            '\nsys:x:3:3:sys:/dev:/bin/sh' \
                            '\nsync:x:4:65534:sync:/bin:/bin/sync' \
                            '\ngames:x:5:60:games:/usr/games:/bin/sh' \
                            '\nman:x:6:12:man:/var/cache/man:/bin/sh' \
                            '\nlp:x:7:7:lp:/var/spool/lpd:/bin/sh' \
                            '\nmail:x:8:8:mail:/var/mail:/bin/sh' \
                            '\nnews:x:9:9:news:/var/spool/news:/bin/sh' \
                            '\nuucp:x:10:10:uucp:/var/spool/uucp:/bin/sh' \
                            '\nproxy:x:13:13:proxy:/bin:/bin/sh' \
                            '\nwww-data:x:33:33:www-data:/var/www:/bin/sh' \
                            '\nbackup:x:34:34:backup:/var/backups:/bin/sh' \
                            '\nlist:x:38:38:Mailing List Manager:/var/list:/bin/sh' \
                            '\nirc:x:39:39:ircd:/var/run/ircd:/bin/sh' \
                            '\ngnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh' \
                            '\nnobody:x:65534:65534:nobody:/nonexistent:/bin/sh' \
                            '\nlibuuid:x:100:101::/var/lib/libuuid:/bin/sh' \
                            '\ndhcp:x:101:102::/nonexistent:/bin/false' \
                            '\nsyslog:x:102:103::/home/syslog:/bin/false' \
                            '\nklog:x:103:104::/home/klog:/bin/false' \
                            '\nsshd:x:104:65534::/var/run/sshd:/usr/sbin/nologin' \
                            '\nmsfadmin:x:1000:1000:msfadmin,,,:/home/msfadmin:/bin/bash' \
                            '\nbind:x:105:113::/var/cache/bind:/bin/false' \
                            '\npostfix:x:106:115::/var/spool/postfix:/bin/false' \
                            '\nftp:x:107:65534::/home/ftp:/bin/false' \
                            '\npostgres:x:108:117:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash' \
                            '\nmysql:x:109:118:MySQL Server,,,:/var/lib/mysql:/bin/false' \
                            '\ntomcat55:x:110:65534::/usr/share/tomcat5.5:/bin/false' \
                            '\ndistccd:x:111:65534::/:/bin/false' \
                            '\nuser:x:1001:1001:just a user,111,,:/home/user:/bin/bash' \
                            '\nservice:x:1002:1002:,,,:/home/service:/bin/bash' \
                            '\ntelnetd:x:112:120::/nonexistent:/bin/false' \
                            '\nproftpd:x:113:65534::/var/run/proftpd:/bin/false' \
                            '\nstatd:x:114:65534::/var/lib/nfs:/bin/false' \
                            '\nsnmp:x:115:65534::/var/lib/snmp:/bin/false' \
                            '\nskywalker:x:1003:1003::/home/skywalker:/bin/sh',


        }



