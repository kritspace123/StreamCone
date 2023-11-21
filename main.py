from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

counter_value1 = 0
counter_value2 = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''  # Добавляем переменную для отображения сообщения
    entered_text1 = ''
    entered_text2 = ''

    if request.method == 'POST':
        # Получаем текст из полей ввода на HTML-странице
        entered_text1 = request.form['text1']
        entered_text2 = request.form['text2']

        # Сохраняем текст в файл
        with open('Away_Name.txt', 'w', encoding='utf-8') as file:
            file.write(entered_text1)
        with open('Home_Name.txt', 'w', encoding='utf-8') as file:
            file.write(entered_text2)
        message = 'accept'  # Устанавливаем сообщение "accept"

    return render_template('index.html', message=message, entered_text1=entered_text1, entered_text2=entered_text2, counter_value1=counter_value1, counter_value2=counter_value2)

@app.route('/increment')
def increment():
    global counter_value1
    counter_value1 += 1
    update_counter_file()
    return jsonify({'counter_value1': counter_value1})

@app.route('/decrement')
def decrement():
    global counter_value1
    counter_value1 -= 1
    update_counter_file()
    return jsonify({'counter_value1': counter_value1})

@app.route('/reset')
def reset():
    global counter_value1
    counter_value1 = 0
    update_counter_file()
    return jsonify({'counter_value1': counter_value1})

@app.route('/increment2')
def increment2():
    global counter_value2
    counter_value2 += 1
    update_counter_file2()
    return jsonify({'counter_value2': counter_value2})

@app.route('/decrement2')
def decrement2():
    global counter_value2
    counter_value2 -= 1
    update_counter_file2()
    return jsonify({'counter_value2': counter_value2})

@app.route('/reset2')
def reset2():
    global counter_value2
    counter_value2 = 0
    update_counter_file2()
    return jsonify({'counter_value2': counter_value2})

def update_counter_file():
    with open('Away_Score.txt', 'w') as file:
        file.write(f"{counter_value1}")

def update_counter_file2():
    with open('Home_Score.txt', 'w') as file:
        file.write(str(counter_value2))

if __name__ == '__main__':
    #ipconfig
    app.run(host='192.168.31.20', port=5000, debug=True)
