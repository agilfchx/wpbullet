import json
import os
import html

def convert_json_to_html(json_filepath, output_filepath):
    with open(json_filepath, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    if not data:
        return

    report_name = os.path.splitext(os.path.basename(json_filepath))[0]

    template_filepath = 'core/template.html'

    try:
        with open(template_filepath, 'r', encoding='utf-8') as template_file:
            template = template_file.read()
    except FileNotFoundError:
        print(f"Error: Template file not found at {template_filepath}")
        return

    if isinstance(data[0], dict):
        headers = [header.upper() for header in data[0].keys()]
    elif isinstance(data[0], list):
        headers = [f"Column {i+1}".upper() for i in range(len(data[0]))]
    else:
        print("Error: Unexpected data format.")
        return

    table_headers = ''.join(f'<th>{html.escape(header)}</th>' for header in headers)

    table_rows = ''
    for item in data:
        if isinstance(item, dict):
            severity = item.get('severity', '').lower()
            class_name = ''
            if severity == 'low':
                class_name = 'low'
            elif severity == 'medium':
                class_name = 'medium'
            elif severity == 'high':
                class_name = 'high'
            elif severity == 'critical':
                class_name = 'critical'
            
            row = ''.join(f'<td>{html.escape(str(item.get(header.lower(), "")))}</td>' for header in headers)
            table_rows += f'<tr class="{class_name}">{row}</tr>'
        elif isinstance(item, list):
            row = ''.join(f'<td>{html.escape(str(value))}</td>' for value in item)
            table_rows += f'<tr>{row}</tr>'
        else:
            row = ''
            table_rows += f'<tr>{row}</tr>'

    html_content = template.replace('{{ report_name }}', html.escape(report_name))
    html_content = html_content.replace('{{ table_headers }}', table_headers)
    html_content = html_content.replace('{{ table_rows }}', table_rows)

    try:
        with open(output_filepath, 'w', encoding='utf-8') as output_file:
            output_file.write(html_content)
    except IOError:
        print(f"Error: Failed to write HTML file to {output_filepath}")
        return
