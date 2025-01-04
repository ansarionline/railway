from nicegui import ui
import os
@ui.page('/')
def home_page():
    ui.label('Welcome to my NiceGUI app!'
    ).style('font-size: 24px;')
    ui.button('Click Me', on_click=lambda: 
    ui.notify('It is working',position='center',type='positive')
    ).style('font-size: 18px;')
if __name__ in {'__main__','__mp_main__'}:
    port = int(os.environ.get('PORT', 5000))
    ui.run(host='0.0.0.0', port=port)
