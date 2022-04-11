from crontab import CronTab

cron = CronTab()
job = cron.new(command='python update_job.py')
job.day.every(1)
