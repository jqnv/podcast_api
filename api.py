from flask import Flask, request,render_template
import requests

app=Flask(__name__)

ind="index.html"
@app.route('/my_app', methods=['GET','POST'])
def my_app():
    if request.method != 'GET':
        print("not GET")
        return render_template(ind)
    else:
        req_data = requests.get("https://rss.itunes.apple.com/api/v1/us/podcasts/top-podcasts/all/100/explicit.json")
        data = req_data.json()
        resul = data['feed']['results']
        name = request.args.get('name_1')
        return render_template(ind, params=resul, name=name)

if __name__ == '__main__':
    app.run(debug=True, port=8000)

