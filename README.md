# Template-Repository

Dies ist ein Template, mit dem du neue Projekte erstellen kannst. Es enthält (oder sollte enthalten) alle grundlegenden Dateien, die man beim Einrichten eines neuen (Python-)Projekts benötigt.

## Verwendung

Folge den [Anweisungen hier](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template#creating-a-repository-from-a-template), um ein Repository mit diesem Template zu erstellen.

Sobald du das neue Repository erstellt hast, solltest du die folgenden Schritte durchführen, um dein Projekt einzurichten:

1. Installiere die benötigten Programme:
   - [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)
   - [VSCode](https://code.visualstudio.com/download)
   - [Python](https://realpython.com/installing-python/) – Es wird empfohlen, [`pyenv`](https://realpython.com/intro-to-pyenv/) zu verwenden, dies ist jedoch nicht erforderlich.

2. `poetry init` : Dies hilft dir, die Datei `pyproject.toml` für dein Projekt einzurichten.

3. `poetry install` : Installiert dein Projekt als Paket (sowie alle Abhängigkeiten, die du möglicherweise manuell in die Datei `pyproject.toml` hinzugefügt hast).

4. Danach kannst du beginnen, die Abhängigkeiten deines Projekts mit `poetry add xxxxx` zu definieren.

5. Erstelle einen neuen Ordner mit dem Namen deines Pakets. Achte darauf, dass der Name den [Anforderungen](https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html#packages) eines Python-Pakets entspricht. Wenn du dein Repository `my-cool-repo` genannt hast, ist es am besten, das Paket gleich zu benennen (aber mit Unterstrichen, da Bindestriche in Python-Paketnamen nicht erlaubt sind): `my_cool_repo`.

## Inhalt

Enthält:

- `poetry.toml`, welche festlegt, dass Poetry die `.venv` (virtuelle Umgebung) im Projektordner installieren soll. Dies kann nützlich sein, wenn du deinen Projektcode z. B. in einem Docker-Container bereitstellen möchtest.

- `.gitignore`-Datei mit einigen grundlegenden ausgeschlossenen Dateien. Diese Dateien werden nicht in dein Remote-Repository (z. B. GitHub) hochgeladen.

- `.vscode`-Ordner, der drei Dateien enthält:
  - `settings.json` : Definiert die Einstellungen für deinen Python-Interpreter (verwendet den im Projekt `.venv`, vorausgesetzt, du hast ihn im Projekt erstellt), Einstellungen für Testdateien und Einstellungen für einige VSCode-Erweiterungen, die dein Projekt verwenden sollte.
  - `extensions.json` : Definiert eine Reihe von VSCode-Erweiterungen, die du installieren solltest. Beim Öffnen des Repositorys in VSCode wirst du aufgefordert, fehlende Erweiterungen zu installieren, oder du kannst sie manuell aus der Erweiterungs-Seitenleiste installieren.
  - `launch.json` : Bietet ein Beispiel, wie eine Launch-Konfiguration eingerichtet werden kann. Nützlich, um vordefinierte Befehle aus deinem Python-Code auszuführen oder einen Befehl zu debuggen.

- `.python-version` : Legt fest, welche Python-Version im Projekt von `pyenv` verwendet werden soll. Standardmäßig ist dies Version 3.12, dies kann jedoch auf jede gewünschte Version geändert werden.

- `tests` : Ordner, der alle Tests (z. B. Unit-Tests) enthalten sollte, die du auf



# English

## Template Repo

This is a template which you can create new projects from. It has (or should have) all of the basic files one needs wwhen setting up a new (python) project. 

## Usage

Follow the [instructions here](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template#creating-a-repository-from-a-template) in order to create a repository using the template.

Once you have the new repository made, you should follow these steps to complete your project set-up:

1. Install pre-requisites
   - [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)
   - [VSCode](https://code.visualstudio.com/download) 
   - [Python](https://realpython.com/installing-python/) - Recommended to use [`pyenv`](https://realpython.com/intro-to-pyenv/) but not necessary.

2. `poetry init` : This will help you set-up the `pyproject.toml` file needed for your project. 

3. `poetry install` : Installs your project as a package (as well as any dependencies you may have manually added to the `pyproject.toml` file)
   
4. Afterwards you can start defining your project dependencies using `poetry add xxxxx`.

5. Create a new folder with the name of your package. Make sure that the name is compliant with the [requirements](https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html#packages) of a Python package. If you named your repository `my-cool-repo` then its best to name the package the same thing (but with underscores as dashes aren't allowed in python package names) `my_cool_repo`

## Contents

Contains:

- `poetry.toml` which specifies that poetry should install the `.venv` (virtual environment) in the project folder. This can be useful if you want to deploy your project code using something like a docker container.

- `.gitignore` file with some basic ignored files. These files will not be commited to your remote repository (e.g. to GitHub)

- `.vscode` folder which contains three files: 
  - `settings.json` : defines the settings for your python interpreter (uses the one in your project `.venv` assuming you built it inside the project), settings for test files, and settings for some VSCode extensions which your project should use.
  - `extensions.json` : defines a set of VSCode extensions which you should install. Upon opening the repository in VSCode you should be prompted to install any missing extensions, or you can install them manually from the extensions sidebar.
  - `launch.json` : provides a dummy example of how a lauch configuration can be setup. Useful for running some pre-defined commands from your python code, or for setting up a command you want to debug.

- `.python-version` : defines which python version should be used within the project by `pyenv`. Default is set to 3.12 but this can be changed to whatever version you want to use.

- `tests` : folder which should contain any tests (e.g. unit tests) you want to run on your project code. 