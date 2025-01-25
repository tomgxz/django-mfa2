from django.shortcuts import render as _render
from django.conf import settings

bcmap = {
    "???": "???",
    
    "email": ("Email", ""),
    "email_add": ("Add", ""),
    "email_start": ("Start", ""),
    
    "fido2": ("FIDO2", ""),
    "fido2_add": ("Add", ""),
    "fido2_recheck": ("Recheck", ""),
    
    "recovery": ("Recovery Codes", ""),
    "recovery_add": ("Add", ""),
    "recovery_recheck": ("Recheck", ""),
    
    "totp": ("Authenticator App", ""),
    "totp_add": ("Add", ""),
    "totp_recheck": ("Recheck", ""),
    
    "trusted_devices": ("Trusted Devices", ""),
    "trusted_devices_add": ("Add", ""),
    "trusted_devices_done": ("Done", ""),
    "trusted_devices_start": ("Start", ""),
    
    "u2f": ("U2F Key", ""),
    "u2f_add": ("Add", ""),
    "u2f_recheck": ("Recheck", ""),
}


def render(request,path,options={},*a,breadcrumbs=[],title="",**k):
    bcmap_prefix = settings.BCMAP_MFA_PREFIX or []
    
    options["current_page"]=""
    
    if breadcrumbs is not None:
        options["breadcrumbs"] = bcmap_prefix + list(map(lambda x: bcmap[x] if x != breadcrumbs[-1] else bcmap[x][0], breadcrumbs))
        if len(options["breadcrumbs"]):
            if type(options["breadcrumbs"][-1]) == tuple:
                options["breadcrumbs"][-1] = options["breadcrumbs"][-1][0]
    else:
        options["breadcrumbs"] = []
    
    options["pagemeta"] = {
        "sitename": "Finance Manager",
        "title": f"{title} | Finance Manager",
        "description": "",
        "domain": request.build_absolute_uri("/"),
        "pageurl": request.build_absolute_uri(),
        "canonicalurl": "finance.tomlx.co.uk",
        "image": {
            "type":"", "w":"", "h":"", "path":"",
        }
    }
    
    return _render(request,path,options,*a,*k)
