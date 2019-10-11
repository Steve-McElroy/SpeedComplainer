# SpeedComplainer
Python scripts for running speed tests, generating statistics and tweeting at your service provider if desired

# Dependencies
* Speedtest CLI - https://github.com/sivel/speedtest-cli
* NumPy - https://numpy.org/
* Matplotlib - https://matplotlib.org/
* Twython - https://twython.readthedocs.io/en/latest/

# To use
* You will need to have a Twitter developer account which will have the information needed for the _auth.py_ (listed in this repo as blank_auth.py)
* You will need to set cronjobs to run these scripts. To run out of the box, set *run_speed_test.py* to run every **5** minutes. Run the hourly *average_results.py* and daily stats *daily_stats.py* accordingly. Run the *graph_results.py* every **4** hours.

# Example CRON
*/5 * * * * /usr/bin/python3.5 /home/pi/speedcomplainer/v1/run_speed_test.py
1 */1 * * * /usr/bin/python3.5 /home/pi/speedcomplainer/v1/average_results.py
12 12 */1 * * /usr/bin/python3.5 /home/pi/speedcomplainer/v1/daily_stats.py
1 */4 * * * /usr/bin/python3.5 /home/pi/speedcomplainer/v1/graph_results.py
