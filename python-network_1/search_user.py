from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route("/search_user", methods=["POST"])
def search():
    q = request.form.get('q', "")
    if q == "":
        return jsonify({})
    elif q in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        return jsonify({
            "id": random.randint(1, 9999),
            "name": f"User_{q}"
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
