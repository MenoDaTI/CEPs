from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ceps = request.form.getlist('cep')
        result = get_ceps_data(ceps)
        return render_template('index.html', result=result)

    return render_template('index.html')

def get_ceps_data(ceps):
    result = []
    for cep in ceps:
        api_url = f'https://viacep.com.br/ws/{cep}/json/'
        response = requests.get(api_url)
        data = response.json()
        result.append(data)
    return result

if __name__ == '__main__':
    app.run(debug=True)
