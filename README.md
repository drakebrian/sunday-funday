# sunday-funday
Yahoo Fantasy Football Scoreboard for Sunday Fundays

### Prerequisites
* [Yahoo Developer](https://developer.yahoo.com/) account

### Setup
1. [Create an app](https://developer.yahoo.com/apps/create/) with the following settings:
    * Redirect URI: https://localhost:8000
    * API Permissions: Fantasy Sports, read only
2. Copy Client ID and Secret for setup
3. Create virtual environment, activate and install requirements.txt
4. Run `yahoofantasy login`
5. Enter Client ID and Secret from your app
6. Login to Yahoo Fantasy at the prompt
7. Start Flask app with `flask --app app run` with optional `--debug` flag
