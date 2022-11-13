import string

from random import shuffle, randint, choice
from flask import Flask, request
from datetime import datetime


app = Flask(__name__)

navi_bar = """
<p><a href="/">Main page</a>
    <a href="/whoami">whoami</a>
    <a href="/random">random</a>
    <a href="/source_code">source cod</a></p>
"""


@app.route('/')
def main():
    answer = f"""
    {navi_bar}
    <h1> Main page</h1>
    <h2> This is Flask HW </h2>
    <h3> Just chose one of page below, to check how its work </h3>
    {navi_bar}
    """
    return answer


@app.route('/whoami')
def whoami():
    answer = f"""
    {navi_bar}
    <h1>WHO AM I ???</h1>
    <h3> This is page to to know who R u </h3>
    <h3> your user-agent is: </h3> <p> {request.headers['User-Agent']}  </p>
    <h3> your ip-address is: </h3> <p> {request.remote_addr}  </p>
    <h3> server datetime is: </h3> <p> {datetime.now().strftime("date: %m/%d/%Y, time: %H:%M:%S")}  </p>
    {navi_bar}
    """
    return answer


@app.route('/random', methods=['GET', 'POST'])
def random():
    if request.method == "GET":
        answer_get = f"""
                {navi_bar}
                <h1>Random page</h1>
                <h3> This page for random... </h3>
                <form method="POST">
                    Length of random: <input name="length" input type=number placeholder="int from 1 to 100"> Default - 1. </br>
                    <h2>Need specials ?:</h2>
                     <p>
                    <input type="radio" value="1" class="form-check-input" name="specials"> </br> YEP!
                    </p>
                     <p>
                    <input type="radio" value="0" class="form-check-input" checked name="specials"> </br> NOPE!
                    </p>
                    <h2>Need digits?: </h2>
                     <p>
                    <input type="radio" value="1" class="form-check-input" name="digits"> </br> YEP!
                    </p>
                     <p>
                    <input type="radio" value="0" class="form-check-input" checked name="digits"> </br> NOPE!
                    </p>      
                    <h2>Only unic symbols?:</h2>      
                    <input type="radio" value="1" class="form-check-input" checked name="unic_symb"> </br> YEP!
                    </p>
                     <p>
                    <input type="radio" value="0" class="form-check-input"  name="unic_symb"> </br> NOPE!
                    </p>   
                    
                    <button type="submit" class="btn btn-primary">Submit</button>
                </form>
                {navi_bar}
                """
        return answer_get

    elif request.method == "POST":
        length = int(request.values.get('length')) if request.values.get('length') else 1
        specials = int(request.values.get('specials'))
        digits = int(request.values.get('digits'))
        unic_symb = int(request.values.get('unic_symb'))

        length = length if length != 0 and length in range(1, 100) else 100 if length >= 100 else 1

        random_digits = string.digits if digits else ''
        random_species = string.punctuation if specials else ''

        generated_string = string.ascii_letters + random_digits + random_species

        if unic_symb:
            generated_string = [i for i in generated_string]
            shuffle(generated_string)
        else:
            generated_string = [choice(generated_string) for _ in generated_string]
            shuffle(generated_string)

        generated_answer = ''.join([i for i in generated_string][0:length])
        answer_post = f"""
            {navi_bar}
            <h3>Your params is:</h3>
            {length =}, {specials = }, {digits = }, {unic_symb = } </br>
            <h2>Your species is:</h2>
            {generated_answer} </br>
            <form action="/random">
            <button>Заводим еще раз ?</button>
            {navi_bar}
            """
        return answer_post


@app.route('/source_code')
def source_cod():
    with open('flask_application.py') as f:
        code = f.read()

    a = f"""
    {navi_bar}
    <h1>source_cod</h1>
    <h2> This page for show U source code of Flask APP </h2>
    <xmp>
    {code}
    </xmp>
    {navi_bar}
    """
    return a


if __name__ == '__main__':
    app.run(debug=True)
