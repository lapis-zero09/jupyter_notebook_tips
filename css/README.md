# jupyter css

## how to use

### Jupyter notebook or Jupyter Lab

```python
from IPython.display import display, HTML

css = '''
 **ここに作成したCSSを書く**
'''
display(HTML('<style type="text/css">%s</style>'%css))
```

try example

```python
from IPython.display import display, HTML
css = !wget https://raw.githubusercontent.com/lapis-zero09/jupyter_notebook_tips/master/css/jupyter_notebook/monokai.css -q -O -
css = "\n".join(css)
display(HTML('<style type="text/css">%s</style>'%css))
```

### Google Colaboratory

use [stylus](https://add0n.com/stylus.html).
