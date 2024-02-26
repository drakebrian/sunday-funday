# sunday-funday
Yahoo Fantasy Football Scoreboard for Sunday Fundays


### Prerequisites
* [Yahoo Developer](https://developer.yahoo.com/) account
* [Create an app](https://developer.yahoo.com/apps/create/) with the following settings:
    * Redirect URI: https://localhost:8000
    * API Permissions: Fantasy Sports, read only
* Copy Client ID and Secret for setup

### Setup
1. Create virtual environment, activate and install requirements.txt
2. Run `yahoofantasy login`
3. Enter Client ID and Secret from your app
4. Login to Yahoo Fantasy at the prompt
5. Start Flask app with `flask --app app run` with optional `--debug` flag
