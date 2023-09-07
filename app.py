from yahoofantasy import Context, League
from flask import Flask, redirect, render_template, request, url_for
# from yahoofantasy.api.games import get_game_id, _find_game_id

app = Flask(__name__)
ctx = Context()

YEAR = 2023
SPORT = 'nfl'

@app.route('/setup')
def league_select():
    leagues = ctx.get_leagues(SPORT, YEAR)

    return render_template('setup.html', leagues=leagues)

@app.route('/scoreboard')
def scoreboard():
    league_id = request.args.get('league', None)
    
    if not league_id:
        return redirect(url_for('league_select'))

    leagues = ctx.get_leagues(SPORT, YEAR)
    league = next(l for l in leagues if l.id == league_id)

    get_week = int(request.args.get('week', 0))
    week = league.weeks()[get_week]

    # for matchup in week.matchups:
    #     print(vars(matchup))


    return render_template('scoreboard.html', league=league, week=get_week + 1, matchups=week.matchups)


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