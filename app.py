from flask import Flask, request, jsonify, send_from_directory, render_template, redirect, url_for, session, flash
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import mysql.connector
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
import io
import warnings
import random

# Suppress the specific FutureWarning from google.generativeai
warnings.filterwarnings("ignore", category=FutureWarning, module="google.generativeai")

# Import static data and helpers
import data

# Load environment variables
load_dotenv()

# Set template_folder to the same as static_folder for simplicity since HTMLs are there
app = Flask(__name__, static_folder="../frontend", static_url_path="", template_folder="../frontend")
app.secret_key = os.getenv("SECRET_KEY", "agroai_secret_key_secure_session")
CORS(app)

# ---------------- CONFIGURATION ----------------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# ---------------- DATABASE CONFIG ----------------
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "agroai_db")
    )

# ---------------- LOG HELPERS ----------------
def log_chat(user_id, user_message, bot_reply):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Ensure table exists (optional double-check)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chats (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                user_message TEXT,
                bot_reply TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        cursor.execute("INSERT INTO chats (user_id, user_message, bot_reply) VALUES (%s, %s, %s)", 
                       (user_id, user_message, bot_reply))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"DB Log Error: {e}")

# ---------------- LANGUAGE & ISSUE DETECTION ----------------
def is_kannada(text):
    if not text: return False
    for ch in text:
        if '\u0C80' <= ch <= '\u0CFF':
            return True
    return False

def detect_issue(text):
    text = text.lower()
    for w in data.YIELD_WORDS:
        if w in text: return "yield"
    for w in data.SOIL_WORDS:
        if w in text: return "soil"
    for w in data.WATER_WORDS:
        if w in text: return "water"
    for w in data.PEST_WORDS:
        if w in text: return "pest"
    for w in data.FUNGUS_WORDS:
        if w in text: return "fungus"
    for w in data.LEAF_WORDS:
        if w in text: return "leaf"
    return "general"

def extract_crop(text):
    text_lower = text.lower()
    for crop in data.KNOWN_CROPS:
        if crop in text_lower:
            return crop.capitalize()
    return "Crop"

# ---------------- AI RESPONSE ENGINE ----------------
def generate_response(crop, issue, kannada, user_message="", image_file=None):
    # List of models to try in order of preference
    # 2.0 Flash/Lite are fast but might be rate-limited. Pro is a good fallback.
    models_to_try = [
        'gemini-1.5-flash-8b', # Often has better availability
        'models/gemini-2.0-flash-lite-001',
        'gemini-2.0-flash',
        'gemini-pro',
        'gemini-1.5-pro-latest'
    ]

    # Prepare inputs
    lang_instruction = "Respond in English."
    if kannada:
        lang_instruction = "Respond in Kannada language only."
        
    system_instruction = f"""
    You are 'AgroAI', a friendly and empathetic agricultural expert (Plant Doctor). 
    Your goal is to help farmers like a personal doctor.
    
    Detected Crop: {crop}
    Detected Issue Category: {issue}
    {lang_instruction}
    
    **Guidelines:**
    1. **Be Conversational:** Don't just list facts. Talk to the user. Say things like "I see your tomato plant is struggling..." or "Don't worry, we can fix this."
    2. **Ask Clarifying Questions:** If the user's details are vague (e.g., just "my plant died"), ask 1-2 relevant questions to diagnose better (e.g., "Did you notice any spots on the leaves?" or "How often do you water?").
    3. **Structure Your Advice:**
       - **Analysis:** Briefly explain what you see/think is wrong.
       - **Remedy:** Give organic first, then chemical options.
       - **Pro Tip:** rigorous advice for future prevention.
    4. **Tone:** Warm, professional, encouraging. Use emojis to make it friendly. 🌾🚜
    
    Output format: purely natural language, but well-structured with paragraphs and bullet points where needed.
    """
    
    inputs = [system_instruction, user_message]
    if image_file:
        try:
            image_file.seek(0) # Reset pointer
            img = Image.open(image_file)
            inputs.append(img)
            inputs[0] += "\n\n[IMAGE ANALYSIS REQUEST]: The user has uploaded an image. Analyze the visual symptoms carefully (discoloration, pests, spots, wilting) and incorporate these findings into your diagnosis."
        except Exception as img_err:
            print(f"Image Error: {img_err}")


    # Try Models Logic
    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(inputs)
            
            if response and response.text:
                return response.text
                
        except Exception as e:
            print(f"Gemini API Error ({model_name}): {e}")
            # Continue to next model
            continue
            
    # If all models fail, fall through to rule-based
    print("All Gemini models failed. Switching to Rule-Based.")
    with open("api_error.log", "a") as f:
        f.write("All models failed. Fallback triggered.\n")
        
    # 2. Fallback: Rule-Based Logic
    return generate_rule_based_response(crop, issue, kannada)


