# Daymoon
Daymoon is a _Telegram_ bot that uses [Ephem](https://rhodesmill.org/pyephem/) 
to calculate sun/moon rise/set (`dm_function.py`). The main code, `dm_sched.py`, 
uses this information to calculate the times of the day that the moon is 
visible in the sky.

The bot is hosted on [Heroku](https://heroku.com/) and is scheduled to run 
everyday at 8am CEST.
`Procfile` defines the process type to Heroku. Please do not modify it.
