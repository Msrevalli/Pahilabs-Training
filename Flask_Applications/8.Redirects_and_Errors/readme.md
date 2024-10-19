## Accessing the Application

1. Open your web browser and navigate to `http://127.0.0.1:5000/`. 
   - You should see the home page, which will automatically redirect you to the login page.

## Testing Error Handling

1. **401 Unauthorized**:
   - Click on the **Go to Protected Area** link. 
   - Since `user_has_access()` returns `False`, you will see the **401 Unauthorized** page.

2. **404 Not Found**:
   - You can also test the `404 Not Found` error by visiting a non-existent route like `http://127.0.0.1:5000/nonexistent`. 
   - This will display the **404 Not Found** error page.
