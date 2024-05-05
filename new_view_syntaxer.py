'''
port of clbk_event_listener_win_view_new.on_load()
'''


global os_path_splitext
from os.path import splitext as os_path_splitext

global os_path_dirname
from os.path import dirname as os_path_dirname


class clbk_event_listener_win_view_new(sublime_plugin_EventListener):
    '''
        sets the new file (new views) syntax to the specified themes syntax
    '''


    # uri['_nvrn_st']['views_pathend_to_fold_on_view_load']
    # {relative_path : file_extension}
    rltpath_ext = {'\\Shell\\AutoHotKey': 'ahk'}

    # uri['_nvrn_us']['syntax']
    ext_rltpathpkg = {'__default__': 'Packages/Python/Python.sublime-syntax'
        'py': 'Packages/Python/Python.sublime-syntax'
        'py_magic': 'Packages/MagicPython/grammars/MagicPython.tmLanguage'
        'json': 'Packages/JavaScript/JSON.sublime-syntax'
        'ahk': 'Packages/AutoHotkey/AutoHotkey.sublime-syntax'}


    def on_load(self, view):
        '''
            executes automatically when new view is created and its file has been loaded
        '''

        # set the extension less files based on their folder path
        file = view.file_name()

        if file and not os_path_splitext(file)[1]:

            folder_path = os_path_dirname(file)
    
            for rlt, ext in self.rltpath_ext.items():

                if folder_path.startswith(rlt) or rlt in folder_path:

                    syntax_file = ext_rltpathpkg.get(ext, None)

                    if syntax_file:

                        view.set_syntax_file(syntax_file)

                    return

