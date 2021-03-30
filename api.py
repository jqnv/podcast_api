from flask import Flask, request,render_template
import requests

app=Flask(__name__)

ind="index.html"
req_data = requests.get("https://rss.itunes.apple.com/api/v1/us/podcasts/top-podcasts/all/100/explicit.json")


@app.route('/my_app', methods=['GET','POST'])
def my_app():
    if request.method != 'GET':
        return render_template(ind)
    else:
        data = req_data.json()
        resul = data['feed']['results']
        name = request.args.get('name_1')
        return render_template(ind, params=resul)

@app.route("/"+ind, methods=['GET','POST'])
def index():
    if request.method != 'GET':
        return render_template(ind)
    else:

        #req_data = requests.get("https://rss.itunes.apple.com/api/v1/us/podcasts/top-podcasts/all/100/explicit.json")
        data = req_data.json()
        resul = data['feed']['results']
        name = request.args.get('name_1')
        print("digitado",name)
        if name:
            param_search=list()
            for num in range(0, len(resul)):
                if (resul[num].get('name')).lower().find(name.lower())!=-1:
                    param_search.append({"name":resul[num].get("name"),"artworkUrl100": resul[num].get('artworkUrl100'), "artistName": resul[num].get('artistName')})
            print(len(param_search))
            resul = param_search
        return render_template(ind, params=resul)

if __name__ == '__main__':
    app.run(debug=True, port=8000)

