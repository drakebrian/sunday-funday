from yahoofantasy import Context, League
from flask import Flask, redirect, render_template, request, url_for
import yahoofantasy.util.persistence as persistence
# from yahoofantasy.api.games import get_game_id, _find_game_id

app = Flask(__name__, static_url_path='', static_folder='static')

YEAR = 2023
SPORT = 'nfl'
RETAINED_KEYS = ["auth"]
ctx = Context()

@app.route('/setup')
def league_select():
    # ctx = Context()
    leagues = ctx.get_leagues(SPORT, YEAR)

    return render_template('setup.html', leagues=leagues)

@app.route('/scoreboard')
def scoreboard():
    # ctx = Context()
    league_id = request.args.get('league', None)
    
    if not league_id:
        return redirect(url_for('league_select'))

    # persistence.clear(RETAINED_KEYS, ctx._persist_key)

    leagues = ctx.get_leagues(SPORT, YEAR)
    league = next(l for l in leagues if l.id == league_id)

    standings = {}

    for team in league.standings():
        team_standings = team.team_standings.outcome_totals
        standings[team.team_id] = team_standings

        # print(team.team_standings)
        # print(vars(team))

    get_week = int(request.args.get('week', 1)) - 1
    week = league.weeks()[get_week]

    # for matchup in week.matchups:
    #     print(vars(matchup))


    return render_template('scoreboard.html', week=get_week + 1, matchups=week.matchups, standings=standings, enumerate=enumerate)


@app.route("/setup/<sport>/")
def league_setup(sport):
    leagues = ctx.get_leagues(sport, YEAR)

    return f"<p>Hello, {sport}! Hhah {leagues}</p>"



# for league in leagues:
#     print(league.name + " -- " + league.league_type)
#     print(vars(league))

    # league = League(ctx, '388.l.25000')  # Use a manual league ID or get it from league.id above
    # for team in league.teams():
    #     print(f"Team Name: {team.name}\tManager: {team.manager.nickname}")