def generate_rule_based_response(crop, issue, kannada):
    # --- KANNADA RESPONSES (Simplistic for now) ---
    if kannada:
        if issue == "yield":
            return f"""ನಮಸ್ಕಾರ! ನಿಮ್ಮ **{crop}** ಇಳುವರಿ ಕಡಿಮೆ ಇರುವ ಹಾಗಿದೆ.\n\n🌾 **ಕಾರಣಗಳು:** ಪೋಷಕಾಂಶಗಳ ಕೊರತೆ.\n✅ **ಪರಿಹಾರಗಳು:**\n1. **ಗೊಬ್ಬರ:** ಪೊಟ್ಯಾಶ್ ಮತ್ತು ಜಿಂಕ್ ಸಲ್ಫೇಟ್ ಕೊಡಿ.\n2. **ಟಾನಿಕ್:** "ಪಾಂಚಜನ್ಯ" ಸಿಂಪಡಿಸಿ."""
        elif issue == "leaf":
            return f"""ನಮಸ್ಕಾರ! ನಿಮ್ಮ {crop} ಎಲೆಗಳ ಸಮಸ್ಯೆ ಕಂಡುಬರುತ್ತಿದೆ.\n\n🌿 **ಪರಿಹಾರಗಳು:**\n1. **ಜೈವಿಕ:** ನೀಮ್ ಎಣ್ಣೆಯನ್ನು ಸಿಂಪಡಿಸಿ.\n2. **ಗೊಬ್ಬರ:** ವರ್ಮಿಕಂಪೋಸ್ಟ್ ಬಳಸಿ.\n💊 **ರಾಸಾಯನಿಕ:** ಮ್ಯಾಂಕೋಜೆಬ್ ಬಳಸಿ."""
        elif issue == "pest":
            return f"""ನಿಮ್ಮ {crop} ಬೆಳೆಗೆ ಕೀಟಗಳ ಬಾಧೆ ಇದೆ.\n\n🌿 **ಜೈವಿಕ:** ನೀಮ್ ಎಣ್ಣೆ ಸಿಂಪಡಿಸಿ.\n💊 **ರಾಸಾಯನಿಕ:** ಇಮಿಡಾಕ್ಲೋಪ್ರಿಡ್ ಸಿಂಪಡಿಸಿ."""
        elif issue == "fungus":
             return f"""ಗಮನಿಸಿ, ನಿಮ್ಮ {crop} ಬೆಳೆಗೆ ಶಿಲೀಂಧ್ರ ಸೋಂಕು ತಗುಲಿದೆ.\n\n🌿 **ಪರಿಹಾರ:** ಟ್ರೈಕೊಡರ್ಮಾ ಬಳಸಿ.\n💊 **ಔಷಧ:** ಮ್ಯಾಂಕೋಜೆಬ್ ಸಿಂಪಡಿಸಿ."""
        else:
            return f"""ಕ್ಷಮಿಸಿ, ನಿಮ್ಮ {crop} ಬೆಳೆಯ ಸಮಸ್ಯೆಯನ್ನು ವಿವರಿಸಿ. ಉದಾಹರಣೆಗೆ: "{crop} ಎಲೆಗಳು ಹಳದಿ"."""
            
    # --- ENGLISH "DOCTOR" PERSONA RESPONSES ---
    
    expert_tip = data.CROP_SPECIFIC_TIPS.get(crop.capitalize(), "Ensure proper drainage and rotation.")
    
    # Templates for conversational variety
    intros = [
        f"I see you're worried about your **{crop}**.",
        f"Hello! Let's look at your **{crop}** together.",
        f"Don't worry, I can help your **{crop}** recover.",
        f"It sounds like your **{crop}** is having a tough time."
    ]
    
    intro = random.choice(intros)
    
    if issue == "leaf":
        return f"""{intro} 🍃\n\n**Observation:** The leaves seem to be affected (yellowing/spots).\n**Diagnosis:** This is often due to **Nitrogen deficiency** or early **Fungal Blight**.\n\n**Doctor's Prescription:**\n1. 🌿 **Organic:** Spray **Neem Oil** (5ml/liter) immediately.\n2. 💊 **Chemical:** If spreading, use **Mancozeb** (2g/liter).\n\n💡 **Pro Tip:** {expert_tip}"""
        
    elif issue == "pest":
        return f"""{intro} 🐛\n\n**Observation:** It definitely looks like a **Pest Attack**.\n**Diagnosis:** Likely Aphids, Thrips, or Borers.\n\n**Doctor's Prescription:**\n1. 🌿 **First Step:** Install **Yellow Sticky Traps** in the field.\n2. 💊 **Treatment:** Spray **Imidacloprid** (0.5ml/liter) for quick control.\n\n💡 **Pro Tip:** {expert_tip}"""

    elif issue == "fungus":
        return f"""{intro} 🍄\n\n**Observation:** Fungal infections can spread fast!\n**Diagnosis:** Likely **Blight** or **Rot** caused by humidity.\n\n**Doctor's Prescription:**\n1. 🛑 **Immediate Action:** Stop watering for 2 days.\n2. 🌿 **Bio-Cure:** Apply **Trichoderma** to the soil.\n3. 💊 **Stronger Fix:** Spray **Copper Oxychloride**.\n\n💡 **Pro Tip:** {expert_tip}"""

    elif issue == "yield":
        return f"""{intro} 📉\n\n**Observation:** You want better growth and yield.\n**Diagnosis:** Usually caused by **Micro-nutrient deficiency** during flowering.\n\n**Doctor's Prescription:**\n1. 🌿 **Boost:** Apply **Vermicompost** at the roots.\n2. 💊 **Spray:** Use **NPK 19:19:19** (water soluble) for instant energy.\n\n💡 **Pro Tip:** {expert_tip}"""
        
    elif issue == "soil":
        return f"""{intro} 🟤\n\n**Observation:** Soil health is the foundation.\n**Diagnosis:** The roots might be weak or nutrient-deprived.\n\n**Doctor's Prescription:**\n1. 🌿 **Mix:** Add **Humic Acid** granules to the soil.\n2. 🦠 **Bio:** Use **Mycorrhiza** to expand the root system.\n\n💡 **Pro Tip:** {expert_tip}"""

    elif issue == "water":
         return f"""{intro} 💧\n\n**Observation:** Water management is tricky!\n**Diagnosis:** Over-watering or irregular watering causes stress.\n\n**Doctor's Prescription:**\n1. 📏 **Rule:** Only irrigate when the top 2 inches of soil are dry.\n2. 🚿 **Method:** Drip irrigation is best for {crop}.\n\n💡 **Pro Tip:** {expert_tip}"""

    else:
        # General/Unknown Fallback - Asking questions
        return f"""Hello! I am your Plant Doctor. 🩺\n\nI noticed you mentioned **{crop}**, but I need a few more details to diagnose correctly.\n\n**Could you tell me:**\n1. Are the leaves turning yellow or drying?\n2. Do you see any insects?\n3. Is the growth stunted?\n\n*Reply with details like "yellow leaves" or "white bugs" so I can help!*"""


