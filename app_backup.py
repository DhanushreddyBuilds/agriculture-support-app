from flask import Flask, request, jsonify, session
from flask_cors import CORS
import mysql.connector
import hashlib

app = Flask(__name__)
app.secret_key = "agroai_super_secret_key"
CORS(app, supports_credentials=True)

# ---------------- DATABASE CONNECTION ----------------
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="agroai_db"
    )

# ---------------- SMART CROP KNOWLEDGE BASE ----------------
CROP_DATABASE = {
    "tomato": {
        "leaf disease": "🍅 Tomato Leaf Disease:\nCause: Fungal infections like Early & Late blight.\nSymptoms: Brown/black spots, yellowing, leaf fall.\nTreatment: Spray neem oil, Mancozeb, or Copper fungicide.",
        "pest": "🍅 Tomato Pests:\nCommon: Aphids, whiteflies.\nTreatment: Neem oil spray, sticky traps, proper field hygiene."
    },
    "rice": {
        "blast": "🌾 Rice Blast:\nCause: Fungus.\nTreatment: Use resistant varieties, spray Tricyclazole.",
        "pest": "🌾 Rice Pests:\nBrown planthopper, stem borer.\nTreatment: Neem oil or recommended insecticides."
    },
    "wheat": {
        "rust": "🌾 Wheat Rust:\nCause: Fungal disease.\nTreatment: Propiconazole spray, disease-resistant seeds."
    },
    "cotton": {
        "pest": "🌿 Cotton Pests:\nBollworm, whitefly.\nTreatment: Neem oil, pheromone traps, IPM methods."
    },
    "maize": {
        "leaf blight": "🌽 Maize Leaf Blight:\nCause: Fungus.\nTreatment: Mancozeb spray, crop rotation."
    },
    "potato": {
        "late blight": "🥔 Potato Late Blight:\nCause: Fungus.\nTreatment: Copper fungicide, avoid waterlogging."
    },
    "onion": {
        "purple blotch": "🧅 Onion Purple Blotch:\nTreatment: Mancozeb or Chlorothalonil spray."
    },
    "banana": {
        "sigatoka": "🍌 Banana Sigatoka:\nCause: Fungus.\nTreatment: Proper spacing, Carbendazim spray."
    },
    "sugarcane": {
        "red rot": "🍬 Sugarcane Red Rot:\nTreatment: Remove infected plants, use resistant varieties."
    },
    "groundnut": {
        "leaf spot": "🥜 Groundnut Leaf Spot:\nTreatment: Mancozeb spray every 10–15 days."
    }
}

GENERAL_FALLBACK = (
    "🌱 Please mention the crop name and symptoms clearly.\n"
    "Example:\n"
    "- Tomato leaf disease\n"
    "- Rice pest\n"
    "- Cotton fungus\n\n"
    "I support all major Indian crops."
)

GENERAL_DISEASE_TREATMENT = (
    "🦠 General Disease Care:\n"
    "- Remove infected leaves\n"
    "- Avoid over-watering\n"
    "- Ensure air circulation\n"
    "- Use neem oil spray\n"
    "- Apply suitable fungicide if needed"
)

# ---------------- CHAT BOT API ----------------
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "").lower()

    bot_reply = None
    found_crop = None
    found_issue = None

    for crop in CROP_DATABASE:
        if crop in user_message:
            found_crop = crop
            break

    if found_crop:
        for issue in CROP_DATABASE[found_crop]:
            if issue in user_message:
                found_issue = issue
                bot_reply = CROP_DATABASE[found_crop][issue]
                break

        if not bot_reply:
            bot_reply = (
                f"🌾 Crop detected: {found_crop.capitalize()}\n"
                f"Please specify the problem like:\n"
                f"- {found_crop} leaf disease\n"
                f"- {found_crop} pest\n"
                f"- {found_crop} fungus"
            )
    else:
        if "disease" in user_message or "fungus" in user_message:
            bot_reply = GENERAL_DISEASE_TREATMENT
        else:
            bot_reply = GENERAL_FALLBACK

    # Save chat into database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO chats (user_message, bot_reply) VALUES (%s, %s)",
        (user_message, bot_reply)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"reply": bot_reply})


# ---------------- ADMIN LOGIN ----------------
@app.route("/admin/login", methods=["POST"])
def admin_login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM admin_users WHERE username=%s AND password=%s",
        (username, hashed_password)
    )
    admin = cursor.fetchone()
    cursor.close()
    conn.close()

    if admin:
        session["admin"] = True
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})


# ---------------- SESSION CHECK ----------------
@app.route("/admin/check", methods=["GET"])
def admin_check():
    return jsonify({"logged": session.get("admin", False)})


# ---------------- ADMIN LOGOUT ----------------
@app.route("/admin/logout", methods=["POST"])
def admin_logout():
    session.clear()
    return jsonify({"success": True})


# ---------------- ADMIN CHAT DATA ----------------
@app.route("/admin/chats", methods=["GET"])
def get_chats():
    if not session.get("admin"):
        return jsonify({"error": "Unauthorized"}), 401

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM chats ORDER BY id DESC")
    chats = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(chats)


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)
