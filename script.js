// ---------------- INITIALIZATION (Animations & Particles) ----------------
window.onload = function () {
  createParticles();
  initTiltEffect();
};

function createParticles() {
  const container = document.getElementById("particles");
  if (!container) return;

  const particleCount = 20;

  for (let i = 0; i < particleCount; i++) {
    const p = document.createElement("div");
    p.className = "particle";
    // Random size
    const size = Math.random() * 10 + 5;
    p.style.width = `${size}px`;
    p.style.height = `${size}px`;

    // Random position
    p.style.left = `${Math.random() * 100}%`;
    p.style.top = `${Math.random() * 100}%`;

    // Random animation delay
    p.style.animationDelay = `-${Math.random() * 15}s`;
    p.style.opacity = Math.random() * 0.5 + 0.1;

    container.appendChild(p);
  }
}

function initTiltEffect() {
  const card = document.getElementById("input-card");
  if (!card) return;

  document.addEventListener("mousemove", (e) => {
    const x = (window.innerWidth / 2 - e.pageX) / 50; // rotation range
    const y = (window.innerHeight / 2 - e.pageY) / 50;

    card.style.transform = `rotateY(${x}deg) rotateX(${y}deg)`;
  });
}


// ---------------- VIEW HANDLING ----------------
function switchTab(tab) {
  const doctorView = document.getElementById("view-doctor");
  const advisorView = document.getElementById("view-advisor");
  const btnDoctor = document.getElementById("btn-doctor");
  const btnAdvisor = document.getElementById("btn-advisor");

  if (tab === "doctor") {
    doctorView.classList.remove("hidden");
    advisorView.classList.add("hidden");

    btnDoctor.classList.add("bg-green-700", "shadow-md");
    btnDoctor.classList.remove("text-green-100");

    btnAdvisor.classList.remove("bg-green-700", "shadow-md");
    btnAdvisor.classList.add("text-green-100");
  } else {
    doctorView.classList.add("hidden");
    advisorView.classList.remove("hidden");

    btnAdvisor.classList.add("bg-green-700", "shadow-md");
    btnAdvisor.classList.remove("text-green-100");

    btnDoctor.classList.remove("bg-green-700", "shadow-md");
    btnDoctor.classList.add("text-green-100");
  }
}

// ---------------- SPEECH RECOGNITION ----------------
function startVoice() {
  // If running inside Android WebView
  if (typeof Android !== "undefined" && Android.startVoiceInput) {
    Android.startVoiceInput();
    return;
  }

  // Else use browser speech recognition
  if (!('webkitSpeechRecognition' in window || 'SpeechRecognition' in window)) {
    alert("Speech recognition not supported in this browser.");
    return;
  }

  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  const recognition = new SpeechRecognition();
  recognition.lang = "en-IN";
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;

  const voiceBtn = document.getElementById("voiceBtn");
  if (voiceBtn) voiceBtn.classList.add("pulse-active");

  const input = document.getElementById("userInput");
  input.placeholder = "Listening...";

  recognition.start();

  recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    input.value = transcript;
    input.placeholder = "Describe your crop issue...";
    if (voiceBtn) voiceBtn.classList.remove("pulse-active");
    // Optional: Auto-send
    // sendMessage();
  };

  recognition.onerror = () => {
    input.placeholder = "Describe your crop issue...";
    if (voiceBtn) voiceBtn.classList.remove("pulse-active");
    alert("Voice recognition error or silence detected.");
  };

  recognition.onend = () => {
    input.placeholder = "Describe your crop issue...";
    if (voiceBtn) voiceBtn.classList.remove("pulse-active");
  };
}

// ---------------- CHATBOT LOGIC (Plant Doctor) ----------------
const chatBox = document.getElementById("chatBox");
// const typing = document.getElementById("typing"); // Removed static element
const input = document.getElementById("userInput");
const imageInput = document.getElementById("imageInput");
const imagePreview = document.getElementById("imagePreview");
const previewImg = document.getElementById("previewImg");

let typingIndicatorElement = null;

function showTyping() {
  if (typingIndicatorElement) return;

  typingIndicatorElement = document.createElement("div");
  typingIndicatorElement.className = "flex gap-4 max-w-5xl mx-auto animate-fade-in-up transition-all duration-300";
  typingIndicatorElement.innerHTML = `
    <div class="w-10 h-10 bg-green-600 rounded-full flex-shrink-0 flex items-center justify-center text-white font-bold shadow-md ring-2 ring-green-100">AI</div>
    <div class="glass-effect p-4 rounded-2xl rounded-tl-none border border-white/50 text-gray-500 shadow-sm flex items-center gap-2">
      <span class="w-2 h-2 bg-green-500 rounded-full animate-bounce"></span>
      <span class="w-2 h-2 bg-green-500 rounded-full animate-bounce" style="animation-delay: 0.15s"></span>
      <span class="w-2 h-2 bg-green-500 rounded-full animate-bounce" style="animation-delay: 0.3s"></span>
      <span class="text-xs font-medium ml-1">Thinking...</span>
    </div>
  `;
  chatBox.appendChild(typingIndicatorElement);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function hideTyping() {
  if (typingIndicatorElement) {
    typingIndicatorElement.remove();
    typingIndicatorElement = null;
  }
}

// Image Handling
if (imageInput) {
  imageInput.addEventListener("change", function () {
    const file = this.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function (e) {
        previewImg.src = e.target.result;
        imagePreview.classList.remove("hidden");
      }
      reader.readAsDataURL(file);
    }
  });
}

