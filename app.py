from flask import Flask, request, jsonify, render_template
from recommender import get_recommendations, df_data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/genre")
def genre():
    return render_template("genre.html")

@app.route("/dramas")
def dramas():
    return render_template("dramas.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/get_all_dramas")
def get_all_dramas():
    dramas = df_data['Title'].tolist()
    return jsonify({"dramas": dramas})

@app.route("/recommend", methods=["POST"])
def recommend_endpoint():
    data = request.json
    user_input = data.get("query", "").strip()
    if not user_input:
        return jsonify({"input": "", "recommendations": []})

    recs = get_recommendations(user_input)
    return jsonify({"input": user_input, "recommendations": recs})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    # host="0.0.0.0" so external network can reach it on Render
    app.run(debug=True, host="0.0.0.0", port=port)
