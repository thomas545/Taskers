
def category_image_path(instance, filename):
    return "category/%s/%s/%s"% (instance.id, instance.name, filename)


def profile_image_path(instance, filename):
    return "profile/%s/%s/%s"% (instance.id, instance.user.username, filename)

