# Daymoon
Daymoon is a _Telegram_ bot that uses [Ephem](https://rhodesmill.org/pyephem/) 
to calculate sun/moon rise/set (`daymoon` function). it uses this information 
to calculate the times of the day that the moon is visible in the sky.
`weather` function gets the +3 hour forecast of the cloud coverage from 
[OpenWeatherMap](https://openweathermap.org) and if that is < 50%, it returns cloud 
coverage message.
The main code, `dm_sched.py`, uses [APScheduler](https://apscheduler.readthedocs.io/en/latest/)
to do the calculations at 8 am everyday.

The bot is hosted on [Heroku](https://heroku.com/) and is scheduled to run 
everyday at 8am CEST.
`Procfile` defines the process type to Heroku. Please do not modify it.
