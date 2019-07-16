from flask import Flask, request
from flask import render_template
from flask import Response
from lxml import etree, objectify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('xxe.html')

@app.route('/xxe', methods = ['POST', 'GET'])
def parse_xml():
    parsed_xml = []
    if request.method == 'POST':
        xml_file = request.files['xml']
        files = xml_file.read()
        parser = etree.XMLParser(no_network=False, dtd_validation=True)
        root = objectify.fromstring(files, parser)
        parsed_xmls = etree.tostring(root)
        parsed_xml.append(parsed_xmls)
    return Response(parsed_xml)

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 5000)
