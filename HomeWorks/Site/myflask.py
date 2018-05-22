from flask import Flask, render_template, url_for, request, redirect
import sqlite3
app = Flask(__name__)
@app.route("/")
def index():
    return "Hello world"

conn = sqlite3.connect("test.db", check_same_thread=False)
cursor = conn.cursor()
try:
    cursor.execute("""CREATE TABLE Friends
                      (Name, Second_name, Age, City)
                   """)

except sqlite3.OperationalError:
    pass


def addtodb(firstname, lastname, age, city):
    execute_last_commit = "SELECT * FROM Messages ORDER BY Id DESC LIMIT 1"
    cursor.execute(execute_last_commit)
    if cursor.fetchone() is None:
        cursor.execute("""INSERT INTO Friends
                          VALUES (Роман, 'Ваврик', 12, Львів)
                          """, )
        conn.commit()
        cursor.execute(execute_last_commit)
    else:
        cursor.execute(execute_last_commit)
    cursor.execute("""INSERT INTO Friends
                          VALUES ((?), (?), (?), (?))
                          """, (firstname, lastname, age, city,))
    conn.commit()



@app.route("/user/<username>")
def username(username):
    return "Your name is {}".format(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)

@app.route('/Page1/')
@app.route('/Page1/<name>/')
def hello(name=None):
    return render_template('Page1.html', myname=name)
@app.route("/Page2/<name>")
def page_2(name):
    print(name)
    return render_template('Page2.html', var_name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        friend_name = request.form['name']
        friend_second_name = request.form['second_name']
        friend_city = request.form['city']
        try:
            friend_name = int(request.form['name'])
            error = 'Помилка введених данних! Спробуй ще.'
        except:
            pass
        try:
            friend_second_name = int(request.form['second_name'])
            error = 'Помилка введених данних! Спробуй ще.'
        except:
            pass
        try:
            friend_city = int(request.form['city'])
            error = 'Помилка введених данних! Спробуй ще.'
        except:
            pass

        try:
            friend_age = int(request.form['age'])
            if not isinstance(friend_name, str) or not isinstance(friend_second_name, str) or not \
                    isinstance(friend_age, int) or not isinstance(friend_city, str):
                error = 'Помилка введених данних! Спробуй ще.'
            else:
                return redirect(url_for('returner', fname=friend_name, lname=friend_second_name, uage=friend_age,
                                        fcity=friend_city))
        except:
            error = 'Помилка введених данних! Спробуй ще.'



    return render_template('Page2.html', error=error)
@app.route("/Page3/<fname>/<lname>/<uage>/<fcity>", )
def returner(fname=None, lname=None, uage=None, fcity=None):
    addtodb(fname, lname, uage, fcity)
    a=(fname, lname, uage, fcity)
    lister = []
    for i in a:
        lister.append("{}\n".format(i))
    return "".join(lister)
if __name__ == '__main__':
    app.debug = True
    app.run(port=999)