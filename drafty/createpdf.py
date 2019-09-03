from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, json
)

bp = Blueprint('createpdf', __name__)

@bp.route('/userdata', methods=('GET', 'POST'))
def createpdf():
    if request.method == 'POST':
        data = request.get_json(force=True)
        print(data)
        #test = json.loads(data)
        #print(test)
        return redirect(url_for('createpdf.download'))
    

@bp.route('/download')
def download():

    return render_template('createpdf/download.html')
