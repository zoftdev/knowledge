---
title: zabbix-session2
tags:
categories:
date: 2024-03-07
lastMod: 2024-03-07
---


## Create trigger & alert #Learning/zabbix


  + use items and function to create problem trigger.

  + how to config smtp.

    ![image.png](/knowledge/assets/image_1707776714370_0.png)

  + [doc trigger](https://www.zabbix.com/documentation/current/en/manual/config/triggers/trigger)

  + alert  [macro](https://www.zabbix.com/documentation/current/en/manual/appendix/macros/supported_by_location)

## Zabbix Items #Learning/zabbix


  + ### summary

    + Host อาจมีทั้ง template และ items เดี่ยวๆ ผสมกัน

  + list of linux keys [linux items keys](https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/zabbix_agent)

  + create item screen


    ![image.png](/knowledge/assets/image_1707716027972_0.png)

  + in case create active agent item behind proxy, need to:

    + reload cache on proxy

      + ((65c98937-2869-4e2c-8bd4-3b36bbd3ec1e))

    + restart agent to retrive new item keys.

    + 

## Zabbix-Agent #Learning/Zabbix


  + ### step

    + install os

    + search zabbix package install

  + ### passive vs active


  + ### auto-add


    + by create alert->action

      + do 3 thing -> add host/ add hostgroup /  add template

## Installing Zabbix-Proxy #Learning/Zabbix


  + screen: add hosts behind proxy


    ![image.png](/knowledge/assets/image_1707706679184_0.png)

    + reload config ``zabbix_proxy  -R config_cache_reload``

      + 

      + 

  + 
