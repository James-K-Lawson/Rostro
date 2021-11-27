from flask import render_template, flash, redirect, request, send_from_directory, send_file, url_for, Response
from werkzeug.utils import secure_filename
import os, io
from app.forms import RosterForm
from app import app
import RostroBackend.Rostro as Rostro
import rails


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/form', methods = ['GET','POST'])
def form():
    form = RosterForm()
    if form.validate_on_submit():
        flash(f'Roster request sent for {form.username}')
        if 'roster' not in request.files:
            flash('No file part')
            print('file not uploading')
            return redirect(request.url)
        file = request.files['roster']
        # If the user  not select a file, the browser submits an
        # empty file hout a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
            print('THIS SECTION HAS BEEN ACCESSED (VALIDATE ON SUBMIT)')
            file.save(os.path.join(save_path, filename))
            # with open(content,'r') as f:
            #     g=io.StringIO(f.read())
            # temporarylocation=os.path.join(save_path,'temp.xlsx')
            # with open(temporarylocation,'wb') as out:
            #     out.write(g.read())            
            return redirect('/success', code= 307)
    return render_template('form.html', title = 'Home', form = form)

@app.route('/success', methods = ['get', 'post'])
def success():
    form_data = request.form
    temporarylocation="testout.xlsx"
    file_data = request.files['roster']
    username = form_data.get('username')
    rostertype = form_data.get('rostertype')
    file_data.filename = 'temp' + '.' + file_data.filename.split('.')[1]
    roster_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'],file_data.filename)
    file_data.save(roster_path)
    ros = Rostro.sort_roster(username, rostertype, roster_path)
    calpath = ros.create_ical()
    os.remove(roster_path)
    return render_template('success.html', username=username, filename = calpath, shiftcount = ros.shiftcount)

@app.route('/success/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    basename = os.path.basename(filename)
    uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, path = os.path.basename(filename))

# return_data = io.BytesIO()
# with open(filename, 'rb') as fo:
#     return_data.write(fo.read())
#     # (after writing, cursor will be at last byte, so move it to start)
#     return_data.seek(0)
# os.remove(filename)
# return send_file(return_data, mimetype='application/ics', attachment_filename=basename)