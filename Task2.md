Metrics to monitor:

    CPU : Load ,Utilzation and  Memeroy usage
	Server: Disk space usage ,Sever running state and IO Read/Write Statistics
	Network: Network traffic and connection states

How can be Monitored:

Method 1: 

Using Monitioring tools (Nginx ,zabbix)

	1. monitor all the important metrics values and trigger the related alert message through sms or email
	2. Grapical representation of metrics values
  
Method 2: 


Automated script to monitor each metrics and send warning when metric value over expected, then add as a cron job to execute in regular Interval

	1. Customized scripts for disk usage,Memory consumption and N/W Statistics

challenges of monitoring:

	1. Set proper trigger warning value to minimize false alarm
	2. Metrics monitoring tool should not slowdown/affect the server's performance.
  
  
