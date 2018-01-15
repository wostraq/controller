class DefaultConfig(object):
    # Get the app root path
    basedir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
    py_version = '{0.major}{0.minor}'.format(sys.version_info)
    DEBUG = False    
    TESTING = False
    SERVER_NAME = "controller.wostraq.net"
    SESSION_COOKIE_DOMAIN = ".wostraq.net"
    PREFERRED_URL_SCHEME = "https"
    INFO_LOG = "info.log"    
    ERROR_LOG = "error.log"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{basedir}/flaskbb.sqlite'.format(basedir=basedir)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    ALEMBIC = {        
      'script_location': os.path.join(basedir, "migrations"),
      'version_locations': get_alembic_branches()
      }    
    ALEMBIC_CONTEXT = {'render_as_batch': True}
    SECRET_KEY = 'secret key'
    WTF_CSRF_ENABLED = True    
    WTF_CSRF_SECRET_KEY = "reallyhardtoguess"
    LOGIN_VIEW = "auth.login"    
    REAUTH_VIEW = "auth.reauth"    
    LOGIN_MESSAGE_CATEGORY = "info"    
    REFRESH_MESSAGE_CATEGORY = "info"
    REMEMBER_COOKIE_NAME = "remember_token"
    REMEMBER_COOKIE_DURATION = datetime.timedelta(days=365)
    REMEMBER_COOKIE_DOMAIN = '.wostraq.net'
    REMEMBER_COOKIE_PATH = "/"
    REMEMBER_COOKIE_SECURE = None
    REMEMBER_COOKIE_HTTPONLY = False
    RATELIMIT_STORAGE_URL = "redis://localhost:6379"
    
def configure_app(app, config):    
  """Configures FlaskBB."""    
  # Use the default config and override it afterwards    
  app.config.from_object('controller.configs.default.DefaultConfig')
    
  if isinstance(config, string_types) and \            
  os.path.exists(os.path.abspath(config)):        
  config = os.path.abspath(config)        
  app.config.from_pyfile(config)    
  else:        
  # try to update the config from the object        
  app.config.from_object(config)    
  # Add the location of the config to the config    
  app.config["CONFIG_PATH"] = config
  app.config.from_envvar("WOSTRAQ_SETTINGS", silent=True)    
  app_config_from_env(app, prefix="WOSTRAQ_")
