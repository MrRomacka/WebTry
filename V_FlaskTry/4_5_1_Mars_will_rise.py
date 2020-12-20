from flask import Flask, url_for, request, render_template
import random as r
import json


app = Flask(__name__)


@app.route('/')
def start_page():
    return 'Миссия Колонизации Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promote():
    pr_list = ['ХЗ', "Что", "Тут", "Мне", "Писать"]
    return '<br>'.join(['<p>' + elem + '</p>' for elem in pr_list])


@app.route('/image_mars')
def image_mars():
    return render_template('img_mars.html')


@app.route('/promotion_img')
def promo_img():
    return render_template('promotion_img.html')


@app.route('/asker')
def ask():
    return render_template('austronaut_selection (1).html')


@app.route('/table/<sex>/<age>')
def show_room(sex, age):
    return render_template('tableroom.html',
                           sex = sex,
                           age = int(age))

@app.route('/member')
def random_member():
    with open('templates/cosmonauts.json') as info:
        data = info.read()
    json_data = json.loads(data)
    aus = r.choice(json_data['astronaut'])
    print(aus)
    return render_template('selfcard.html', name = aus['name'],
                    ali_photo = aus['photo'], specs = aus['specializations'])

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')