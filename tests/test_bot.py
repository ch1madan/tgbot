# Simple function representing your bot's logic
def handle_start_command(user_name):
    return f"Hello {user_name}! I am your bot."

# The actual test function (must start with 'test_')
def test_handle_start_command():
    user = "Alice"
    expected_response = "Hello Alice! I am your bot."
    
    # Run the function and check the result
    actual_response = handle_start_command(user)
    
    assert actual_response == expected_response

def test_basic_math():
    # A simple "sanity check" test
    assert 1 + 1 == 2
