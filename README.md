# NewMyMatcha 🎬💖  

**Live Demo:** [https://newmymatcha.onrender.com/](https://newmymatcha.onrender.com/)  

> “A BL drama recommendation platform built with love, dedication, and a mission to celebrate **every story that deserves to be seen**.”  

---

## Table of Contents 📑  

1. [The Story Behind NewMyMatcha](#the-story-behind-newmymatcha)  
2. [Features](#features)  
3. [Dataset & Representation](#dataset--representation)  
4. [How the Recommendation Works](#how-the-recommendation-works)  
5. [Tech Stack](#tech-stack)  
6. [Installation & Setup](#installation--setup)  
7. [File Structure](#file-structure)  
8. [Usage](#usage)  
9. [Contribution](#contribution)  
10. [License & Contact](#license--contact)  

---

## The Story Behind NewMyMatcha ✨  

This project started as an idea in **the midst of a busy semester**. I remember losing **Engineers’ Day** to work on it, juggling lectures, assignments, and a microprocessor lab. My **Civils professor Dr. Karanjeet Kaur**, who usually doesn’t deal with coding, noticed my effort and called it a “gem” — and that motivated me to push harder.  

My goal was simple but important: **to create a platform that represents underrepresented communities in BL dramas**. Many dramas either ignore minority stories or fail to make them discoverable. I wanted **NewMyMatcha** to shine a light on these gems, giving visibility to **LGBTQIA+ characters, POC, and minority themes** while maintaining a robust, technical recommendation system.  

---

## Features ✨  

- Personalized **BL drama recommendations** based on user input.  
- **Genre-based browsing** to explore dramas easily.  
- Focus on **diverse representation** for underrepresented stories.  
- Live updates from a **Google Sheets dataset**.  
- Hosted online with **zero setup required**, thanks to Render.  

---

## Dataset & Representation 🌈  

- **Source**: Google Sheets CSV export with columns like `Title`, `Summary`, `Genres`, and `Themes`.  
- **Representation Focus**:  
  - Each drama tagged with its themes, including LGBTQIA+, POC, and minority narratives.  
  - The system ensures **recommendations don’t erase or overshadow underrepresented content**.  
  - New dramas can be added to the sheet, and they automatically enter the recommendation engine.  

**Sample dataset structure**:

| Title             | Summary                 | Genres        | Themes               |
|------------------|------------------------|--------------|--------------------|
| Shine             | College romance story   | Romance, BL  | LGBTQIA+, Campus   |
| Hermoso           | Young love and struggles| Drama, BL    | Minority, Identity |

---

## How the Recommendation Works 🤖  

1. **Input Processing**: The user enters a drama title.  
2. **Preprocessing**:  
   - Combine summary, genres, and themes into one text field.  
   - Convert to lowercase and stem using **PorterStemmer**.  
3. **Vectorization**: TF-IDF converts text into numeric vectors.  
4. **Similarity Calculation**: Cosine similarity finds closest matches in the dataset.  
5. **Recommendation**: Returns **top 5 most similar dramas** while highlighting diverse stories.  

---

## Tech Stack 🛠️  

| Layer | Technology |
|-------|------------|
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| ML/NLP | Pandas, NLTK, Scikit-learn (TF-IDF & Cosine Similarity) |
| Hosting | Render |
| Version Control | Git, GitHub |

---

## Installation & Setup 💻  

1. Clone the repo:  
   ```bash
   git clone https://github.com/sanidhya2506/NewMyMatcha.git
   cd NewMyMatcha

## File Structure 📂

NewMyMatcha/
│
├─ app.py               # Main Flask app
├─ recommender.py       # Recommendation logic
├─ requirements.txt     # Dependencies
├─ Procfile             # For Render deployment
├─ templates/           # HTML pages
│   ├─ index.html
│   ├─ genre.html
│   ├─ dramas.html
│   └─ contact.html


---

## Usage 🚀

1. Open the live app: [NewMyMatcha on Render](https://newmymatcha.onrender.com/)  
2. Explore by **genre** or **search for a BL drama** you like.  
3. Get **top 5 personalized recommendations** that focus on underrepresented stories.  
4. Add new dramas to the **Google Sheets dataset** to automatically update the recommendation engine.

---

## Contribution 🤝

- Everyone is welcome to contribute!  
- Steps to contribute:
  1. Fork the repository.  
  2. Create your feature branch:  
     ```bash
     git checkout -b feature-name
     ```  
  3. Commit your changes:  
     ```bash
     git commit -m "Add feature XYZ"
     ```  
  4. Push to the branch:  
     ```bash
     git push origin feature-name
     ```  
  5. Open a Pull Request for review.  

---

## License & Contact 📬

- **License**: MIT License  
- **Contact**: SANIDHYA SHARMA
- **Live Demo**: [https://newmymatcha.onrender.com/](https://newmymatcha.onrender.com/)  

> Built with ❤️ for BL drama fans and underrepresented communities everywhere.  
> Even on hectic days, with Engineers’ Day lost, the passion for this project never faded.
