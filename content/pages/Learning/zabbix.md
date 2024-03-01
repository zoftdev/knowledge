---
title: Learning/zabbix
tags:
categories:
date: 2024-02-18
lastMod: 2024-03-01
---
## Zabbix Learning Map ![image.png](/knowledge/assets/image_1709276775562_0.png) 🗺️ #Learning/Zabbix11

  + ### key

    + Think everything you want to do for monitoring in terms of Host Groups, User Groups and Templates.

  + ### component

    ![Securing Zabbix 6.0 LTS by Kārlis Saliņš / Zabbix Summit Online 2021 | Noise](https://blog.zabbix.com/wp-content/uploads/2022/01/diagram.png)

    + server

    + agent

    + proxy

    + web

  + ### monitor

    + network [how-to-monitor-cisco-switch-or-router-with-zabbix/](https://bestmonitoringtools.com/how-to-monitor-cisco-switch-or-router-with-zabbix/)

  + ### to-lean

    + #### install

      + Installing the Zabbix Server — https://tecadmin.net/install-zabbix-on-ubuntu/
Installing Zabbix Agents -https://tecadmin.net/install-zabbix-agent-on-ubuntu-and-debian
Adding Host in Zabbix Server to Monitor — https://tecadmin.net/add-host-zabbix-server-monitor

    + #### hostgroup

      + ``#LearningPaths, #staging, #live, #database, #mongodb, #appserver, #search.``

    + #### template -> hostgroup user

      + os,mongodb,elasticsearch

      + example


        + https://github.com/omni-lchen/zabbix-mongodb

        + [https://github.com/zarplata/zabbix-agent-extension-elasticsearch](https://github.com/zarplata/zabbix-agent-extension-elasticsearch)

    + #### debuging

      + ##### check port

        + server ``telnet ip-of-your-agent 10050``

        + agent


        ```
        apt install zabbix-get
        zabbix_get -s ip-of-your-agent -k agent.ping  
        zabbix_get -s ip-of-your-agent -k agent.version  
        zabbix_get -s ip-of-your-agent -k agent.hostname
        ```

    + #### active agent


      + using zabbix-send  : Item type `trapper`

        + server-> agent  ``telnet ip-of-your-server 10050``

        + send to server

          + ``sudo apt-get install zabbix-sender``

          + ``zabbix_sender -vv -z [serverIp] -p 10051 -s [clientName] -k traptest -o "Test value"``

    + #### report

      + screens


        + . In Zabbix, a "screen" is a user-defined layout that can display multiple data elements, such as graphs, maps, plain text values, etc., on a single page. This feature allows users to create a customized dashboard

    + #### notification

      + use sendgrid with Zabbix

        + [sendgrid_zabbix_alert](https://github.com/mkgin/sendgrid_zabbix_alert)

      + default not work well

    + #### customize item/trigger (shuld be to template)

      + [config/items/item](https://www.zabbix.com/documentation/3.4/manual/config/items/item)

      + [config/triggers/trigger](https://www.zabbix.com/documentation/3.4/manual/config/triggers/trigger)

  + ### link

    + [overview (gen this map)](https://medium.com/@gokulnk/understanding-zabbix-f2a83eeb1221)

    + demo [https://zabbix.org/zabbix/index.php](https://zabbix.org/zabbix/index.php) and “sign in as guest”.
