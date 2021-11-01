from flask import Flask, render_template, request, redirect
import sqlite3 as sql
import requests

app = Flask(__name__)

USER_ID = "1"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/addresses", methods=["GET"])
def addresses():

    with sql.connect("database.db") as con:
        db = con.cursor()
        db.execute(
            "SELECT addr, balance, balance_usd FROM addresses WHERE userId=?",
            USER_ID,
        )
        result = db.fetchall()
        data = []
        total_btc = 0
        total_usd = 0
        for i in result:
            data.append(
                {
                    "addr": i[0],
                    "balance": i[1] / 10 ** 8,
                    "balance_usd": "${:,.2f}".format(i[2]),
                }
            )
            total_btc += i[1]
            total_usd += i[2]

        total_btc = "{:,.8f}".format(total_btc / 10 ** 8)
        total_usd = "${:,.2f}".format(total_usd)
    return render_template(
        "addresses.html", data=data, total_btc=total_btc, total_usd=total_usd
    )


@app.route("/post_address", methods=["POST"])
def post_address():
    addr = request.form.get("addr")
    # addr = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
    # addr = "3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5"
    # addr = "76a91477bff20c60e522dfaa3350c39b030a5d004e839a88ac"
    # addr = "17FDQ8eoRfWFRJJdZwTF3KmKDRYPxYxApM"

    # Check input is not empty
    if not addr:
        error_msg = "Please enter a bitcoin address"
        return render_template("addresses.html", error_msg=error_msg)

    # TODO: Check if address is valid

    # Call Blockchair API
    url = f"https://api.blockchair.com/bitcoin/dashboards/address/{addr}?limit=2&transaction_details=true"

    r = requests.get(url)
    addr_data = r.json()["data"][addr]["address"]
    balance = addr_data["balance"]
    balance_usd = addr_data["balance_usd"]

    # data = []
    # total_btc = 0
    # total_usd = 0
    with sql.connect("database.db") as con:
        try:
            db = con.cursor()
            db.execute(
                "INSERT INTO addresses (userId, addr, balance, balance_usd) VALUES(?, ?, ?, ?)",
                (USER_ID, addr, balance, balance_usd),
            )
            con.commit()
        except:
            con.rollback()
    return redirect("/addresses")
