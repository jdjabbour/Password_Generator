from flask import Flask, render_template, request
import passgen

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=['POST'])
def result():
    if request.method == 'POST':
        numb = int(request.form['number'])
        numb = passgen.pwrd(numb)
        print(numb)

        wordnumb = int(request.form['charwords'])
        wordnumb = passgen.phrase(wordnumb)
        print(wordnumb)

        output = numb, wordnumb
        print(output)



    return render_template("result.html", variable=output)


if __name__ == '__main__':
    app.debug = True
app.run()