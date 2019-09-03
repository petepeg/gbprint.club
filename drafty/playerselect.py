from flask import (
    Blueprint, g, redirect, render_template, request, url_for, send_from_directory, current_app as app)
from . import playerlist
from .PDFmaker.PDFmaker import makePDF


bp = Blueprint('playerselect', __name__)

@bp.route('/')
def index():
    guilds = playerlist.guilds
    return render_template('playerselect/index.html', guilds = guilds)

@bp.route('/tips')
def tips():
    return render_template('playerselect/tips.html')

@bp.route('/about')
def about():
    return render_template('playerselect/about.html')

@bp.route('/makePDF', methods=('GET', 'POST'))
def download():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        user_list = []
        for card_name in data.values():
            user_list.append(card_name)
        filename = makePDF(user_list)
        return filename #js than redirects to download function

@bp.route('/download/<path:filename>')
def download_pdf(filename):
    print(app.config['UPLOAD_FOLDER'])
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)