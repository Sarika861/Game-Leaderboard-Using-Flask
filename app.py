from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Store players and scores
players = {}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        score = int(request.form["score"])

        players[name] = score
        return redirect("/")

    # Sort leaderboard
    leaderboard = sorted(players.items(), key=lambda x: x[1], reverse=True)
    return render_template("index.html", players=players, leaderboard=leaderboard)


if __name__ == "__main__":
    app.run(debug=True)
