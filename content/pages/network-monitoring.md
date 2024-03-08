---
title: network-monitoring
tags:
categories:
date: 2024-03-07
lastMod: 2024-03-07
---


## Monitor Network #Learning/Zabbix

  + from https://bestmonitoringtools.com/how-to-monitor-cisco-switch-or-router-with-zabbix/

  ```yaml
  configure Zabbix to monitor network traffic (bandwidth), CPU utilization, power supply and serial numbers on Cisco switches and routers that use classic IOS (like Cisco Catalyst 3650, 3750, 3850, 2960, 2950, 2801, 2911 or routers 1841, 1921, etc.).
  
  Keep in mind that you can also use this tutorial for montoring routers that use IOS-XR (like CRS series, 12000 series, and ASR9000 series, etc.) or Nexus switches (like series 7000, 9000, etc. )
  ```

  + monitor Cisco switch and router with SNMP protocol

  + ### smnp

    + ref [what-is-snmp-protocol](https://bestmonitoringtools.com/what-is-snmp-protocol-learn-step-by-step-manager-agent-mib-oid/)

    + #### flow

      ![image.png](/knowledge/assets/image_1707702709060_0.png)

      + **SNMP uses UDP port 161 **for sending request and response message types **and UDP port 162 for sending traps and informs**.

    + which stands for Simple Network Management Protocol, is a communication protocol that allows *discovery, monitoring, and configuration*

    + de facto standard in network and system monitoring

    + **manager  (nms)**query to **agent.**

    + #### manager can

      + discovery

      + monitor

      + manage

      + alarm

      + gui with show history

    + #### use case

      + monitor inbound and outbound traffic flowing through the device;

      + os resource/process

      + access/configure

    + polling

      + ``snmpget -v2c  -c public 127.0.0.1 1.3.6.1.2.1.1.1``

    + manager

      + zabbix

      + Other honorable mentions are [Prometheus](https://prometheus.io/) in combination with [Grafana](https://grafana.com/), or [Icinga](https://icinga.com/), [LibreNMS](https://www.librenms.org/), [OpenNMS](https://www.opennms.com/), [Nagios Core](https://www.nagios.org/projects/nagios-core/).
