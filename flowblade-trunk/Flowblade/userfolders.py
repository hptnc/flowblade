"""
    Flowblade Movie Editor is a nonlinear video editor.
    Copyright 2012 Janne Liljeblad.

    This file is part of Flowblade Movie Editor <http://code.google.com/p/flowblade>.

    Flowblade Movie Editor is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Flowblade Movie Editor is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Flowblade Movie Editor. If not, see <http://www.gnu.org/licenses/>.
"""
import gi

from gi.repository import GLib
import os


import appconsts

USING_DOT_DIRS = 0
USING_XDG_DIRS = 1

_user_dirs = USING_DOT_DIRS

_xdg_prefs_file_exists = False
_dot_prefs_file_exists = False


_dot_dir = None

_xdg_config_dir = None
_xdg_data_dir = None
_xdg_cache_dir = None

# --------------------------------------------------------- interface
def init():
    global _dot_dir, _xdg_config_dir, _xdg_data_dir, _xdg_cache_dir
    _dot_dir = os.getenv("HOME") + "/.flowblade/"
    
    _xdg_config_dir = os.path.join(GLib.get_user_config_dir(), "flowblade")
    _xdg_data_dir = os.path.join(GLib.get_user_data_dir(), "flowblade")
    _xdg_cache_dir = os.path.join(GLib.get_user_cache_dir(), "flowblade")

    global _xdg_prefs_file_exists, _dot_prefs_file_exists

    _dot_prefs_file_exists = os.path.exists(_dot_dir + "prefs" )
    _xdg_prefs_file_exists = os.path.exists(_xdg_config_dir + "/prefs")

def get_config_dir():
    return _dot_dir

def get_data_dir():
    return _dot_dir

def get_cache_dir():
    return _dot_dir

def get_render_dir():
    return get_data_dir() + appconsts.RENDERED_CLIPS_DIR

def get_hidden_screenshot_dir_path():
    return get_cache_dir() + "screenshot/"
    
# ---------------------------------------------------------------- internal functions
def _get_dot_dir_path():
    return os.getenv("HOME") + "/.flowblade/"


def _create_dot_dirs():

    user_dir = _dot_dir

    if not os.path.exists(user_dir):
        os.mkdir(user_dir)
    if not os.path.exists(user_dir + mltprofiles.USER_PROFILES_DIR):
        os.mkdir(user_dir + mltprofiles.USER_PROFILES_DIR)
    if not os.path.exists(user_dir + AUTOSAVE_DIR):
        os.mkdir(user_dir + AUTOSAVE_DIR)
    if not os.path.exists(user_dir + BATCH_DIR):
        os.mkdir(user_dir + BATCH_DIR)
    if not os.path.exists(user_dir + appconsts.AUDIO_LEVELS_DIR):
        os.mkdir(user_dir + appconsts.AUDIO_LEVELS_DIR)
    if not os.path.exists(utils.get_hidden_screenshot_dir_path()):
        os.mkdir(utils.get_hidden_screenshot_dir_path())
    if not os.path.exists(user_dir + appconsts.GMIC_DIR):
        os.mkdir(user_dir + appconsts.GMIC_DIR)
    if not os.path.exists(user_dir + appconsts.MATCH_FRAME_DIR):
        os.mkdir(user_dir + appconsts.MATCH_FRAME_DIR)
    if not os.path.exists(user_dir + appconsts.TRIM_VIEW_DIR):
        os.mkdir(user_dir + appconsts.TRIM_VIEW_DIR)




def _create_xdg_dirs():


    # Config dirs
    if not os.path.exists(user_dir):
        os.mkdir(user_dir)

    # Data stuff that can break projects and cannot be regerated by app
    if not os.path.exists(user_dir + mltprofiles.USER_PROFILES_DIR):
        os.mkdir(user_dir + mltprofiles.USER_PROFILES_DIR)
    # rendered_clips dir was made in app.py line 180...ish
    # now we need to do it here, because prefs have no longer influence
    """
    def create_rendered_clips_folder_if_needed(user_dir):
        if prefs.render_folder == None:
            render_folder = user_dir + appconsts.RENDERED_CLIPS_DIR
            if not os.path.exists(render_folder + "/"):
                os.mkdir(render_folder + "/")
            prefs.render_folder = render_folder
    """
        
    # Cache, stuff that can be regerated by app or is transient
    """
    # now we need to do this here, because prefs have no longer influence
    def create_thumbs_folder_if_needed(user_dir):
    if prefs.thumbnail_folder == None:
        thumbs_folder = user_dir + appconsts.THUMBNAILS_DIR
        if not os.path.exists(thumbs_folder + "/"):
            os.mkdir(thumbs_folder + "/")
        prefs.thumbnail_folder = thumbs_folder
    """
    if not os.path.exists(user_dir + AUTOSAVE_DIR):
        os.mkdir(user_dir + AUTOSAVE_DIR)
    if not os.path.exists(user_dir + appconsts.GMIC_DIR):
        os.mkdir(user_dir + appconsts.GMIC_DIR)
    if not os.path.exists(user_dir + appconsts.MATCH_FRAME_DIR):
        os.mkdir(user_dir + appconsts.MATCH_FRAME_DIR)
    if not os.path.exists(user_dir + appconsts.TRIM_VIEW_DIR):
        os.mkdir(user_dir + appconsts.TRIM_VIEW_DIR)
    if not os.path.exists(utils.get_hidden_screenshot_dir_path()):
        os.mkdir(utils.get_hidden_screenshot_dir_path())
    if not os.path.exists(user_dir + appconsts.AUDIO_LEVELS_DIR):
        os.mkdir(user_dir + appconsts.AUDIO_LEVELS_DIR)
    if not os.path.exists(user_dir + BATCH_DIR):
        os.mkdir(user_dir + BATCH_DIR)





        
