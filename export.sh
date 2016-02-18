rm workshop.md index.html workshop.py
jupyter nbconvert --to html workshop.ipynb
jupyter nbconvert --to markdown workshop.ipynb
jupyter nbconvert --to python workshop.ipynb
jupyter nbconvert --to slides workshop.ipynb
mv workshop.html index.html
mv workshop.slides.html slides.html
