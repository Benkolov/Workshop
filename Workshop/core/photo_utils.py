
def apply_likes_count(photo):
    photo.likes_count = photo.photolike_set.count()
    return photo


def apply_user_liked_photo(photo):
    photo.is_liked_by_user = photo.likes_count > 0
    return photo