function clearImage() {
  imageInput.value = "";
  imagePreview.classList.add("hidden");
  previewImg.src = "";
}

function addMessage(text, sender, imageSrc = null) {
  const msgWrapper = document.createElement("div");
  msgWrapper.className = `flex gap-4 max-w-5xl mx-auto animate-bounce-in ${sender === "user" ? "justify-end" : ""}`;

  let contentHtml = "";
  if (imageSrc) {
    contentHtml += `<img src="${imageSrc}" class="max-w-xs rounded-lg mb-2 border-2 border-green-100 shadow-md transform hover:scale-105 transition-transform cursor-pointer">`;
  }

  const bubbleClass = sender === "bot"
    ? "glass-effect p-5 rounded-2xl rounded-tl-none border border-white/60 text-gray-800 shadow-md leading-relaxed hover:shadow-lg transition-shadow bg-gradient-to-br from-white/80 to-white/40"
    : "bg-gradient-to-br from-green-600 to-green-700 text-white p-4 rounded-2xl rounded-tr-none shadow-lg leading-relaxed transform hover:scale-[1.01] transition-transform";

  // Placeholder ID for typing effect
  const textId = `msg-${Date.now()}`;

  contentHtml += `<div class="${bubbleClass} relative"><span id="${textId}"></span></div>`;

  if (sender === "bot") {
    msgWrapper.innerHTML = `
        <div class="w-10 h-10 bg-green-600 rounded-full flex-shrink-0 flex items-center justify-center text-white font-bold shadow-lg ring-2 ring-green-100 transform hover:rotate-12 transition-transform">AI</div>
        <div class="flex-1 max-w-3xl">${contentHtml}</div>
      `;
  } else {
    msgWrapper.innerHTML = `
        <div class="flex flex-col items-end max-w-3xl">${contentHtml}</div>
        <div class="w-10 h-10 bg-gradient-to-tr from-blue-500 to-purple-500 rounded-full flex-shrink-0 flex items-center justify-center text-white font-bold text-xs shadow-lg ring-2 ring-blue-100">YOU</div>
      `;
  }

  chatBox.appendChild(msgWrapper);
  chatBox.scrollTop = chatBox.scrollHeight;

  // Render text
  if (sender === "user") {
    document.getElementById(textId).innerText = text;
  } else {
    // Basic formatting for bot (markdown-like)
    // We can enhance this later with a proper markdown parser if needed
    // For now, keep simple text injection but maybe process bolding
    const processedText = text.replace(/\*\*(.*?)\*\*/g, '<b>$1</b>').replace(/\n/g, '<br>');
    // typeWriterEffect(textId, text); // Use simple implementation for now, or processed
    // To support HTML in typeWriter, we need a complex parser. 
    // Let's stick to innerHTML injection for bolding support with a simple fade or just direct insert for now to be safe with HTML
    // Or use the typeWriter but plain text. 
    // Check if the user wants strictly animation. 
    // Let's use a smarter typeWriter that supports HTML tags? No, too complex for now.
    // Let's just set innerHTML directly for rich text support which looks better than raw typing for bold text.
    // If we want typing, we must use plain text or advanced lib.
    // Let's try the typing effect but stripped of HTML for animation, then replace with HTML?
    // No, let's just use typing effect for PLAIN text, and if it contains ** treat it special?
    // Actually, let's just *not* use typewriter if we want rich text (bolding).
    // The previous implementation used innerHTML += text.charAt(i), which is bad for HTML tags.
    // Let's use a simple "Stream" simulation:

    simulateTyping(textId, processedText);
  }
}

function simulateTyping(elementId, htmlContent) {
  const element = document.getElementById(elementId);
  // If content is long, just show it immediately to avoid annoyance
  // Or use a very fast interval
  // For "Doctor" checks, accurate rendering is more important.
  element.innerHTML = htmlContent;

  // Add a small bounce effect to the bubble itself?
  // The bubble already has animate-bounce-in.
}

// function typeWriterEffect(elementId, text) { ... } // Removed in favor of simulateTyping or direct render

