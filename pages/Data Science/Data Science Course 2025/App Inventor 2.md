<title>App Inventor 2 (AI2)</title>

# Overview

MIT App Inventor 2 (AI2) is a free, cloud-based visual programming platform created by MIT that lets anyone — especially beginners, students, and non-programmers — build fully functional Android (and iOS) mobile apps using only drag-and-drop puzzle blocks instead of writing code. Running entirely in a web browser, it features a live companion app or emulator so you can test your app instantly on your phone as you build it, and it supports powerful features like camera, sensors, GPS, Bluetooth, Firebase databases, text-to-speech, AI extensions, and even augmented reality, and IoT device control — all without ever typing a line of traditional code. First launched in 2010 by Google and now maintained by MIT, App Inventor 2 is used by millions of people worldwide (from middle-school classrooms to startups in developing countries) to create everything from simple games and quizzes to sophisticated business, health, and artificial-intelligence apps that are published directly to Google Play and the Apple App Store.

# Getting Started

Here’s the **fastest, zero-stress way for a total beginner to go from nothing to a working app on your phone in under 30 minutes** (updated for 2025):

### Step-by-Step (Takes ~20–30 minutes)

1. **Go to the official site**  
   Open your browser and go to: https://appinventor.mit.edu  
   Click the big orange button **“Create Apps!”**

2. **Sign in with Google**  
   Use any Gmail or Google account (school accounts work too). No extra signup needed.

3. **Start a new project**  
   Click **“Start new project”** → give it any name (e.g., “MyFirstApp”)

4. **You now see two windows**
   - Left = Designer (drag buttons, labels, images here)
   - Right = Blocks (drag puzzle pieces here later)

5. **Instantly test on your phone (the magic part)**
   - Android phone:  
     On your phone, go to Google Play and install **“MIT AI2 Companion** (free)  
     In the App Inventor website, click **Connect → AI Companion**  
     A QR code or 6-digit code appears → scan/type it in the Companion app  
     → Whatever you design now appears LIVE on your phone as you build!

   - iPhone/iPad:  
     Same thing, but download **“MIT AI2 Companion”** from the Apple App Store.

   - No phone? Click **Connect → Emulator** and a virtual Android phone appears in your browser.

6. **Make your first tiny app (Hello World)**
   - In Designer:  
     Drag a **Button** and change its Text to “Touch Me”  
     Drag a **Label** below it and change its Text to blank
   - Switch to Blocks (top right button)
   - Drag the yellow “when Button1.Click” block
   - Drag the green “set Label1.Text to” block and snap it inside
   - Click the blue “text” block → type “Hello! I made an app!”
   - Go back to your phone → tap the button → it says “Hello! I made an app!”

7. **Save & download your app**
   - Projects → Export .aia (backup (so you never lose it)
   - Build → App (provide QR code for .apk) → scan with phone to install permanently  
     or → App bundle (.aab) to publish on Google Play later

### Best Free Beginner Resources (2025)
- Official tutorials (built-in): Click [**Learning → Tutorials**](http://appinventor.mit.edu/explore/ai2/tutorials) inside App Inventor
- YouTube: Search “[App Inventor 2025 beginner tutorial](https://www.youtube.com/results?search_query=App+Inventor+2025+beginner+tutorial)”
- MIT’s free book: http://appinventor.mit.edu/explore/ai2/beginner-tutorials
- [Amazon Books](https://www.amazon.com/s?k=app+inventor+2&crid=185TNNIVQLKPH&sprefix=app+inventor%2Caps%2C174&ref=nb_sb_ss_p13n-expert-pd-ops-ranker_2_12
- [Recommended Books](https://appinventor.mit.edu/explore/books)
- [PDF Tutorial](https://appinventor.mit.edu/explore/sites/all/files/hourofcode/AppInventorTutorials.pdf)

# Some things you can do with AI2

Here’s a curated list of **truly amazing (and real)** things people have built with **MIT App Inventor 2** in 2024–2025 — many of them look like they came from professional studios, but they’re 100% made with the drag-and-drop blocks (or blocks + a few extensions).

| Category                        | Amazing Example Project (with proof/link if public)                                                                 | What makes it “wow”                                                                 |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Games                           | Flappy Bird clones with online leaderboards, 3D-like racing games, full Pokémon-style RPGs                           | Realtime multiplayer via Firebase, physics engines, animated sprites                |
| IoT / Hardware                  | Control real robots, drones (DJI Tello), Arduino, ESP32, Raspberry Pi over Bluetooth/Wi-Fi                           | Students flying drones or moving robot arms just with an app they built in class    |
| AI & Machine Learning           | Image recognition (Teachable Machine + custom model), live speech-to-text translation, ChatGPT inside the app       | Talk to your app and it answers using GPT-4o, or detects objects with the camera    |
| Augmented Reality (AR)          | Pokémon GO-style games, AR business cards, virtual try-on for glasses/clothes                                       | Uses phone camera + AR extensions (ARCore via extension)                             |
| Wearables                       | Full smartwatch apps for Android Wear / Galaxy Watch (using the Wear OS companion)                                 | Control phone or show notifications directly on the watch — built in App Inventor 2       |
| Professional Business Apps      | Delivery apps (like Uber), restaurant ordering systems, field service apps with maps + signature + PDF generation   | Used by real companies in India, Africa, Latin America because it’s free & fast      |
| Medical & Health                | Glucose monitors for diabetes, ECG viewers, mental-health mood trackers with graphs                                 | Used in hospitals in Brazil and India                                               |
| Education & Science             | Interactive physics simulations, virtual labs, star/planet identifiers using phone sensors                          | MIT itself uses App Inventor in university courses                                  |
| Music & Creativity              | Full synthesizer apps, beat makers, guitar tuner with pitch detector, draw-and-play music apps                      | Some of these are on Google Play with 100k+ downloads                                |
| Social & Chat                   | WhatsApp-style chat apps with voice messages, group chat, end-to-end encryption (using extensions)                  | Realtime Firebase + encryption extensions                                            |
| Blockchain / Crypto             | Simple crypto wallets, NFT viewers, send/receive testnet coins                                                      | Yes — people really did this with App Inventor!                                     |
| Accessibility                   | Apps for blind users (text-to-speech + object detection), sign-language translators                                | Winner projects at Google Science Fair and Technovation Girls                        |

### My personal top 5 “mind-blowing” ones (all 100% App Inventor 2)
1. **Drone Controller** – Fly a real DJI Tello drone using only your phone and an App Inventor app.
2. **Live Sign-Language Translator** – Point camera at hands → translates to text/speech in real time.
3. **Multiplayer Online Battle Arena Game** – 2–8 players in same room or over internet (like a mini Fortnite).
4. **Home Automation Dashboard** – Control lights, AC, doors in entire house with custom UI.
5. **AI Doctor Symptom Checker** – You describe symptoms by voice → app uses GPT + medical database to suggest possible issues (used in rural clinics).

### Bonus: Things you can add with free extensions (still drag-and-drop!)
- OneSignal push notifications (millions of users)
- In-app purchases & Google Play billing
- Google Maps with custom markers and routes
- Fingerprint / Face ID login
- Turn your app into a web app (Progressive Web App)

**Bottom line:**  
App Inventor 2 is no longer “just for beginners” or “only simple apps”.  
In 2025, teenagers and even startups are shipping real, monetized, beautiful apps entirely with App Inventor — and many of them earn money on Google Play.
