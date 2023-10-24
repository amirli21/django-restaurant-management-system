
def detect_user(user):
    roles = {1: 'vendor-dashboard', 2: 'customer-dashboard'}
    if user.role in roles:
        return roles[user.role]
    if user.is_superadmin:
        return '/admin'