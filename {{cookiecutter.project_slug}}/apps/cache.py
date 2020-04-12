from flask_caching import Cache

cache = Cache()


def configure_cache(app):
    cache.init_app(app)
