# -*- coding: utf-8 -*-
from flask import Flask, request, render_template

import os
import codecs

import pypandoc
import markdown

import gitinterface
import converterutils

app = Flask(__name__)
repo = gitinterface.GitInterface("repo")


@app.route("/", methods=['GET', 'POST'])
@app.route("/demo", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        network_file = request.files['file']
        if network_file.mimetype == 'application/octet-stream':
            return render_template('index.html', error='Please enter filename.')
        mdname = converterutils.get_md_version(network_file.filename)
        local_file = repo.repo.get_named_file('../' + mdname)
        if local_file is not None:
            md = local_file.read()
            local_file.close()
        else:
            md = converterutils.storage(network_file.filename,
                                        network_file, repo)
        format_md = md.decode('utf-8').replace('\\\n', '\n\n')
        return render_template('index.html', markdown=format_md)
    return render_template('index.html')


@app.route("/showtest/<filename>")
def showtest(filename):
    with codecs.open('md_output/%s' % filename, 'r', encoding='utf-8') as file:
        data = file.read()
    output = pypandoc.convert(data, 'html', format='markdown')
    return render_template('cv.html', markdown=output)


@app.route("/listdata")
def listdata():
    files = list(os.walk('./md_output'))[0][2]
    datas = [f.decode('utf-8') for f in files]
    return render_template('listdata.html', datas=datas)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4888)
