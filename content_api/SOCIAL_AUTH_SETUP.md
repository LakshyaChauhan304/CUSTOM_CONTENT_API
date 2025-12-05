# Social Authentication Setup Guide

To enable social login (Google, Facebook, Apple), you need to obtain API keys from the respective developer consoles and configure them in your project.

## 1. Create a `.env` file

Copy the example file to create your local configuration file:

```bash
cp .env.example .env
# OR on Windows Command Prompt
copy .env.example .env
```

## 2. Google OAuth Setup

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Navigate to **APIs & Services** > **Credentials**.
4. Click **Create Credentials** > **OAuth client ID**.
5. Select **Web application**.
6. Add the following **Authorized redirect URIs**:
   - `http://127.0.0.1:8000/accounts/google/login/callback/`
7. Copy the **Client ID** and **Client Secret**.
8. Update your `.env` file:
   ```
   GOOGLE_CLIENT_ID=your_client_id_here
   GOOGLE_CLIENT_SECRET=your_client_secret_here
   ```

## 3. Facebook OAuth Setup

1. Go to [Meta for Developers](https://developers.facebook.com/).
2. Create a new App (Select **Consumer** or **Business** type).
3. Add **Facebook Login** product.
4. Go to **Settings** > **Basic**.
5. Copy the **App ID** and **App Secret**.
6. In **Facebook Login** > **Settings**, add `http://127.0.0.1:8000/accounts/facebook/login/callback/` to **Valid OAuth Redirect URIs**.
7. Update your `.env` file:
   ```
   FACEBOOK_CLIENT_ID=your_app_id_here
   FACEBOOK_CLIENT_SECRET=your_app_secret_here
   ```

## 4. Apple OAuth Setup

Apple Sign In is more complex and requires an Apple Developer Account ($99/year).

1. Go to [Apple Developer Account](https://developer.apple.com/account/).
2. Create an **App ID** with "Sign In with Apple" capability.
3. Create a **Service ID** and configure the return URL: `http://127.0.0.1:8000/accounts/apple/login/callback/`.
4. Create a **Private Key** for Sign In with Apple.
5. Update your `.env` file with the Client ID (Service ID) and Secret (generated JWT or key details depending on library usage).

> **Note**: For local development, Apple Sign In often requires HTTPS (e.g., using ngrok).

## 5. Restart Server

After updating the `.env` file, restart your Django server:

```bash
python manage.py runserver
```
