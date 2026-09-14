# Palak Soni — Portfolio (Streamlit, v2)

Python-based animated portfolio: rotate-in scroll animations, a blob-shaped
photo frame, radial skill rings, and a smarter chatbot that answers only
from Palak's resume data.

## Run it locally

```
pip install -r requirements.txt
streamlit run app.py
```
(If `streamlit` isn't recognized as a command, use `python -m streamlit run app.py` instead.)

It opens at http://localhost:8501

## Deploy for free

1. Push this folder to a GitHub repo.
2. Go to share.streamlit.io, sign in with GitHub.
3. New app → pick the repo → main file `app.py` → Deploy.

## Files

- `app.py` — everything: layout, styling, animations, chatbot logic
- `assets/palak.jpg` — your photo
- `.streamlit/config.toml` — theme colors
- `requirements.txt` — just `streamlit`

## What's different from v1

- New color palette: warm coral + amber gradient on a near-black plum
  background (previously violet/teal).
- Sections now rotate + fade into view as you scroll (via a small
  IntersectionObserver script), instead of static sections.
- Skills shown as radial progress rings instead of tag chips.
- Photo is an animated organic "blob" shape instead of a rectangle.
- Contact section is a real form that opens your email app with the
  message pre-filled.
- Chatbot now uses fuzzy phrase matching (handles varied wording, not
  just exact keywords) but still only answers from Palak's data, with
  a clear fallback for anything else.

## Customizing

- Edit any text/section directly in `app.py`.
- Chatbot answers live in the `KB` list near the bottom of `app.py` —
  each entry is `(list_of_example_phrasings, answer_text)`.
- Colors are CSS variables at the top of the `st.markdown(...)` style
  block (`--coral`, `--amber`, `--indigo`, `--bg`, etc).

 ## Live Link

 https://palak-portfolio-u1ra.onrender.com
