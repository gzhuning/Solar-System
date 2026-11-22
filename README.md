# Solar System Django starter

This repository now has a small Django project with a Study Hub home page and a Science Study page. The original `solar_system.html` stays in the repository unchanged; Django serves it at `/playground/` inside the Science Study page.

## Start the site on Windows

Open PowerShell in this folder and activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Then start Django's local development server:

```powershell
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in your browser to see Study Hub. Choose **Science Study** to open the solar system explorer. Press `Ctrl+C` in PowerShell to stop the server. If PowerShell says script activation is blocked, you can run Django without activating the environment:

```powershell
.\.venv\Scripts\python.exe manage.py runserver
```

## A few Django words

- **Project** (`config/`) is the main configuration for the website.
- **App** (`solar_system/`) is a smaller part of the project that handles solar system pages.
- **URL** (`solar_system/urls.py`) connects a web address to Python code. Study Hub is `/`, Science Study is `/science/`, and the original explorer is `/playground/`.
- **View** (`solar_system/views.py`) is Python code that responds to a URL. `home` supplies the subject list, `science` returns the Science Study page, and `playground` serves the existing standalone HTML file.
- **Template** (`solar_system/templates/solar_system/`) is HTML that Django fills in before sending it to the browser. The home template loops over the subject list, so future subjects can be added by adding a URL, view, and one entry in `home`.

`manage.py` is Django's command-line helper. For example, `python manage.py runserver` starts the local preview server.
