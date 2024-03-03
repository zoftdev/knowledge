---
title: Learning/zabbix
tags:
categories:
date: 2024-02-18
lastMod: 2024-03-03
---
## Zabbix Learning Map ![image.png](/knowledge/assets/image_1709276775562_0.png) 🗺️ #Learning/Zabbix

  + ### resource

    + https://bestmonitoringtools.com/zabbix-tutorial-for-beginners-a-step-by-step-guide/

    + https://www.amazon.com/Zabbix-Infrastructure-Monitoring-Cookbook-maintaining/dp/180324691X

    + https://www.youtube.com/@DmitryLambert/featured

    + https://trueidc.udemy.com/course/zabbix-monitoring/learn/lecture/20198908#overview

  + ### key

    + Think everything you want to do for monitoring in terms of Host Groups, User Groups and Templates.

  + ### concept

    ![Securing Zabbix 6.0 LTS by Kārlis Saliņš / Zabbix Summit Online 2021 | Noise](https://blog.zabbix.com/wp-content/uploads/2022/01/diagram.png)

    + server

    + agent / active agent

    + proxy

    + web

    + cli-util ( sabbix-send )

  + #### install

    + install server

      + overview step ( video on 2,3,4  [here](https://trueidc.udemy.com/course/zabbix-monitoring/learn/lecture/20198932#overview))

        + search 'zabbix download'

        + run install as describe

        + install db ``apt install mysql-server``

        + [add mysql user zabbix](https://sbcode.net/zabbix/create-initial-database/)

        + install schema

        + start zabbix-server

      + apache+mysql

      ```shell
      sudo apt-get update
      sudo apt-get install apache2 libapache2-mod-php
      sudo apt-get install mysql-server
      sudo apt-get install php php-mbstring php-gd php-xml php-bcmath php-ldap php-mysql libapache2-mod-php
      ```

        + ref — https://tecadmin.net/install-zabbix-on-ubuntu/

        + change timezone

          + ``sudo sed -i 's/;date.timezone =/date.timezone = "Asia\/Bangkok"/' /etc/php/*/apache2/php.ini``

        + continue install

          + at [zabbix download](https://www.zabbix.com/download?zabbix=6.4&os_distribution=ubuntu&os_version=22.04&components=server_frontend_agent&db=mysql&ws=apache)

          + set password

            + ``sudo sed -i 's/# DBPassword=/DBPassword=password/' /etc/zabbix/zabbix_server.conf``

        + all-in-one ( u22 - web + server)

        ```yaml
        set -e
        
        # https://tecadmin.net/install-zabbix-on-ubuntu/
        sudo apt-get update
        sudo apt-get install apache2 libapache2-mod-php -y 
        sudo apt-get install mysql-server -y
        sudo apt-get install php php-mbstring php-gd php-xml php-bcmath php-ldap php-mysql libapache2-mod-php -y
        sudo sed -i 's/;date.timezone =/date.timezone = "Asia\/Bangkok"/' /etc/php/*/apache2/php.ini
        
        #https://www.zabbix.com/download?zabbix=6.4&os_distribution=ubuntu&os_version=22.04&components=server_frontend_agent&db=mysql&ws=apache
        wget https://repo.zabbix.com/zabbix/6.4/ubuntu/pool/main/z/zabbix-release/zabbix-release_6.4-1+ubuntu22.04_all.deb
        sudo dpkg -i zabbix-release_6.4-1+ubuntu22.04_all.deb
        sudo apt update
        sudo apt install zabbix-server-mysql zabbix-frontend-php zabbix-apache-conf zabbix-sql-scripts zabbix-agent -y
        
        #create user
        sudo mysql -u root -ppassword   <<EOF
        
        create database zabbix character set utf8mb4 collate utf8mb4_bin;
        create user zabbix@localhost identified by 'password';
        grant all privileges on zabbix.* to zabbix@localhost;
        set global log_bin_trust_function_creators = 1;
        FLUSH PRIVILEGES;
        quit;
        EOF
        
        zcat /usr/share/zabbix-sql-scripts/mysql/server.sql.gz | mysql --default-character-set=utf8mb4 -uzabbix -ppassword zabbix
        
        #end sql
        mysql -u root -ppassword   <<EOF
        set global log_bin_trust_function_creators = 0;
        EOF
        
        sudo sed -i 's/# DBPassword=/DBPassword=password/' /etc/zabbix/zabbix_server.conf
        systemctl restart zabbix-server zabbix-agent apache2
        systemctl enable zabbix-server zabbix-agent apache2
        
        curl http://localhost/zabbix/
        ```

    + Installing Zabbix Agents - https://tecadmin.net/install-zabbix-agent-on-ubuntu-and-debian

    ```shell
    #https://www.zabbix.com/download?zabbix=6.4&os_distribution=ubuntu&os_version=22.04&components=server_frontend_agent&db=mysql&ws=apache
    wget https://repo.zabbix.com/zabbix/6.4/ubuntu/pool/main/z/zabbix-release/zabbix-release_6.4-1+ubuntu22.04_all.deb
    sudo dpkg -i zabbix-release_6.4-1+ubuntu22.04_all.deb
    sudo apt update
    
    sudo apt-get install zabbix-agent
    sudo sed -i 's/Server=127.0.0.1/Server=10.10.68.1/' /etc/zabbix/zabbix_agentd.conf
    sudo sed -i 's/Hostname=Zabbix server/Hostname=68-2/' /etc/zabbix/zabbix_agentd.conf
    sudo systemctl enable zabbix-agent 
    sudo systemctl start zabbix-agent 
    ```

    + Adding Host in Zabbix Server to Monitor — https://tecadmin.net/add-host-zabbix-server-monitor

  + #### hostgroup

    + ``#LearningPaths, #staging, #live, #database, #mongodb, #appserver, #search.``

  + #### template -> hostgroup user

    + os,mongodb,elasticsearch

    + example

      + https://github.com/omni-lchen/zabbix-mongodb

      + [https://github.com/zarplata/zabbix-agent-extension-elasticsearch](https://github.com/zarplata/zabbix-agent-extension-elasticsearch)

  + #### sabbix send

    + Or use using zabbix-send  : Item type `trapper`

      + send to server

        + ``sudo apt-get install zabbix-sender``

        + ``zabbix_sender -vv -z [serverIp] -p 10051 -s [clientName] -k traptest -o "Test value"``

          ![image.png](/knowledge/assets/image_1709368312975_0.png)

          + 

          + 

  + #### ping agent

    + check port

      + server ``telnet ip-of-your-agent 10050``

      + agent

      ```
      sudo apt install zabbix-get
      zabbix_get -s ip-of-your-agent -k agent.ping  
      zabbix_get -s ip-of-your-agent -k agent.version  
      zabbix_get -s ip-of-your-agent -k agent.hostname
      ```

  + #### notification

    + use sendgrid with Zabbix

      + [sendgrid_zabbix_alert](https://github.com/mkgin/sendgrid_zabbix_alert)

    + default not work well

  + #### customize item/trigger (shuld be to template)

    + [config/items/item](https://www.zabbix.com/documentation/3.4/manual/config/items/item)

    + [config/triggers/trigger](https://www.zabbix.com/documentation/3.4/manual/config/triggers/trigger)

  + ### link

    + network [how-to-monitor-cisco-switch-or-router-with-zabbix/](https://bestmonitoringtools.com/how-to-monitor-cisco-switch-or-router-with-zabbix/)

    + [overview (gen this map)](https://medium.com/@gokulnk/understanding-zabbix-f2a83eeb1221)

    + demo [https://zabbix.org/zabbix/index.php](https://zabbix.org/zabbix/index.php) and “sign in as guest”.