# ---------------- API ROUTES ----------------

@app.route("/chat", methods=["POST"])
def chat():
    # Handle optional image upload
    image_file = None
    user_message = ""
    
    # check if the post request has the file part or is just json
    if request.content_type and 'multipart/form-data' in request.content_type:
        user_message = request.form.get("message", "").lower()
        if 'image' in request.files:
            file = request.files['image']
            if file and file.filename != '':
                image_file = file
    else:
        data = request.json
        if data:
            user_message = data.get("message", "").lower()

    if not user_message and not image_file:
         return jsonify({"reply": "Please send a message or image."}), 400
         
    kannada = is_kannada(user_message)
    crop = extract_crop(user_message)
    issue = detect_issue(user_message)

    reply = generate_response(crop, issue, kannada, user_message, image_file)
    
    # Log to DB if user is logged in (or just log everything with null user_id)
    user_id = session.get("user_id") # Can be None
    log_chat(user_id, user_message, reply)
    
    return jsonify({"reply": reply})


@app.route("/recommend", methods=["POST"])
def recommend():
    req_data = request.json
    soil = req_data.get("soil", "").lower()
    season = req_data.get("season", "").lower()

    # Normalize inputs
    if "red" in soil: soil = "red"
    elif "black" in soil: soil = "black"
    elif "clay" in soil: soil = "clay"
    elif "sandy" in soil: soil = "sandy"
    
    if "kharif" in season or "monsoon" in season: season = "kharif"
    elif "rabi" in season or "winter" in season: season = "rabi"
    elif "summer" in season: season = "summer"

    if soil in data.CROP_DATA and season in data.CROP_DATA[soil]:
        recommendations = data.CROP_DATA[soil][season]
        return jsonify({"recommendations": recommendations})
    else:
        return jsonify({"recommendations": [], "error": "No specific data for this combination. Please try standard soil types (Red, Black, Clay, Sandy) and seasons."})


# ---------------- AUTHENTICATION ROUTES ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirm = request.form["confirm_password"]

        if password != confirm:
            flash("Passwords do not match!", "error")
            return redirect(url_for("register"))

        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM admin_users WHERE username = %s", (username,))
            if cursor.fetchone():
                flash("Username already exists!", "error")
                return redirect(url_for("register"))

            hashed_pw = generate_password_hash(password)
            cursor.execute("INSERT INTO admin_users (username, password) VALUES (%s, %s)", (username, hashed_pw))
            conn.commit()
            flash("Registration successful! Please login.", "success")
            return redirect(url_for("login"))
        except Exception as e:
            flash(f"Database Error: {str(e)}", "error")
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM admin_users WHERE username = %s", (username,))
            user = cursor.fetchone()

            if user and check_password_hash(user["password"], password):
                session["user_id"] = user["id"]
                session["username"] = user["username"]
                return redirect(url_for("home"))
            else:
                flash("Invalid username or password", "error")
        except Exception as e:
            flash(f"Connection Error: {str(e)}", "error")
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# ---------------- ROOT UI (Protected) ----------------
@app.route("/")
def home():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("index.html", username=session.get("username"))


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
