from flask import Flask , render_template, redirect, session

app=Flask(__name__)
app.secret_key='idk'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    
    else: 
        session['count'] += 1

    return render_template("index.html", count = session['count'])

@app.route('/reset')
def reset():
    session['count'] = 0
    return redirect('/')

if 'count' in session:
    print('key exists!')
else:
    print("key 'count' does NOT exist")



if __name__=="__main__":
    app.run(debug=True) 
