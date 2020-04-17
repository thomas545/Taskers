
def category_image_path(instance, filename):
    return "category/%s/%s/%s" % (instance.pk, instance.name, filename)


def profile_image_path(instance, filename):
    return "profile/%s/%s/%s" % (instance.user.username, filename)
