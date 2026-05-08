#!/usr/bin/env python3
"""
Initialize all 4 Botswana MVP applications with shared configuration.
"""
import os
import sys

def create_mvp(name, port, description):
    mvp_dir = f"./{name}"
    os.makedirs(f"{mvp_dir}/app/templates", exist_ok=True)
    os.makedirs(f"{mvp_dir}/app/static", exist_ok=True)
    
    # Create app.py
    with open(f"{mvp_dir}/app/__init__.py", "w") as f:
        f.write(f'"""Initializes the {name} application."""\n')
    
    with open(f"{mvp_dir}/app.py", "w") as f:
        f.write(f'''from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-key-change-in-prod'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{name.lower()}.db'
    app.config['PORT'] = {port}
    
    db.init_app(app)
    
    @app.route('/')
    def index():
        return render_template('index.html', title='{description}')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port={port}, debug=True)
''')
    
    with open(f"{mvp_dir}/app/templates/index.html", "w") as f:
        f.write(f'''<!DOCTYPE html>
<html><head><title>{description}</title></head>
<body><h1>{description}</h1><p>Running on port {port}</p></body></html>''')

if __name__ == '__main__':
    mvps = [
        ('thutofund', 9000, 'ThutoFund - Education Grants'),
        ('lekgetho', 9001, 'Lekgetho - Tax Filing'),
        ('ditshetelo', 9002, 'Ditshetelo - Legal Aid'),
        ('dikgwebo', 9003, 'Dikgwebo - Business Registry')
    ]
    
    for name, port, desc in mvps:
        create_mvp(name, port, desc)
        print(f"Created {name} on port {port}")
    
    print("\nAll MVPs created. Run each with: cd <name> && python app.py")
