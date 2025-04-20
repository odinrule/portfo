# 參考https://github.com/aneagoie/portfo/tree/master
# vs code終端機輸入 flask --app python檔名稱（不含副檔名） run
# 或 flask --app python檔名稱（不含副檔名） run --debug

# 導入flask框架的render_template函式
from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')  # 使用flask框架，html檔預定在templates資料夾內


@app.route("/<string:page_name>")  # 變數page_name是字符串，可代入不同頁面名稱
def html_page(page_name):
    return render_template(page_name)


def write_to_txt(data):
    with open("database.txt", mode='a') as my_database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        my_database.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
    with open("database.csv", mode='a',  newline='', encoding='utf-8') as my_database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(
            my_database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()  # 使用者在contact.html填入的內容轉為字典
            # print(data)
            write_to_txt(data)
            write_to_csv(data)
            # return redirect('thankyou.html') # redirect較難與thankyou.html內的{{}}互動
            return render_template('thankyou.html', email=data['email'])
            # email=data['email']傳遞字典內email的對應value到thankyou.html內的{{email}}
        except:
            return "did not save in database."
    else:
        return 'something went wrong!'

# @app.route("/index.html")  # new route
# def index():
#     return render_template('index.html')


# @app.route("/works.html")
# def works():
#     return render_template('works.html')


# @app.route("/about.html")
# def about():
#     return render_template('about.html')


# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')


# 以上是server.py
