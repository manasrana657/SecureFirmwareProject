roles = {
    "admin": [
        "upload_firmware",
        "approve_update",
        "view_logs"
    ],

    "operator": [
        "upload_firmware"
    ],

    "viewer": [
        "view_logs"
    ]
}

def check_permission(role, permission):
    return permission in roles.get(role, [])

# Demo
user_role = "operator"

if check_permission(user_role, "upload_firmware"):
    print("Upload Allowed")
else:
    print("Upload Denied")

if check_permission(user_role, "approve_update"):
    print("Approval Allowed")
else:
    print("Approval Denied")
