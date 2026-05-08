#!/usr/bin/env python3
import os
import sys
import shutil

def init_bundle(project_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(base_dir, '..', 'templates')
    project_dir = os.path.join(os.getcwd(), project_name)
    
    if os.path.exists(project_dir):
        print(f"Error: {project_name} already exists")
        sys.exit(1)
    
    shutil.copytree(template_dir, project_dir)
    
    # Create symlinks in ~/project-hub/
    hub_dir = os.path.expanduser('~/project-hub')
    os.makedirs(hub_dir, exist_ok=True)
    
    for mvp in ['thutofund', 'lekgetho', 'ditshetelo', 'dikgwebo']:
        src = os.path.join(project_dir, mvp)
        dst = os.path.join(hub_dir, mvp)
        if os.path.exists(src):
            os.symlink(src, dst)
    
    print(f"Created {project_name} with all 4 Botswana MVPs")
    print(f"Symlinks created in ~/project-hub/")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python init_botswana_bundle.py <project_name>")
        sys.exit(1)
    init_bundle(sys.argv[1])
