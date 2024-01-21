export function getAuthTokenFromCookie() {
    // Retrieve the authToken from the cookie
    const cookies = document.cookie.split('; ');
    for (const cookie of cookies) {
      const [name, value] = cookie.split('=');
      if (name === 'authToken') {
        return decodeURIComponent(value);
      }
    }
    return null; // Return null if authToken is not found in the cookies
  }