#!/usr/bin/python3

import os.path
from cgi import parse_qs, escape

from stdatm import StdAtm

def getHead():
    return """
    <html>
    <head><title>Standard Atmosphere calculations</title></head>
    <body>
      <h3> Standard Atmosphere calculations </h3>

      <form method="get" action="%s">
        <p>Height: <input type="text" name="height" />
        <input type='radio' name='unit' value='m' checked='checked' /> m
        <input type='radio' name='unit' value='ft' /> ft </p>
        <p><input type='submit' value='Calculate' /></p>
      </form>
    """ % (os.path.basename(__file__), )
    
def formatResults(data):

    return f"""
    <hr />
    <table border="0" cellpadding="5" cellspacing="0">
        <tr><td><b>Height:</b></td> <td>{data['h_m']:.1f} m, {data['h_ft']:.1f} ft</td></tr>
        <tr><td><b>Temperature:</b></td> <td>{data['temp_K']:.2f} K, {data['temp_C']:.2f} C</td></tr>
        <tr><td><b>Pressure:</b></td> <td>{data['pressure']:.2f} Pa</td></tr>
        <tr><td><b>Density:</b></td> <td>{data['rho']:.2f} kg.m<sup>-3</sup></td></tr>
        <tr><td><b>Mach 1:</b></td> <td>{data['mach1_si']:.2f} m/s, {data['mach1_kt']:.2f} knots</td></tr>
    </table>
    """

def getTail():
    return """
    </body>
    </html>
    """

def processInput(data):
    if "height" in data:
        height = data["height"][0]
        if data["unit"][0] == "m":
            data["h_m"] = float(height)
        else:
            data["h_ft"] = float(height)
        atm = StdAtm()
        atm.getResults(data)
        return formatResults(data)
    else:
        return ""
    
        
def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    response_body = getHead() + processInput(d) + getTail()

    status = '200 OK'

    # Now content type is text/html
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [bytes(response_body, 'utf-8')]


