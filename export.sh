rm workshop.md index.html workshop.py
jupyter nbconvert --to html workshop.ipynb
jupyter nbconvert --to markdown workshop.ipynb
jupyter nbconvert --to python workshop.ipynb
jupyter nbconvert --to slides workshop.ipynb --reveal-prefix "https://cdnjs.cloudflare.com/ajax/libs/reveal.js/2.6.2"
mv workshop.html index.html
mv workshop.slides.html slides.html
