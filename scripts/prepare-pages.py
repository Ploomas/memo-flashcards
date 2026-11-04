"""Copy the editable app to the GitHub Pages publishing folder."""
from pathlib import Path
from shutil import copytree

root = Path(__file__).resolve().parent.parent
copytree(root / 'dist', root / 'docs', dirs_exist_ok=True)
(root / 'docs' / '.nojekyll').touch()
print('GitHub Pages files updated in docs/')
