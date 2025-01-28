# Discord-Webhook-Proxy
Python based webhook proxy to allow Elastic alerts to be properly formatted for Discord

Steps:
1) Download and replace variables at the top of the script. This includes a url to your security dashboard, listening port, and discord webhook URL.
2) Create connector in ELK pointing to the host running the script. http://<ip_address>:<port>/webhook
3) Create alert action to send notification to webhook.
   To format the data, use the ; character as a delimiter. This will be replaced with a newline.
   Example: "{{date}};Rule: {{rule.name}}; Reason: {{context.alerts.0.signal.reason}}"
   ![image](https://github.com/user-attachments/assets/5a447670-14b0-42aa-8c7e-c5313ff8d181)\



Enjoy your alerts!


![image](https://github.com/user-attachments/assets/9e62e3fd-d22e-4984-9f39-316d7352e3c6)
