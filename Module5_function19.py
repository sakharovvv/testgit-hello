def log_filter(logs_strintg, log_level):
   for line in logs_strintg.split('\n'):
      if line and log_level in line:
         yield line.strip()


logs = """\
2023-08-15 14:15:24 INFO Starting the system.
2023-08-15 14:15:26 WARN System load is above 80%.
2023-08-15 14:15:27 ERROR Failed to connect to database.
2023-08-15 14:15:28 INFO Connection retry in 5 seconds.
"""

for log in log_filter(logs, 'ERROR'):
   print(log)

# 2023-08-15 14:15:27 ERROR Failed to connect to database. new changes123