async function sendMessage() {
  const message = input.value.trim();
  const file = imageInput.files[0];

  if (!message && !file) return;

  // Show user message immediately (with image if present)
  let userImageSrc = null;
  if (file) {
    userImageSrc = previewImg.src;
  }
  addMessage(message, "user", userImageSrc);

  // Clear inputs
  input.value = "";
  clearImage();
  showTyping(); // Use new function

  const sendBtn = document.getElementById("sendBtn");
  if (sendBtn) {
    sendBtn.disabled = true;
    sendBtn.innerHTML = "⏳";
  }

  try {
    const formData = new FormData();
    formData.append("message", message);
    if (file) {
      formData.append("image", file);
    }

    // Use relative path to work on any IP/host
    const API_BASE = "";

    const res = await fetch(`${API_BASE}/chat`, {
      method: "POST",
      body: formData
    });

    if (!res.ok) {
      throw new Error(`Server error: ${res.status}`);
    }

    const data = await res.json();
    hideTyping(); // Use new function
    addMessage(data.reply, "bot");

  } catch (error) {
    console.error("Chat Error:", error);
    hideTyping();
    addMessage("⚠️ Error connecting to AgroAI. Please check if the backend is running.", "bot");
  } finally {
    if (sendBtn) {
      sendBtn.disabled = false;
      sendBtn.innerHTML = "Send";
    }
  }
}

// ---------------- CROP RECOMMENDATION LOGIC ----------------
async function getRecommendation() {
  const soil = document.getElementById("soilInput").value;
  const season = document.querySelector('input[name="season"]:checked')?.value;
  const resultsDiv = document.getElementById("advisorResult");
  const container = document.getElementById("resultsContainer");

  if (!soil || !season) {
    alert("Please select both Soil Type and Season!");
    return;
  }

  // Show loading
  resultsDiv.classList.add("hidden");

  try {
    // Use relative path to work on any IP/host
    const API_BASE = "";

    const res = await fetch(`${API_BASE}/recommend`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ soil, season })
    });

    const data = await res.json();
    container.innerHTML = "";

    if (data.error) {
      container.innerHTML = `<div class="col-span-2 text-red-500 bg-red-50 p-4 rounded-lg">${data.error}</div>`;
    } else {
      data.recommendations.forEach((rec, index) => {
        const delay = index * 100;
        const card = document.createElement("div");
        // Premium card styling: clearer background, stronger shadow on hover, decorative overflow
        card.className = "bg-white p-6 rounded-2xl shadow-lg border border-gray-100 hover:shadow-2xl hover:-translate-y-1 transition-all duration-300 animate-fade-in-up flex flex-col gap-4 relative overflow-hidden group";
        card.style.animationDelay = `${delay}ms`;

        // Decorative background shape
        const bgDecoration = `<div class="absolute -right-8 -top-8 w-32 h-32 bg-green-50 rounded-full opacity-50 group-hover:scale-125 transition-transform duration-700 pointer-events-none"></div>`;

        card.innerHTML = `
            ${bgDecoration}
            
            <div class="relative z-10">
                <!-- Header -->
                <div class="flex items-start justify-between mb-4">
                    <div>
                        <span class="text-[10px] font-bold tracking-wider text-green-600 uppercase bg-green-50 px-2 py-1 rounded-md mb-2 inline-block border border-green-100">Recommended Crop</span>
                        <h4 class="font-bold text-gray-800 text-xl leading-tight group-hover:text-green-700 transition-colors">${rec.name}</h4>
                    </div>
                </div>
                
                <div class="space-y-4">
                    <!-- Variety Section -->
                    <div class="flex items-start gap-3 p-3 rounded-lg hover:bg-slate-50 transition-colors border border-transparent hover:border-slate-100">
                        <div class="w-8 h-8 rounded-full bg-blue-50 flex items-center justify-center flex-shrink-0 text-blue-500 border border-blue-100">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" />
                            </svg>
                        </div>
                        <div>
                            <p class="text-[10px] text-gray-400 font-bold uppercase tracking-wider">Best Variety</p>
                            <p class="text-sm font-semibold text-gray-700">${rec.variety}</p>
                        </div>
                    </div>

                    <!-- Tips Section (Enhanced Bulb) -->
                    <div class="flex items-start gap-3 p-3 bg-yellow-50/50 rounded-lg border border-yellow-100/50">
                        <div class="w-8 h-8 rounded-full bg-yellow-100 flex items-center justify-center flex-shrink-0 text-yellow-600 shadow-sm">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                            </svg>
                        </div>
                        <div>
                            <p class="text-[10px] text-yellow-600 font-bold uppercase tracking-wider mb-0.5">Expert Insight</p>
                            <p class="text-sm text-gray-600 leading-relaxed font-medium">${rec.tips}</p>
                        </div>
                    </div>
                </div>
            </div>
        `;
        container.appendChild(card);
      });
    }

    resultsDiv.classList.remove("hidden");
    resultsDiv.scrollIntoView({ behavior: 'smooth' });

  } catch (error) {
    console.error(error);
    alert("Error fetching data.");
  }
}
