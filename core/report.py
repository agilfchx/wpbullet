import json
import os
import re
from core.converter import convert_json_to_html

def save_report(name, data, filename):
    os.makedirs('reports/json', exist_ok=True)
    os.makedirs('reports/html', exist_ok=True)

    output = []
    if name == 'admin_actions':
        iterdata = iter(data)
        next(iterdata)
        for item in iterdata:
            output.append({
                'action_name': __(item[0]),
                'function': __(item[1]),
                'file': __(item[2])
            })

    elif name == 'ajax_hooks':
        iterdata = iter(data)
        next(iterdata)
        for item in iterdata:
            output.append({
                'action_name': __(item[0]),
                'function': __(item[1]),
                'file': __(item[2]),
                'user_input': __(item[3])
            })

    elif name == 'admin_init':
        iterdata = iter(data)
        next(iterdata)
        for item in iterdata:
            output.append({
                'function': __(item[0]),
                'file': __(item[1]),
                'user_input': __(item[2])
            })
    
    elif name == 'vulnerabilities':
        iterdata = iter(data)
        next(iterdata)
        for item in iterdata:
            output.append({
                'severity': __(item[0]),
                'vulnerability': __(item[1]),
                'file': __(item[2]),
                'info': __(item[3])
            })

    json_filepath = os.path.join('reports/json', filename + '_' + name +'.json')

    with open(json_filepath, 'w') as outfile:
        json.dump(output, outfile)

    html_filepath = os.path.join('reports/html', filename + '_' + name + '.html')
    convert_json_to_html(json_filepath, html_filepath)

def __(text):
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)
