from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gia Đình Việt</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://unpkg.com/aos@2.3.4/dist/aos.css" rel="stylesheet">
  <style>
    body { background:#0f172a; color:white; text-align:center; padding-top:20vh; font-family:sans-serif; }
    h1 { font-size:3rem; margin-bottom:1rem; }
    .btn-light { color:#0f172a; font-weight:bold; border-radius:12px; }
  </style>
</head>
<body data-aos="fade-up">
  <h1>Gia Đình Việt</h1>
  <p data-aos="fade-up" data-aos-delay="200">Website Flask demo trên Vercel</p>
  <a href="https://vercel.com" target="_blank" class="btn btn-light mt-3">Powered by Vercel</a>
  <script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>
  <script>AOS.init();</script>
</body>
</html>
""")
