from flask import Flask, render_template, request, send_file
from scrapper import search_incruit
from file import save_to_csv

app = Flask(__name__) #웹 서버를 만들며 파일 이름ㅇ르 자동으로 넣음

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/search')
def search():
    keyword = request.args.get("keyword")
    # print(keyword)
    jobs = search_incruit(keyword,1)
    
    return render_template("search.html", jobs = enumerate(jobs), keyword=keyword)    

@app.route('/file')
def file():
    keyword = request.args.get("keyword")
    jobs = search_incruit(keyword,1)

    save_to_csv(jobs)

    return send_file("downloads.csv", as_attachment=True)


# @app.route("/hello")
# def hello():
#     return render_template("hello.html")

if __name__ == '__main__':
    app.run(
            host='0.0.0.0',
            port=int(os.environ.get("PORT", 5000))
        )