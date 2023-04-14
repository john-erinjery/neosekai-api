<h1 style="text-align:center;">neosekai-api</h1>

An Unoffical Python API for [neosekaitranslations.com](https://www.neosekaitranslations.com/)

<h2>Installation</h2>

from a terminal, run : 

```
pip install neosekai-api
```
in case of an error, go [here](https://github.com/john-erinjery/neosekai-api/wiki/Installation) in the Github Wiki.

<h2>Usage</h2>

- Go to the [Github wiki](https://github.com/john-erinjery/neosekai-api/wiki) for this project to read full usage tutorial.
- Below is a short and sweet version

```python
from neosekai_api import Novel, NovelChapter

novel = Novel('https://www.neosekaitranslations.com/novel/oresuki/')

chapter = NovelChapter('https://www.neosekaitranslations.com/novel/oresuki/volume-1/chapter-3-part-3/')
```

- `Novel` and `NovelChapter` are the two main objects in this API
- through these two objects, neosekai-api offers a list of functions that are specified in the [Github wiki](https://github.com/john-erinjery/neosekai-api/wiki).
  
<h2>neosekai-dl</h2>

neosekai-dl is a project that uses neosekai-api to download novels from [neosekaitranslations.com](https://www.neosekaitranslations.com/) as PDF. The project is also in it's starting stages, so please bear with me. It's not a far fetch to say I made this API for the sole purpose of making neosekai-dl

<h2>For Future Releases</h2>

If you are using this project and wish to see more features in it, do open an issue on [github.](https://github.com/john-erinjery/neosekai-api) As I mentioned, I built this API for making neosekai-dl. This project, as it is, is all that is required for me to make neosekai-dl. However, if you wish to see more features in this API, I would be glad to implement your needs.

<h2>On creating support for authentification</h2>

neosekai-api, at the moment, does NOT support the registraton of new users or the ability to log in to neosekaitranslations.com. <br/>
This is mostly because, In neosekaitranslations.com, the only thing a registered user can do is leave comments. Since I feel like commenting is better done on the website itself, I didn't implement this functionality in the program.