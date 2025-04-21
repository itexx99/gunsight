# Production Deployment Checklist

This checklist contains what is needed to transition the project from development to a secure, production-ready deployment.

---

## 🛠️ Configuration

- Set `DEBUG = False` in `settings.py` to prevent leaking sensitive information.
- Set `ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com', 'IP_ADDRESS']`.
- Store your `SECRET_KEY` securely using environment variables or a secret manager.
- Configure `TIME_ZONE`, `USE_I18N`, and `USE_TZ` appropriately.

---

## 🌐 Hosting

- Choose a production host: DigitalOcean, AWS EC2, Linode, Heroku, Render, or Railway.
- Create a virtual server (preferably Ubuntu).
- Install Python, pip, and virtualenv.
- Set up Gunicorn to serve your Django app.
- Use Nginx as a reverse proxy to Gunicorn.
- Install Supervisor to manage your Gunicorn process (optional).

---

## 🗄️ Database

- Switch from SQLite to PostgreSQL or MySQL.
- Create a secure production database user and password.
- Update your `DATABASES` setting in `settings.py` to reflect the production DB.
- Set up automatic backups or snapshotting.

---

## 📦 Static and Media Files

- Run `python manage.py collectstatic` to gather static files in the `STATIC_ROOT`.
- Configure Nginx to serve static files (e.g., `/static/`) and media files (`/media/`).
- Ensure `STATIC_URL`, `STATIC_ROOT`, `MEDIA_URL`, and `MEDIA_ROOT` are correctly set.

---

## 🔐 Security Settings

- Use HTTPS by installing SSL via Let’s Encrypt and Certbot.
- Add the following to `settings.py`:
  ```python
  SECURE_SSL_REDIRECT = True
  SESSION_COOKIE_SECURE = True
  CSRF_COOKIE_SECURE = True
  X_FRAME_OPTIONS = 'DENY'
  SECURE_HSTS_SECONDS = 31536000
  SECURE_BROWSER_XSS_FILTER = True
  SECURE_CONTENT_TYPE_NOSNIFF = True
  ```

---

## 🌍 Domain and DNS

- Purchase a domain from a registrar (e.g., Namecheap, Google Domains).
- Set A record to point to your server's IP.
- Ensure Nginx is configured to handle requests to your domain.

---

## 📧 Email Setup (Optional but Recommended)

- Set up SMTP for sending email:
  ```python
  EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
  EMAIL_HOST = 'smtp.provider.com'
  EMAIL_PORT = 587
  EMAIL_USE_TLS = True
  EMAIL_HOST_USER = 'your@email.com'
  EMAIL_HOST_PASSWORD = 'your_password'
  ```
- Use Mailgun, SendGrid, or Gmail for production email.

---

## 🛡️ Error Logging and Monitoring

- Configure Django's logging in `settings.py`.
- Set up a third-party monitoring tool (e.g., Sentry) to capture production errors.
- Regularly monitor logs via journald, Supervisor, or Nginx logs.

---

## 🧪 Environment Variables

- Store secret keys and credentials outside of your codebase.
- Use `python-decouple` or `django-environ` to load env variables from `.env` files.

---

## 🗂️ Backup and Maintenance

- Schedule automatic database backups (e.g., using cron).
- Keep your software and packages up to date.
- Test restore procedures regularly.

---

## 🚀 Deployment Tools (Optional)

- Use Docker for container-based deployment.
- Automate deployment with Fabric or Ansible.
- Set up CI/CD with GitHub Actions, GitLab CI, or Bitbucket Pipelines.

---

## 🔄 Ready to Launch

- Test everything in a staging environment.
- Ensure SSL, database, email, and error logging are functioning.
- Remove or disable unused apps and routes.
- Monitor traffic and performance with tools like UptimeRobot or Netdata.

---

> Keep this checklist updated as your project grows!

