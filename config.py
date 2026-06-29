class Config:
    SECRET_KEY = 'super-secret-key-123'
    RECAPTCHA_PUBLIC_KEY = '6LcKETstAAAAAKa99z4i1hDvIHWAzzRgFcVvJCo-'
    RECAPTCHA_PRIVATE_KEY = '6LcKETstAAAAAAcY67QQXohDxha-y-COhbY0YO0d'
    # Rate Limiting settings
    RATELIMIT_DEFAULT = "5 per 5 minutes"