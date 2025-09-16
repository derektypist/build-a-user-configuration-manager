def add_setting(settings,new_pair):
    key = new_pair[0].lower()
    value = new_pair[1].lower()
    
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings.update({key:value})
        return f"Setting '{key}' added with value '{value}' successfully!"
    

test_settings = {
    "theme": "light",
    "brightness": 80,
    "volume": "high"
}

print(add_setting(test_settings,("notifications","enabled")))

def update_setting(settings,key_value_pair):
    key = key_value_pair[0].lower()
    value = key_value_pair[1].lower()
    if key in settings:
        settings.update({key:value})
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings,key):
    key = key.lower()
    if key not in settings:
        return f"Setting not found!"
    else:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"

def view_settings(settings):
    if not settings:
        return "No settings available."
    else:
        settings_str = "Current User Settings:\n"
        for i, v in enumerate(settings.items()):
            settings_str += f"{v[0].capitalize()}: {v[1]}\n"
        return settings_str

print(view_settings(test_settings))
