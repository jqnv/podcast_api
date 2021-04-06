from flask import Flask, request,render_template
import requests
import json
import ctypes  # An included library with Python install.


app=Flask(__name__)

ind="index.html"
req_data = requests.get("https://rss.itunes.apple.com/api/v1/us/podcasts/top-podcasts/all/100/explicit.json")


@app.route('/', methods=['GET','POST'])
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
        data = req_data.json()
        resul = data['feed']['results']
        name = request.args.get('name_1')
        top_bot=request.args.get('tb')
        json_save=request.args.get('JsonCheck')
        param_search = list()
        if top_bot:
            if top_bot=="Top 20":
                tb_range=range(0,20)
            elif top_bot == "Bottom 20":
                tb_range = range(len(resul)-20,len(resul))
            for num in tb_range:
                param_search.append(
                    {"name": resul[num].get("name"), "artworkUrl100": resul[num].get('artworkUrl100'),
                     "artistName": resul[num].get('artistName')})
            resul_f = param_search

        if name:
            for num in range(0, len(resul)):
                if (resul[num].get('name')).lower().find(name.lower())!=-1:
                    param_search.append({"name":resul[num].get("name"),"artworkUrl100": resul[num].get('artworkUrl100'), "artistName": resul[num].get('artistName')})
            resul_f = param_search
        if json_save=="yes":
            with open('data.json', 'w') as fp:
                json.dump(resul_f, fp,indent=4)
        return render_template(ind, params=resul_f,top_bot=top_bot)

if __name__ == '__main__':
    app.run(debug=True, port=7050)

