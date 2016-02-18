rm workshop.md index.html workshop.py
jupyter nbconvert --to html workshop.ipynb
jupyter nbconvert --to markdown workshop.ipynb
jupyter nbconvert --to python workshop.ipynb
mv workshop.html index.html
